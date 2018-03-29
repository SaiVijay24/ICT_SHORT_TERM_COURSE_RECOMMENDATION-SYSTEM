import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

#driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

###########################
x = []
y = []
#z = []
#t = []

with open('jobroles_link_only.csv', "r") as ifile:
    reader = csv.reader(ifile, delimiter=',')
    for row in reader:
        x.append(row[0])
        y.append(row[1])
        #z.append(row[2])
        #t.append(row[3])

#print(x)
#print(len(y))
print(y)

count = 0

for each_link in y:
#for each_link in range(count+1, len(y)):
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    #print(type(each_link))
    driver.get(each_link)  # open browser and browse url
    #driver.get(y[each_link]) #use with range
    url = driver.page_source
    soup = BeautifulSoup(url)

    #### job url
    job_title_div = soup.find('div', 'breadcrumb')  # div class="breadcrumb"
    job_title = job_title_div.find('span').get_text()
    job_title = job_title.replace('NICF Job Role: ', '')  # remove the front strings 'Course Details: '


    content_div = soup.find('article', 'article col-9')
    description_div = content_div.find('section','article-tab-content active')  ###### This includes responsibilities & requirements
    description = description_div.find('p').get_text().strip()

    temp = description.split("Functional Group:\xa0")
    temp1 = temp[1].split("Job Family:\xa0")
    temp2 = temp1[1].split("Also known as:\xa0")

    #print(temp1)
    #print(temp2)

    func_group = temp1[0]
    job_family = temp2[0]
    job_family = job_family.replace('Also known as:', '')

    aka = "[Empty]"
    try:                ###Avoid no AKA case
        aka = temp2[1]
        aka = aka.replace('\n', ' ')
    except IndexError:
        print("No AKA")

    with open('job_group.csv', 'a') as g:  # a for appending
        g.write(job_title + ";" + func_group + ";" + job_family + ";" + aka + '\n')

    ####################
    #####################

    competencies_div = content_div.find('div', 'article__accordion')

    try:

        competency_list = competencies_div.findAll('div', 'accordion-title')

        for each_competency in competency_list:
            competency_title = each_competency.get_text()  # get the title

            with open('job_competency.csv', 'a') as f:  # a for appending
                f.write(job_title + ";" + competency_title + '\n')

    except AttributeError: #no competency exist
        print("No competency info")
        with open('job_nocompetency.csv', 'a') as h:  # a for appending
            #h.write(job_title + ";" + str(y[each_link]) + '\n')
            h.write(job_title + ";" + each_link + '\n')



    driver.quit()  # quit browser
    time.sleep(2)  # delay 2 secs
    count += 1
    print(str(count) + " completed out of " + str(len(y)))


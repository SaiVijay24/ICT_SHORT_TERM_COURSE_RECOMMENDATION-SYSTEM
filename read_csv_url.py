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

with open('title_link2.csv', "r") as ifile:
    reader = csv.reader(ifile, delimiter=';')
    for row in reader:
        x.append(row[0])
        y.append(row[1])
        #z.append(row[2])

#print(x)
#print(len(y))
#print(z)

count = 0
for each_link in y:
#for each_link in range(0, 2):
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    #print(type(each_link))
    driver.get(each_link)  # open browser and browse url
    #driver.get(y[each_link]) #use with range
    url = driver.page_source
    soup = BeautifulSoup(url)

    #### competency url
    competency_div = soup.find('article')
    competency_list = competency_div.find('h3', text="Competencies this course provides").find_next_sibling('ul').findChildren('a')  # get all the competencies
    course_title_div = soup.find('div', 'breadcrumb')  # div class="breadcrumb"

    course_title = course_title_div.find('span').get_text()
    course_title = course_title.replace('Course Details: ', '')  # remove the front strings 'Course Details: '


    for each_competency in competency_list:
        competency_title = each_competency.get_text()  # get the title
        link = "https://www.imda.gov.sg" + each_competency['href']

        with open('course_competencies2.csv', 'a') as f:  # a for appending
            f.write(course_title + ";% " + competency_title + ";% " + link + '\n')

    driver.quit()  # quit browser
    time.sleep(2)  # delay 2 secs
    count += 1
    print(str(count) + " completed out of " + str(len(y)))


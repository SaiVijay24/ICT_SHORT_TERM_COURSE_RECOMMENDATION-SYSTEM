from bs4 import BeautifulSoup
import requests
import csv
import os
#import StringIO

#original url was protected by incapsula, unable to retrieve the contents. Need to download html and open as local file
#url = 'https://www.imda.gov.sg/nicf/training/courses-listing?page=1&ip=all'
url ='view-source_https___www.imda.gov.sg_nicf_training_courses-listing_page=1&ip=all.html'
#url ='iMDA_NICF.html'
#response = requests.get(url)

#soup = BeautifulSoup(response.content, "html.parser")
#soup = BeautifulSoup(response.content, "html5lib")
#soup = BeautifulSoup(response.content, "html.parser")
#soup = BeautifulSoup(url, "html5lib")
soup = BeautifulSoup(open(url).read())

course_list = soup.findAll('div','result-detail')
#print(response)
#print(soup.prettify())
#print(soup.findAll('div','result-detail')[0])
#print(soup.findAll('div').find(class_="result-detail"))


print("Total number of courses: "+ str(len(course_list))) #number of courses, course_list is type bs4.result.set
#print(type(course_list))

#initiallise individual course dictionary
ind_course_dict = {"title": "", "link": "", "provider": []}

##################### Function to grab tht title and link <- passing bs4 element tag, returning in 2 separate variables
#loop needed for all individual courses
def get_tittle_link(bs4_element_tag):
    #print(type(bs4_element_tag))
    #course_link = "https://www.imda.gov.sg" + bs4_element_tag.find('a').get('href') #concatenate homepage with relative link
    course_link = "https://www.imda.gov.sg" + bs4_element_tag.find('a').get('href') #concatenate homepage with relative link
    #print(course_link) #link for the course  #https://www.imda.gov.sg/nicf/content-store/courses/advance
    course_title = bs4_element_tag.find('a').string
    #print(course_title) #name of the course
    #ind_course_dict["title"] = course_title
    #ind_course_dict["link"] = course_link
    return course_title, course_link

##################### Function to grab all providers in a course <- passing bs4 element tag, returning a list
#loop needed to find all providers
def get_provider_list(course_list_elementTag):
    provider_list = [] #initialise empty list
    course_providers = course_list_elementTag.findAll('li') #all available course providers for a course #course_list type <class 'bs4.element.ResultSet'>
    #print(len(course_providers)) #length of course_providers (14)

    for providers in course_providers:
        provider_list.append(providers.get_text()) #use get_text for tag to extract text, append to the provider_list
    # print(type(provider_list)) class string type
    #print(provider_list)
    return provider_list

#ind_course_dict["title"], ind_course_dict["link"] = get_tittle_link(course_list)
#course_title, course_link = get_tittle_link(course_list[0]) #This sends the first course, course_list[0]
#print(course_title)

all_course_dict = {} #initialise overall dictionary
list_db = []
count = 0
for take_course in course_list:
    course_title, course_link = get_tittle_link(take_course) #get the course title and link
    ind_course_dict["title"] = course_title
    ind_course_dict["link"] = course_link
    #provider_list = take_course.findAll('li')[0].get_text() #use get_text for tag to extract text
    #print(course_title)

    ind_course_dict["provider"] = get_provider_list(take_course)
    provider_list = get_provider_list(take_course)
    #print(ind_course_dict)
    text = course_title + ";% "
    #s = StringIO.StringIO(text)
    #'{} {}'.format('one', 'two')
    provider_string = "{0}".format(";% ".join(str(i) for i in provider_list))  #concatenate everything in a list

    with open('title_provider2.csv', 'a') as f: #a for appending
        f.write(text + provider_string +'\n')


    with open('title_link2.csv', 'a') as g: #a for appending
        g.write(text + course_link +'\n')
    #list_db.append(ind_course_dict)
    #all_course_dict[course_title] = ind_course_dict
    #all_course_dict[count+1] = ind_course_dict
    count += 1
    #print(all_course_dict)


print(count)

"""
s = StringIO.StringIO(text)
with open('fileName.csv', 'w') as f:
    for line in s:
        f.write(line)
"""

"""
#print(ind_course_dict)
print(list_db[0])
print(list_db[1])
print(len(list_db))
#print(all_course_dict)
print("Total number of courses in dictionary: " + str(len(all_course_dict)))
print(all_course_dict["Agile Project Management Foundation Qualification"])

print(get_provider_list(course_list[457])) #get the provider list
print(get_provider_list(course_list[2])) #get the provider list



#print(ind_course_dict)

#print(get_provider_list(course_list[2])) #get the provider list

#ind_course_dict["provider"] = provider_list

#print(ind_course_dict)

#all_course_dict[ind_course_dict["title"]] = ind_course_dict
#all_course_dict[ind_course_dict["course_id"]] = ind_course_dict
#print(all_course_dict)

"""



"""
# troubleshooting purpose, not required
print(course_list[2].findAll('li')) #for a course, list all providers (list with 'li' elements)
print(len(course_list[2].findAll('li'))) #number of elements of <class 'bs4.element.ResultSet'>, provide index for tag
"""


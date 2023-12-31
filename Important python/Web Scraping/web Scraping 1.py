# libararies neeed:
# requests,html5lib,bs4

# requests: helps to get content.
#  html5lib: helps to parse html.
# bs4 : this parser use by beatufulsoup and convert it into tree like structure.

'''
If u want to scrape a website , you can do it by:
1. using the API.
2. using HTML web scraping some tool like bs4.
'''

import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com"

# step 1: Get the HTML:
r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)  # print all view source of site


# step2: Parse the HTML:
soup = BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify)


# step3: HTML Tree traversal:

title = soup.title
# print(title)    # get list of the title of the HTML page.
# print(title.string) # print the content of title.

# commonly used types of objects:
# 1. Tag:
# print(type(title))      # <class 'bs4.element.Tag'>
# 2. NavigableString:
# print(type(title.string))
# 3. BeautifulSoup:
# print(type(soup)
# 4.comment:
# markup = "<p><!-- this is comment --!></p>"
# soup2 = BeautifulSoup(markup)   # convert markup to soup.
# print(soup2.p)

# Get all the paragraph from the page:
paras = soup.find_all('p')  # get list of all the para of html page.
# print(paras)

# print(soup.find('p'))   # to get first para of html page.

# print(soup.find('p')["class"])  # to get list of class of first para.

# find all the elements with class lead:
# print(soup.find_all('p',class_="lead"))

# Get the text from the tag/soup:
# print(soup.find('p').string)
#       OR:
# print(soup.find('p').get_text())

# Get all the anchor tag from the page:
anchors = soup.find_all('a')    # get list of all anchor tags of the html page.
# print(anchors)

# get all the link from the page:
# for link in anchors:
#
#     print(link.get('href'))

id = soup.find(id = "__next")
# print(id.contents)  # get all content of that id.
# for elem in id.contents:
#     print(elem)
# to get all content in stripped manner:
# for ele in id.stripped_strings:
#     print(ele)

# print(id.parent)    # to get parent of that tag.
# for i in id.parents:
#     print(i.name)   # get all parent of id tag.

# print(id.nextSibling)
# print(id.previousSibling)

ele = soup.select('.px-3')    # buttom class name
print(ele)  # list of element of class name px-3
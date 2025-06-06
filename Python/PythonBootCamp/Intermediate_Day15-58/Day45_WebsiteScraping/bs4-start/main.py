from bs4 import BeautifulSoup
import requests
# import lxml 

FILE_DIRECTORY = ""
WORK_FILE_DIRECTORY = ""
WORK_FILE_DIRECTORY2 = ""

with open(f"{FILE_DIRECTORY}/website.html", errors='ignore') as file:
    contents = file.read()


soup = BeautifulSoup(markup=contents, features="html.parser")
# soup = BeautifulStoneSoup(contents, "html.parser")

print(soup.prettify())

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.a)
print(soup.h1)

print(soup.find_all(name='a'))
print(soup.find_all(name='h1'))
print(soup.find_all(name='h3'))

all_anchor_tags = soup.find_all(name='a')

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)
print(heading.getText())

section_heading = soup.find(name='h3', class_='heading')
print(section_heading)
print(section_heading.getText())

company_url = soup.select_one(selector='p a')
print(company_url)

name = soup.select_one(selector='#name')
print(name)

headings = soup.select(".heading")
print(headings)


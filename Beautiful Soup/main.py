# Basics of Beautiful Soup


#import lxml    (lxml is another module which will enable you to parse, create and modify XML and HTML Files)
from bs4 import BeautifulSoup


with open('website.html') as file:
    contents = file.read()
    

soup = BeautifulSoup(contents, 'html.parser')
print(soup.prettify())
print(soup.title())

all_anchor_tags = soup.find_all(name = 'a') # To get the links
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    
for tag in all_anchor_tags:
    print(tag.get('href'))   # To get only the links out
    
heading = soup.find(name = 'h1', id = 'name')
print(heading)

section_heading = soup.find(name = 'h3', class_ = 'heading')
print(section_heading)

print(section_heading.get('class'))

h3_heading = soup.find_all('h3', class_ = 'heading')
print(h3_heading)

company_url = soup.select_one(selector = 'p a')
print(company_url)

heading = soup.select('.heading')
print(heading)

name = soup.select_one(selector = '#name')
print(name)
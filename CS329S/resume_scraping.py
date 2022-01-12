import requests 
from bs4 import BeautifulSoup 
import csv 
import time

url = "https://www.postjobfree.com/resumes?q=Python+data+scientist&l=United+States&radius=25&r=100"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
title_tags = soup.find_all('h3', attrs = {'class': 'itemTitle'})
links = []
for title_tag in title_tags:
    links.append("https://www.postjobfree.com" + title_tag.a['href'])

# Use BeautifulSoup to scrape contents and job title 
results = []
for link in links:
    res = requests.get(link)
    print(res.status_code, link)
    content = BeautifulSoup(res. content, 'html.parser')
    results.append({
        'job_title': content.find('div', attrs = {'class': 'leftColumn'}).find('h1').get_text(),
        'resume': content.find('div', attrs = {'class': 'normalText'}).get_text()[:-23]
    })
    time.sleep(3)

## Write data into csv files 
with open('resumes.csv', 'w', encoding="utf-8") as csv_file:
     writer = csv.DictWriter(csv_file, fieldnames = results[0].keys())
     writer.writeheader()
     for row in results:
         writer.writerow(row)

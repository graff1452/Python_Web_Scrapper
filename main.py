from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    skills = job.find('div', class_='srp-skills')
    skill_list = []
    for skill in skills.find_all('span'):
        skill_list.append(skill.text.strip())

    if 'few' in published_date:
        print(f"Company Name: {company_name.strip()}")
        print(f"Required Skills: {skill_list}")
        print(f"Published Date: {published_date.strip()}")
        print('---' * 30)
# Libraries for web scrapping
# Request, BeautifulSoup, lxml, scrapy, Selenium
# API Keys
# Exercises, openweathermap.org

# Step 1: 
import requests
from bs4 import BeautifulSoup
import csv
import json

# Step 2: Fetch the web pages

url = 'http://ryeko.org'
response = requests.get(url)
html_content = response.text
api_key = 'user_api_key'

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 4: Find the specific data
data = []

for item in soup.find_all('a'):
    title = item.text.strip()
    link = item.get('href')
    data.append({'title': title, 'link': link})

# Step 5: Save the data to a CSV file
csv_file = 'scrapped_data.csv'
with open(csv_file, mode='w', newline='',encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'link'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

# Step 6: Save the data to a JSON file
json_file = 'scrapped_data.json'
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    
# Step 7: Save successfully to csv and json format
print('Data saved successfully to {csv_file} and {json_file} format!')

# Exercise 1: Scrape data from the https://openweathermap.org
# Current weather data
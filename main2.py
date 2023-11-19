from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

driver_path = r"C:\path\to\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument(f"webdriver.chrome.driver={driver_path}")
driver = webdriver.Chrome(options=chrome_options)

Source = []
Requirement = []
Quantity = []
Name = []
Number = []
Business = []
Location = []
Date = []

driver.get('https://seller.indiamart.com/enquiry/messagecentre?lv=1')
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for element in soup.findAll('div', attrs={'class': 'inbox-enq-cont'}):
    Source.append(element.find('div', attrs={'class': 'th_source'}).text)
    Requirement.append(element.find('div', attrs={'class': 'th_source'}).text)
    Quantity.append(element.find('div', attrs={'class': 'th_subject'}).text)
    Name.append(element.find('span', attrs={'class': 'nmibx'}).text)
    Number.append(element.find('span', attrs={'class': 'th_receiver_span numibx'}).text)
    Business.append(element.find('span', attrs={'class': 'th_receiver_span cmpibx'}).text)
    Location.append(element.find('td', attrs={'aria-label': 'tip--bottom-right th_conty ctibx'}).text)
    Date.append(element.find('td', attrs={'class': 'th_date'}).text)

df = pd.DataFrame({
    'Source': Source,
    'Requirement': Requirement,
    'Quantity': Quantity,
    'Name': Name,
    'Number': Number,
    'Business': Business,
    'Location': Location,
    'Date': Date
})

print(df)

df.to_csv('output.csv', index=False)



from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Corrected the import statement for BeautifulSoup
# Also, fixed the installation commands in the comments
# Make sure to run these commands in your terminal or command prompt
# pip install selenium
# pip install pandas
# pip install beautifulsoup4

# Use raw string for file paths to avoid escape character issues
driver = webdriver.Chrome(r"C:\Users\Admin\PycharmProjects\pythonProject\venv\Lib\site-packages\selenium\webdriver\chromedriver.exe")

# Use lists to store the data
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

# Find the correct div class name and attribute names
for element in soup.findAll('div', attrs={'class': 'inbox-enq-cont'}):
    Source.append(element.find('div', attrs={'class': 'th_source'}).text)
    Requirement.append(element.find('div', attrs={'class': 'th_source'}).text)
    Quantity.append(element.find('div', attrs={'class': 'th_subject'}).text)
    Name.append(element.find('span', attrs={'class': 'nmibx'}).text)
    Number.append(element.find('span', attrs={'class': 'th_receiver_span numibx'}).text)
    Business.append(element.find('span', attrs={'class': 'th_receiver_span cmpibx'}).text)
    Location.append(element.find('td', attrs={'aria-label': 'tip--bottom-right th_conty ctibx'}).text)
    Date.append(element.find('td', attrs={'class': 'th_date'}).text)

# Use pandas to create a DataFrame from the lists
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

# Print the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

# Close the WebDriver
driver.quit()

import requests
from bs4 import BeautifulSoup

url = 'https://uhmidtown.com/rates-floorplans/'
name = "University House Midtown"
address = "930 Spring St NW, Atlanta"

res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
elements = soup.find_all('div', class_='floorplan margin-pad big-bottom')
for element in elements:

    print('----------------------------------------------------------------------------------')

    rent = element.find('span', class_='special-rates').text.split('$')[1].replace(',', '').strip()
    rent = int(rent)
    available_date = '2023-08-15'

    bedrooms = int(element.find('span', class_='nobreak').text[0])
    bathrooms = bedrooms
    is_studio = False

    floorplan_num = int(2.5 + (2.5 - bedrooms))
    link = url + '#floorplan-' +  str(floorplan_num)

    print("rent: ", rent)
    print("bedrooms: ", bedrooms)
    print("bathrooms: ", bathrooms)
    print("link: ", link)
    print("available_date: ", available_date)
    print("apartment: ", name)
    print("is__studio: ", is_studio)

        


        
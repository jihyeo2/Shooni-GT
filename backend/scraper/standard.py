import requests
from bs4 import BeautifulSoup
import re
from datetime import date

url = 'https://thestandardatlanta.landmark-properties.com/floorplans/#studio-content'
name = "The Standard Atlanta"
address = "708 Spring St NW, Atlanta, GA 30308"


today = date.today()

res = requests.get(url).text

soup = BeautifulSoup(res, 'html.parser')

vectors = soup.find_all('div', class_='col-12 col-lg-6 text-center')
for vector in vectors:

    print('----------------------------------------------------------------------------------')

    # Studio

    rent = vector.find('div', class_='fp-prices').text.strip().replace(',','')
    num = re.findall(r'\d+', rent)
    listToStr = ' '.join([str(elem) for elem in num])
    if len(num) >= 2:
        rent = num[1]
    elif len(num) == 1:
        rent = listToStr
    else:
        rent = 0

    if rent != 0:
        link = "https://thestandardatlanta.landmark-properties.com/floorplans/"
        bedrooms = vector.find('span', class_='fp-beds').text.strip().replace('Bed','')

        if bedrooms == "1":
            Link = link + "#one-bed-content"
        elif bedrooms == "2":
            Link = link + "#two-beds-content"
        elif bedrooms == "3":
            Link = link + "#three-beds-content"
        elif bedrooms == "4":
            Link = link + "#four_beds-content"
        else:
            Link = link + "#five_beds-content"

        if bedrooms == "Studio":
            Studio = True
            bathrooms = 1
            Link = link + "#studio-content"
        else:
            Studio = False
            bathrooms = vector.find('span', class_='fp-baths').text.strip().replace('Bath','')

        size = vector.find('span', class_='fp-sqft').text.replace('FT','').replace('SQ','').strip()




        print("rent: ", rent)
        print("bedrooms: ", bedrooms)
        print("bathrooms: ", bathrooms)
        print("size: ", size)
        print("Apartment Name: ", name)
        print("Available Date: ", today)
        print("link: ", Link)
        print("Studio: ", Studio)

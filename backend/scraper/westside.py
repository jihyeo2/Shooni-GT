import requests
from bs4 import BeautifulSoup
import datetime


url = 'https://www.bowerwestside.com/atlanta/bower-westside/conventional/'
name = "Bower Westside"
address = "1000 Northside Dr NW Atlanta"

res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')

vectors = soup.find_all('div', class_='inner-card-container')
for vector in vectors:

    print('----------------------------------------------------------------------------------')
    rent = vector.find('ul', class_='fp-details').text.split()[11].replace(',','')
    num = ""
    for c in rent:
        if c.isdigit():
            num = num + c



    bedrooms = vector.find('ul', class_='fp-details').text.split()[0]
    bathrooms = vector.find('ul', class_='fp-details').text.split()[3]
    size = vector.find('ul', class_='fp-details').text.split()[6].replace(',','')


    Studio = False
    deposit = 500

    link = vector.find('a', class_='primary btn')
    Link = link.get('href')

    dates = vector.find('span', class_='fp-special-date').text.strip().replace(',','').split()
    if len(dates) == 4:
        mnum = datetime.datetime.strptime(dates[1], '%b').month
        dates = dates[3] + str(mnum) + dates[2]
        format_str = '%Y%m%d' # The format
        datetime_obj = datetime.datetime.strptime(dates, format_str)
        dates = datetime_obj.date()

    else:
        dates = -1


    print("rent: ", num)
    print("bedrooms: ", bedrooms)
    print("bathrooms: ", bathrooms)
    print("deposit: ", deposit)
    print("size: ", size)
    print("Apartment Name: ", name)
    print("Available Date: ", dates)
    print("Studio: ", Studio)
    print("link: ", Link)

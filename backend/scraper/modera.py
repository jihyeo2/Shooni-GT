import requests
from bs4 import BeautifulSoup
import datetime


url = 'https://www.moderamidtown.com/atlanta/modera-midtown/conventional/'
name = "Modera Midtown"
address = "95 8th St NW, Atlanta, GA 30309"

res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')

vectors = soup.find_all('div', class_='fp-col-wrapper')
for vector in vectors:

    print('----------------------------------------------------------------------------------')

    # Studio
    rent = vector.find('div', class_='fp-col-text').text.split()[2].replace('$', '').split('/')[0].replace(',', '').strip()
    rent = int(rent)


    bedrooms = vector.find('div', class_='fp-col bed-bath').text.split('/')[1].replace(',','').strip().replace('Baths', '').replace('bd','')
    bathrooms = vector.find('div', class_='fp-col bed-bath').text.split('/')[2].replace(',','').strip().replace('ba','')
    if bedrooms == "Studio":
        Studio = True
    else:
        Studio = False

    deposit = 300

    size = vector.find('div', class_='fp-col sq-feet').text.replace('Ft','').replace('Sq.','').strip().replace(',','').replace('+','')

    dates = vector.find('a', class_='primary-action').text.strip().replace(',','').split()
    if len(dates) == 4:
        mnum = datetime.datetime.strptime(dates[1], '%b').month
        dates = dates[3] + str(mnum) + dates[2]
        format_str = '%Y%m%d' # The format
        datetime_obj = datetime.datetime.strptime(dates, format_str)
        dates = datetime_obj.date()

    else:
        dates = -1



    link = vector.find('a', class_='secondary-action')
    Link = link.get('href')

    print("rent: ", rent)
    print("bedrooms: ", bedrooms)
    print("bathrooms: ", bathrooms)
    print("deposit: ", deposit)
    print("size: ", size)
    print("Apartment Name: ", name)
    print("Available Date: ", dates)
    print("Studio: ", Studio)
    print("link: ", Link)



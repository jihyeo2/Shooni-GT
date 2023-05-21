from bs4 import BeautifulSoup
from shooni_apartments.shared import Article, Apartment
import datetime

class Modera(Apartment):

    name = "Modera Midtown"
    address = "95 8th St NW, Atlanta, GA 30309"
    url = 'https://www.moderamidtown.com/atlanta/modera-midtown/conventional/'

    def get_all(self):

        articles = []
        res = self.session.get(self.url).text
        soup = BeautifulSoup(res, 'html.parser')
        vectors = soup.find_all('div', class_='fp-col-wrapper')
        for vector in vectors:

            # Studio
            rent = vector.find('div', class_='fp-col-text').text.split()[2].replace('$', '').split('/')[0].replace(',', '').strip()
            rent = int(rent)


            bedrooms = vector.find('div', class_='fp-col bed-bath').text.split('/')[1].replace(',','').strip().replace('Baths', '').replace('bd','')
            bathrooms = vector.find('div', class_='fp-col bed-bath').text.split('/')[2].replace(',','').strip().replace('ba','')

            if bedrooms == "Studio":
                is_studio = True
            else:
                is_studio = False

            # deposit = 300

            # size = vector.find('div', class_='fp-col sq-feet').text.replace('Ft','').replace('Sq.','').strip().replace(',','').replace('+','')

            dates = vector.find('a', class_='primary-action').text.strip().replace(',','').split()

            if len(dates) == 4:
                mnum = datetime.datetime.strptime(dates[1], '%b').month
                dates = dates[3] + str(mnum) + dates[2]
                format_str = '%Y%m%d' # The format
                datetime_obj = datetime.datetime.strptime(dates, format_str)
                available_date = str(datetime_obj.date())

            else:
                available_date = "TBA"

            link = vector.find('a', class_='secondary-action')
            link = link.get('href')

            bedrooms = int(bedrooms)
            bathrooms = int(bathrooms)

            articles.append(Article(self.address, rent, bedrooms, bathrooms, link, available_date, self.name, is_studio))

        return articles
            # print("deposit: ", deposit)
            # print("size: ", size)
 



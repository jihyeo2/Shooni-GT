from bs4 import BeautifulSoup
import datetime
from shooni_apartments.shared import Article, Apartment

class BowerWestside(Apartment):

    name = "Bower Westside"
    address = "1000 Northside Dr NW, Atlanta"
    url = 'https://www.bowerwestside.com/atlanta/bower-westside/conventional/'

    def get_all(self):

        articles = []
        res = self.session.get(self.url).text
        soup = BeautifulSoup(res, 'html.parser')
        vectors = soup.find_all('div', class_='inner-card-container')
        for vector in vectors:
            rent = vector.find('ul', class_='fp-details').text.split()[11].replace(',','')
            num = ""
            for c in rent:
                if c.isdigit():
                    num += c

            bedrooms = int(vector.find('ul', class_='fp-details').text.split()[0])
            bathrooms = int(vector.find('ul', class_='fp-details').text.split()[3])
            # size = vector.find('ul', class_='fp-details').text.split()[6].replace(',','')


            is_studio = False
            # deposit = 500

            link = vector.find('a', class_='primary btn')
            link = link.get('href')

            dates = vector.find('span', class_='fp-special-date').text.strip().replace(',','').split()
            if len(dates) == 4:
                mnum = datetime.datetime.strptime(dates[1], '%b').month
                dates = dates[3] + str(mnum) + dates[2]
                format_str = '%Y%m%d' # The format
                datetime_obj = datetime.datetime.strptime(dates, format_str)
                available_date = str(datetime_obj.date())

            else:
                available_date = "TBA"

            rent = int(num)

            articles.append(Article(self.address, rent, bedrooms, bathrooms, link, available_date, self.name, is_studio))

        return articles


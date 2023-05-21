from bs4 import BeautifulSoup
from shooni_apartments.shared import Article, Apartment
import re

class Standard(Apartment):
    name = "The Standard at Atlanta"

    address = "708 Spring St NW, Atlanta, GA 30308"
    url = 'https://thestandardatlanta.landmark-properties.com/floorplans/'

    def get_all(self): 

        articles = []
        res = self.session.get(self.url).text
        soup = BeautifulSoup(res, 'html.parser')
        vectors = soup.find_all('div', class_='col-12 col-lg-6 text-center')
        for vector in vectors:
            link = self.url
            rent = vector.find('div', class_='fp-prices').text.strip().replace(',','')
            num = re.findall(r'\d+', rent)
            listToStr = ' '.join([str(elem) for elem in num])
            if len(num) >= 2:
                rent = num[1]
                rent = int(rent.strip())
            elif len(num) == 1:
                rent = listToStr
                rent = int(rent.strip())
            else:
                rent = 0

            if rent != 0:
                bedrooms = vector.find('span', class_='fp-beds').text.strip().replace('Bed','').strip()

                if bedrooms == "Studio":
                    is_studio = True
                    bedrooms = 1

                    bathrooms = 1
                    link += "#studio-content"
                else:
                    is_studio = False
                    bedrooms = int(bedrooms)
                    bathrooms = int(vector.find('span', class_='fp-baths').text.strip().replace('Bath','').strip())
                    if bedrooms == "1":
                        link += "#one-bed-content"
                    elif bedrooms == "2":
                        link += "#two-beds-content"
                    elif bedrooms == "3":
                        link += "#three-beds-content"
                    elif bedrooms == "4":
                        link += "#four_beds-content"
                    else:
                        link += "#five_beds-content"

                available_date = "TBA"
                # size = vector.find('span', class_='fp-sqft').text.replace('FT','').replace('SQ','').strip()


                articles.append(Article(self.address, rent, bedrooms, bathrooms, link, available_date, self.name, is_studio))
        
        return articles
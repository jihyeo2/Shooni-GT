from bs4 import BeautifulSoup
from shooni_apartments.shared import Article, Apartment

class UHMidtown(Apartment):
    name = "University House Midtown"
    address = "930 Spring St NW, Atlanta"
    url = "https://uhmidtown.com/rates-floorplans/"

    def get_all(self):

        articles = []
        page = self.session.get(self.url).text
        soup = BeautifulSoup(page, 'html.parser')
        elements = soup.find_all('div', class_='floorplan margin-pad big-bottom')
        for element in elements:
            link = self.url 
            rent = element.find('span', class_='special-rates').text.split('$')[1].replace(',', '').strip()
            rent = int(rent)
            available_date = '2023-08-15'
        
            bedrooms = int(element.find('span', class_='nobreak').text[0])
            bathrooms = bedrooms
            is_studio = False

            link += "#floorplan-" + str(5 - bedrooms)

            articles.append(Article(self.address, rent, bedrooms, bathrooms, link, available_date, self.name, is_studio))
        
        return articles

        
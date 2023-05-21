# Reference: https://github.com/uiuc-apartments/uiuc-apartments.com 

from abc import ABC, abstractmethod
import requests

class Article:
    def __init__(self, address, rent, bedrooms, bathrooms, link, available_date, apartment, is_studio):
        self.address = address
        self.rent = rent
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.link = link
        self.available_date = available_date
        self.apartment = apartment
        self.is_studio = is_studio

    def __str__(self):
        info = 'Studio' if self.is_studio else f'{self.bedrooms} beds/{self.bathrooms} baths'
        return f"<{self.apartment} ${self.rent}/month {info} {self.available_date}>"
    __repr__ = __str__

class Apartment(ABC):
    name: str
    url: str
    address: str
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'https://shooni.org - crawler'})

    @abstractmethod
    def get_all(self):
        pass
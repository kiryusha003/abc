from bs4 import BeautifulSoup as bs
import requests
class CinemaParser:
    def __init__ (self,city='msk'):
        self.city=city
    def get_films_list():
      for item in parsed_main_page.find_all("div", class_='movie-plate'):
        a.append(item['attr-title'])
     return a
get_films_list()


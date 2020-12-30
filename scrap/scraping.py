from bs4 import BeautifulSoup
from pprint import pprint
import requests


class Scraping():

    def __init__(self):
        self.url = 'https://jadwalsholat.pkpu.or.id/?id=266'
        self.webpage = requests.get(self.url)
        self.soup = BeautifulSoup(self.webpage.text, 'html.parser')
        self.data = self.soup.find_all('tr', 'table_highlight')

    def prayer_times(self):
        response = self.data[0]

        waktu_sholat = {}
        i = 0

        for d in response:
            if i == 1:
                waktu_sholat['subuh'] = d.get_text()
            elif i == 2:
                waktu_sholat['dhuhur'] = d.get_text()
            elif i == 3:
                waktu_sholat['ashar'] = d.get_text()
            elif i == 4:
                waktu_sholat['maghrib'] = d.get_text()
            elif i == 5:
                waktu_sholat['isya'] = d.get_text()
            i += 1

        return waktu_sholat

    def spesific_prayer_times(self, s=''):
        response = self.data[0]

        waktu_sholat = {}
        i = 0

        for d in response:
            if i == 1:
                waktu_sholat['subuh'] = d.get_text()
            elif i == 2:
                waktu_sholat['dhuhur'] = d.get_text()
            elif i == 3:
                waktu_sholat['ashar'] = d.get_text()
            elif i == 4:
                waktu_sholat['maghrib'] = d.get_text()
            elif i == 5:
                waktu_sholat['isya'] = d.get_text()
            i += 1

        return waktu_sholat[s]

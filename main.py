from bs4 import BeautifulSoup
import requests

url_pkpu = 'https://jadwalsholat.pkpu.or.id/?id=266'
result = requests.get(url_pkpu)
response = BeautifulSoup(result.text, features="html.parser")

data = response.find_all('tr', 'table_highlight')
data = data[0]

waktu_sholat = {}
i = 0

for d in data:
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

print(waktu_sholat)

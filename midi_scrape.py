from bs4 import BeautifulSoup as bs
import requests
import os 

# os.chdir(r"midi") 

DOMAIN = 'http://metal-midi.grahamdowney.com'
URL = 'http://metal-midi.grahamdowney.com/midi.html'
FILETYPE = '.mid'

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

for link in get_soup(URL).find_all('a'):
    print(link.get('href'))
    if link.get('href') != None:
        file_link = link.get('href')
        if FILETYPE in file_link:
            try:
                with open(link.text.strip() + '.mid', 'wb') as file:
                    print(DOMAIN + file_link)
                    try:
                        repsonse = requests.get(DOMAIN + file_link)
                        file.write(repsonse.content)
                    except:
                        print("error occured \n \n")
            except:
                print(link.text.strip() + '.mid')
                print("Write Error occured \n \n")
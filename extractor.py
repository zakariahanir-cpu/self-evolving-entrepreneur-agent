from bs4 import BeautifulSoup
import scrapy

def extract_data(website):
    soup = BeautifulSoup(website, 'html.parser')
    data = []
    for link in soup.find_all('a'):
        data.append(link.get('href'))
    return data
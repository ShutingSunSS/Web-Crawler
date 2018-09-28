import requests
import bs4
from multiprocessing import Pool
import numpy as np
import pandas as pd

root_url = 'https://us.money2020.com'
parent_page = requests.get('https://us.money2020.com/2017-sponsors-text-list')
parent_soup = bs4.BeautifulSoup(parent_page.content, "html.parser")

def get_names():
    full_name = []
    for a in parent_soup.find_all('a', attrs = {'class': "sponsors-text-list-item"}):
        full_name.append(a.contents[0])
    return full_name
    
    
def get_urls():
    full_link = []
    for a in parent_soup.find_all('a', attrs = {'class': "sponsors-text-list-item"}):
        full_link.append(root_url + a['href'])
    return full_link

def get_contents(url):
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    for div in soup.find_all('div', attrs = {'class': "company-detail-column-2 w-richtext"}):
        return div.find('p').contents[0]

def main():
    full_link = get_urls()
    full_name = get_names()
 #   full_name = [my name is Shuting]
 #   full_link = ['https://us.money2020.com/companies/zafin'] 
    link_contents = []
    for url in full_link:
        link_contents.append(get_contents(url))
    TwoDim = [full_name, link_contents]
    Data = pd.DataFrame(TwoDim)
    Data.to_csv('mine1.csv')

if __name__ == "__main__":
    main()

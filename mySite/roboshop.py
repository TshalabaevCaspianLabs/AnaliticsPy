import requests
from bs4 import BeautifulSoup as bs
import time
from loguru import logger
from multiprocessing import Pool

def get_html(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            logger.error('Not Connect Html')
            return 0
    except:
        pass


def get_links_product(url):
    html = get_html(url)
    if html == 0:
        logger.error('Not connection links product')
        pass
    else:
        soup = bs(html, 'lxml')
        all_product_links = []

        div = soup.find('div', class_='list-group')
        a_list = div.find_all('a')

        for a in a_list:
            text = a.get('href')
            all_product_links.append(text + '?limit=200')

        return all_product_links

def get_name_and_count_product(url):
    try:
        html = get_html(url)
        if html == 0:
            logger.error('Not connection name and count')
            pass
        else:
            soup = bs(html, 'lxml')

            divs = soup.find_all('div', class_='product-thumb')
            with open('roboshop.txt', 'a') as file:
                for div in divs:
                    try:
                        caption = div.find('div', class_='caption')
                        name = caption.find('a').text
                        count = div.find('label', class_='quantity-info').text
                        count = count.strip()
                        count = count.split('В наличии:')[1]
                        print(f'{name} - {count}')
                        file.write(f'{name}:{count}'+'\n')


                    except:
                        count = 0
                        file.write(f'{name}:{count}'+'\n')
                        print(f'{name} - {count}')
    except:
        try:
            time.sleep(5)
            get_name_and_count_product(url)
        except:
            pass




def roboshop():
    links = get_links_product('https://roboshop.spb.ru')
    try:
        with open('roboshop.txt', 'w') as file:
            file.close()
    except:
        pass

    with Pool(20) as p:
        p.map(get_name_and_count_product, links)
        time.sleep(3)
        logger.debug('Category Acepted')

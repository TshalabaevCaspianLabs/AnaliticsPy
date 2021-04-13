import time
from multiprocessing import Pool

import requests
import xlwt
from bs4 import BeautifulSoup as bs
from loguru import logger


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


def get_all_link_product(html):
    soup = bs(html, 'lxml')
    all_links = []

    links = soup.find_all('h3', class_='cat')
    for link in links:
        a = link.find('a').get('href')
        all_links.append('https://www.rekshop.ru' + a)

    return all_links



def get_subproduct_links(url):
    html = get_html(url)

    if html == 0:
        logger.error('Not Connect Category')
        pass
    else:
        soup = bs(html, 'lxml')

        all_links_subproduct = []

        links = soup.find_all('h4', class_='subcat')
        for link in links:
            a = link.find('a').get('href')
            all_links_subproduct.append('https://www.rekshop.ru' + a + '?page=1&number=100')

        return all_links_subproduct


def get_name_and_count_product(url):
    try:
        html = get_html(url)
        if html == 0:
            logger.error('Not Connect Name and Count')
            pass
        else:
            soup = bs(html, 'lxml')
            divs = soup.find_all('table', class_='table_karkas_product_goods')

            with open('rekshop.txt', 'a') as file:
                for div in divs:
                    try:

                        div_a = div.find('div', class_='name_product_goods')
                        name = div_a.find('a').text

                        td = div.find('td', class_='td_amount_karkas_product_goods')
                        count = td.find('span', class_='product_amount_green').text
                        count = count.strip()
                        count = count.split(' ')[0]
                        file.write(f'{name}:{count}' + '\n')
                        print(f'{name} - {count}')

                    except:
                        name = div_a.find('a').text
                        count = 0
                        file.write(f'{name}:{count}' + '\n')
                        print(f'{name} - {count}')
    except Exception as e:
        pass
        logger.error(e)









def rekshop():
    html = get_html('https://www.rekshop.ru/')
    if html == 0:
        rekshop()

    else:
        links = get_all_link_product(html)
        try:
            with open('rekshop.txt', 'w') as file:
                file.close()
        except:
            pass


        with Pool(20) as p:
            for link in links:
                try:
                    all_links_product = get_subproduct_links(link)
                except:
                    all_links_product = get_subproduct_links(link)

                p.map(get_name_and_count_product, all_links_product)
                time.sleep(5)
                logger.debug('Category Acepted')






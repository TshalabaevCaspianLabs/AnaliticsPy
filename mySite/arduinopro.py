import time
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup as bs
from loguru import logger


#  получаем html код страницы
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


#  собираем ссылки на категории тавара
def get_category_links(url):
    html = get_html(url)
    if html == 0:
        logger.error('Not Connection category')
        pass

    else:
        soup = bs(html, 'lxml')
        all_category_links = []

        li_list = soup.find_all('li', class_='product-category')

        for li in li_list:
            a = li.find('a').get('href')
            all_category_links.append(a)

        return all_category_links


#  собираем ссылки на все страницы категории
def get_page_namber_links(url):
    all_links_pagination = []
    all_links_pagination.append(url)
    try:
        html = get_html(url)
        if html == 0:
            logger.error('Not connection page number')
            pass
        else:
            soup = bs(html, 'lxml')

            a_demo = []
            ul = soup.find('ul', class_='page-numbers')
            a_list = ul.find_all('a', class_='page-numbers')

            for a in a_list:
                text = a.get('href')
                a_demo.append(text)

            count_page = len(a_demo)

            for i in range(count_page - 1):
                all_links_pagination.append(a_demo[i])

            return all_links_pagination
    except:
        return all_links_pagination


#  Собираем ссылки на все продукты на старнице
def get_product_links(url):
    html = get_html(url)
    if html == 0:
        logger.error('Not connection products links')
        pass
    else:
        soup = bs(html, 'lxml')
        all_links_page_product = []

        a_list = soup.find_all('a', class_='woocommerce-loop-product__link')

        for a in a_list:
            all_links_page_product.append(f"{a.get('href')}")
        return all_links_page_product


#  Собираем Имя и колво продукта на сайте
def get_name_and_count_product(url):
    try:
        html = get_html(url)
        if html == 0:
            logger.error('Not connection name and count')
            pass
        else:
            soup = bs(html, 'lxml')
            with open('arduinopro.txt', 'a') as filename:
                try:
                    name = soup.find('h1', class_='product_title entry-title').text
                    count = soup.find('p', class_='stock in-stock').text
                    count = count.strip().split(' в наличии')[0]

                    filename.write(f'{name}:{count}' + '\n')

                    print(f'{name} - {count}')
                    time.sleep(3)
                except:
                    try:
                        name = soup.find('h1', class_='product_title entry-title').text
                        count = 0
                        filename.write(f'{name}:{count}' + '\n')

                        print(f'{name} - {count}')
                        time.sleep(3)
                    except:
                        pass
    except:
        pass


def arduinopro():
    categorys = get_category_links('https://arduinopro.ru/catalog/')

    try:
        with open('arduinopro.txt', 'w') as filename:
            filename.close()
    except Exception as e:
        pass

    with Pool(30) as p:
        for category in categorys:
            links = get_page_namber_links(category)

            for link in links:
                prodict_list = get_product_links(link)
                p.map(get_name_and_count_product, prodict_list)
                time.sleep(5)

            logger.debug('\n-- CATEGORY ACEPTEDIT-- \n')
            time.sleep(5)

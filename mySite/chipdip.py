import time
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup as bs
from loguru import logger


def get_html(url):
    try:
        proxies = {
            'http': 'http://Us649105:Us649105@ru2.mproxy.top:60210',
            'https': 'https://Us649105:Us649105@ru2.mproxy.top:60210'
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'}
        r = requests.get(url, headers=headers, proxies=proxies)
        if r.status_code == 200:
            return r.text
        else:
            logger.error('Not connect')
            return 0
    except:
        pass


def get_catcategory_links(url):
    html = get_html(url)
    if html == 0:
        logger.error('Not connection cat catalog')
        pass
    else:
        soup = bs(html, 'lxml')
        all_catcategory_links = []

        div = soup.find('div', id='catmenu')
        li_list = div.find_all('li')

        for li in li_list:
            a = li.find('a').get('href')
            all_catcategory_links.append('https://www.chipdip.ru' + a)
        return all_catcategory_links


def get_category_links(url):
    html = get_html(url)
    if html == 0:
        logger.error('Not connection category')
        pass
    else:
        soup = bs(html, 'lxml')
        all_links_category = []
        li_list = soup.find_all('li', class_='catalog__item')

        for li in li_list:
            a = li.find('a').get('href')
            all_links_category.append('https://www.chipdip.ru' + a + '?ps=x3')
        return all_links_category


def get_pagination_page_links(url):
    all_links_page = []
    all_links_page.append(url)
    try:
        html = get_html(url)
        if html == 0:
            logger.error('Not connection page pagination')
            pass
        else:
            soup = bs(html, 'lxml')
            page = soup.find('ul', class_='pager__pages')
            a_list = page.find_all('a', class_='link')

            for a in a_list:
                all_links_page.append('https://www.chipdip.ru' + a.get('href'))

            return all_links_page
    except:
        return all_links_page


def get_name_and_count_product(url):
    try:
        html = get_html(url)
        if html == 0:
            logger.error('Not connection name and count')
            pass
        else:
            soup = bs(html, 'lxml')
            divs = soup.find_all('tr', class_='with-hover')
            with open('chipdip.txt', 'a') as file:
                for div in divs:
                    try:
                        name = div.find('a', class_='link').text
                        count = div.find('span', class_='item__avail').text.strip()
                        count = count.split(' шт.')[0]
                        if count == 'По запросу':
                            count = 0
                        file.write(f'{name}:{count}' + '\n')
                        print(f'{name} - {count}')

                    except:
                        name = div.find('a', class_='link').text
                        count = 0
                        file.write(f'{name}:{count}' + '\n')
                        print(f'{name} - {count}')
    except:
        pass


def chipdip():
    links = get_catcategory_links('https://www.chipdip.ru')
    try:
        with open('chipdip.txt', 'w') as file:
            file.close()
    except:
        pass
    with Pool(40) as p:

        for link in links:
            categorys = get_category_links(link)
            logger.debug('Get Category')

            for number, category in enumerate(categorys):
                if number == 10:
                    p.close()
                    break

                else:
                    pages = get_pagination_page_links(category)
                    p.map(get_name_and_count_product, pages)
                    logger.debug('category accept')


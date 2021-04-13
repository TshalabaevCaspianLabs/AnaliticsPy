import requests
from bs4 import BeautifulSoup as bs
import time
from loguru import logger
from multiprocessing import Pool

def get_html(url):
    try:
        headers = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.text
        else:
            return 0
    except:
        pass


def get_page_pagination_links(url):
    all_links_page = []
    all_links_page.append(url)
    try:
        html = get_html(url)
        if html == 0:
            logger.error('Not connection page pagination')
            pass
        else:
            soup = bs(html, 'lxml')

            data_links = []
            div = soup.find('div', class_='nav-links')

            page_links = div.find_all('a', class_='page-numbers')

            for page in page_links:
                data_links.append(page.get('href'))

            count_page = len(data_links)

            for i in range(count_page-1):
                all_links_page.append(data_links[i])

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

            div_list = soup.find_all('div', class_='product-h')

            with open('voltiq.txt', 'a') as file:
                for div in div_list:
                    try:
                        name = div.find('h2', class_='woocommerce-loop-product__title').text
                        count = div.find('div', class_='woocommerce-stock-title').find('strong').text
                        file.write(f'{name}:{count}' + '\n')
                        print(f'{name} - {count}')
                    except:
                        name = div.find('h2', class_='woocommerce-loop-product__title').text
                        count = 0
                        file.write(f'{name}:{count}' + '\n')
                        print(f'{name} - {count}')
    except:
        try:
            time.sleep(5)
            get_name_and_count_product(url)
        except:
            pass




def voltiq():
    category_links = [
        'https://voltiq.ru/cat/new/',
        'https://voltiq.ru/cat/sale/',
        'https://voltiq.ru/cat/diy-packs/',
        'https://voltiq.ru/cat/3d-printer-components/mechanical-parts/',
        'https://voltiq.ru/cat/3d-printer-components/consumables/',
        'https://voltiq.ru/cat/3d-printer-components/extruders/',
        'https://voltiq.ru/cat/3d-printer-components/electronics/',
        'https://voltiq.ru/cat/devboards/arduino/',
        'https://voltiq.ru/cat/devboards/h-duino/',
        'https://voltiq.ru/cat/devboards/attiny-devboards/',
        'https://voltiq.ru/cat/devboards/esp8266-devboards/',
        'https://voltiq.ru/cat/devboards/phpoc/',
        'https://voltiq.ru/cat/devboards/kontrollery-pic/',
        'https://voltiq.ru/cat/devboards/pine64-devboards/',
        'https://voltiq.ru/cat/devboards/raspberry-pi-devboards/',
        'https://voltiq.ru/cat/devboards/stm-devdoards/',
        'https://voltiq.ru/cat/shields/arduino-shields/',
        'https://voltiq.ru/cat/shields/esp8266-shields/',
        'https://voltiq.ru/cat/shields/phpoc-shields/',
        'https://voltiq.ru/cat/shields/raspberry-pi-shields/',
        'https://voltiq.ru/cat/sensors/time-measurement/',
        'https://voltiq.ru/cat/sensors/measurement-of-gas/',
        'https://voltiq.ru/cat/sensors/measurement-environment/',
        'https://voltiq.ru/cat/sensors/orientation-measurement/',
        'https://voltiq.ru/cat/sensors/range-measurement/',
        'https://voltiq.ru/cat/sensors/current-measurement/',
        'https://voltiq.ru/cat/sensors/wired-network-modules/',
        'https://voltiq.ru/cat/sensors/wireless-network-modules/',
        'https://voltiq.ru/cat/relay/',
        'https://voltiq.ru/cat/sensors/adc-dac/',
        'https://voltiq.ru/cat/data-storage/',
        'https://voltiq.ru/cat/sensors/audio-modules/',
        'https://voltiq.ru/cat/powers/power-supplies/',
        'https://voltiq.ru/cat/powers/voltage-converters/',
        'https://voltiq.ru/cat/powers/surge-protectors/',
        'https://voltiq.ru/cat/powers/battery-charging-control/',
        'https://voltiq.ru/cat/powers/voltage-current-measurement/',
        'https://voltiq.ru/cat/powers/battery-modules/',
        'https://voltiq.ru/cat/mechanics/dc-motor/',
        'https://voltiq.ru/cat/mechanics/stepper-motors/',
        'https://voltiq.ru/cat/mechanics/motor-reducers/',
        'https://voltiq.ru/cat/mechanics/pumps/',
        'https://voltiq.ru/cat/mechanics/servos/',
        'https://voltiq.ru/cat/mechanics/motor-drivers/',
        'https://voltiq.ru/cat/indication/displays/',
        'https://voltiq.ru/cat/indication/oled-displays/',
        'https://voltiq.ru/cat/indication/symbol-displays/',
        'https://voltiq.ru/cat/indication/segment-indicators/',
        'https://voltiq.ru/cat/indication/led-matrix/',
        'https://voltiq.ru/cat/indication/leds/',
        'https://voltiq.ru/cat/programmators/',
        'https://voltiq.ru/cat/programmators/debuggers/',
        'https://voltiq.ru/cat/interface-converters/',
        'https://voltiq.ru/cat/commutation/buttons/',
        'https://voltiq.ru/cat/commutation/switches/',
        'https://voltiq.ru/cat/connectors/',
        'https://voltiq.ru/cat/smd-components/0402r/',
        'https://voltiq.ru/cat/smd-components/0603r/',
        'https://voltiq.ru/cat/smd-components/0805r/',
        'https://voltiq.ru/cat/smd-components/1206r/',
        'https://voltiq.ru/cat/smd-components/1206c/',
        'https://voltiq.ru/cat/radiocomponents/',
        'https://voltiq.ru/cat/breadboards/',
        'https://voltiq.ru/cat/cases/',
        'https://voltiq.ru/cat/instruments/',
        'https://voltiq.ru/cat/clamps/',
        'https://voltiq.ru/cat/cables/',
        'https://voltiq.ru/cat/cooling/',
        'https://voltiq.ru/cat/others/',
    ]

    try:
        with open('voltiq.txt', 'w') as file:
            file.close()
    except:
        pass

    with Pool(20) as p:
        for category in category_links:
            links = get_page_pagination_links(category)
            p.map(get_name_and_count_product, links)
            time.sleep(5)
            logger.debug('Category Acepted')
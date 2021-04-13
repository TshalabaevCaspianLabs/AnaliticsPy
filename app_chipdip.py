import time
from threading import *

from loguru import logger


from mySite.chipdip import chipdip
from generator_xls import read_first_exele_file, read_last_exele_file
from refactor_txt import update_exele


def first_exele_file(file):
    read_first_exele_file(file)


def new_exele_file(file):
    update_exele(file)


def chipdip_procces():
    time1 = time.time()
    try:
        chipdip()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('One accept')
    first_exele_file('chipdip')
    try:
        chipdip()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('Two accept')
    new_exele_file('chipdip')
    time.sleep(10)
    read_last_exele_file('chipdip')

    try:
        print(time.time() - time1)
    except:
        pass


if __name__ == '__main__':
    logger.debug('Start ChipDip')
    chipdip_procces()
import time
from threading import *

from loguru import logger

from generator_xls import read_first_exele_file
from mySite.arduinopro import arduinopro
from mySite.rekshop import rekshop
from mySite.roboshop import roboshop
from mySite.voltiq import voltiq
from refactor_txt import update_exele


def first_exele_file(file):
    read_first_exele_file(file)


def new_exele_file(file):
    update_exele(file)


def arduinopro_procces():
    try:
        arduinopro()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('One accept')
    first_exele_file('arduinopro')
    time.sleep(3600)
    while True:
        try:
            arduinopro()
        except Exception as e:
            logger.error(e)
            pass
        logger.debug('Two accept')
        new_exele_file('arduinopro')
        time.sleep(3600)


def rekshop_procces():
    try:
        rekshop()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('One accept')
    first_exele_file('rekshop')
    time.sleep(3600)
    while True:
        try:
            rekshop()
        except Exception as e:
            logger.error(e)
            pass
        logger.debug('Two accept')
        new_exele_file('rekshop')
        time.sleep(3600)


def roboshop_procces():
    try:
        roboshop()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('One accept')
    first_exele_file('roboshop')
    time.sleep(3600)
    while True:
        try:
            roboshop()
        except Exception as e:
            logger.error(e)
            pass
        logger.debug('Two accept')
        new_exele_file('roboshop')
        time.sleep(3600)

def voltiq_procces():
    try:
        voltiq()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('One accept')
    first_exele_file('voltiq')
    time.sleep(3600)
    while True:
        try:
            voltiq()
        except Exception as e:
            logger.error(e)
            pass
        logger.debug('Two accept')
        new_exele_file('voltiq')
        time.sleep(3600)



if __name__ == '__main__':
    time1 = time.time()
    logger.debug('Iteration Start')

    t1 = Thread(target=arduinopro_procces)
    t2 = Thread(target=rekshop_procces)
    t3 = Thread(target=roboshop_procces)
    t4 = Thread(target=voltiq_procces)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

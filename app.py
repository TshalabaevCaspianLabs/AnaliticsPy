import time
from threading import *
from multiprocessing import Process

from loguru import logger

from mySite.arduinopro import arduinopro
from mySite.chipdip import chipdip
from mySite.rekshop import rekshop
from mySite.roboshop import roboshop
from mySite.voltiq import voltiq
from generator_xls import read_first_exele_file, read_last_exele_file
from refactor_txt import update_exele

"""
$ ulimit -n 2048
"""


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
    try:
        arduinopro()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('Two accept')
    new_exele_file('arduinopro')
    time.sleep(10)
    read_last_exele_file('arduinopro')




def rekshop_procces():
    try:
        rekshop()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('One accept')
    first_exele_file('rekshop')
    try:
        rekshop()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('Two accept')
    new_exele_file('rekshop')
    time.sleep(10)
    read_last_exele_file('rekshop')


def roboshop_procces():
    try:
        roboshop()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('One accept')
    first_exele_file('roboshop')
    try:
        roboshop()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('Two accept')
    new_exele_file('roboshop')
    time.sleep(10)
    read_last_exele_file('roboshop')


def voltiq_procces():
    try:
        voltiq()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('One accept')
    first_exele_file('voltiq')
    try:
        voltiq()
    except Exception as e:
        logger.error(e)
        pass
    logger.debug('Two accept')
    new_exele_file('voltiq')
    time.sleep(10)
    read_last_exele_file('voltiq')


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
    time1 = time.time()
    logger.debug('Iteration Start')

    t1 = Thread(target=arduinopro_procces)
    t2 = Thread(target=rekshop_procces)
    t3 = Thread(target=roboshop_procces)
    t4 = Thread(target=voltiq_procces)
    t5 = Thread(target=chipdip_procces)

    t1.start()
    t2.start()
    t3.start()
    t4.start()



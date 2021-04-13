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



if __name__ == '__main__':
    logger.debug('Start Arduinopro')
    arduinopro_procces()
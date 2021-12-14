from datetime import datetime, timedelta
from time import sleep, time
from typing import List
from pconst import const as _
import servicemanager
import requests
import logging
from logging import config
from pathlib import Path, PurePath
from configparser import ConfigParser
import sys
import traceback
from threading import Thread, Event
from hashlib import md5
from xml.etree import ElementTree as ET
import hpilo
from Service import ServiceBase
from Database import SQLiteDB


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] - %(message)s')


def humman_format(equipment, state, start_time, reason=None, comp=None, isHandled=False):
    message = 'No data'
    if isHandled is False:
        message = (
            f'熱軋加熱爐{comp}發生異常\n'
            f'⁕設備名稱: {equipment}\n'
            f'⁕目前狀態: {state}\n'
            f'⁕原因: {reason}\n'
            f'⁕發生時間: {start_time}'
        )
    else:
        message = (
            f'熱軋加熱爐{comp}已復原\n'
            f'⁕設備名稱: {equipment}\n'
            f'⁕目前狀態: {state}\n'
            f'⁕復原時間: {start_time}'
        )
    return message


token = '20yBTkYFBYUjp2OSxQI57KuLbuF4LEQd0jYGx2Wkkyy'
url = 'http://10.199.15.109:8080/api/line/notify.php'
inMsg = humman_format(f'溫度感應器03-CPU', 'Error', datetime.now(), comp='SERVER', isHandled=True)
data = {'token': token, 'message': inMsg}
response = requests.post(url=url, data=data)
logging.info(response.status_code)

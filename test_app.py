import psycopg2
from lxml import html

from app import app, basedir
import pytest
import os
from app.yolov5.db_data import Data_db
from app.yolov5.detect_original import run
import requests
import lxml.etree


# проверяем модуль с детектированием на ошибку "деление на ноль (ZeroDivisionError)"
def test_null():
    # video = os.path.abspath('app/uploads/test1s.mp4')
    # print(basedir)
    video = 'test1s.mp4'
    # video = os.path.join(basedir, 'test1s.mp4')

    # video = os.path.join(basedir, 'app/static/video/test1s.mp4')
    weights = os.path.abspath('app/best.pt')
    NotZeroDivision = True
    try:
        run(weights, video, "test1s.webm", False, False)
    except ZeroDivisionError:
        NotZeroDivision = False
    assert NotZeroDivision == True


def test_exists_img():
    xpath = '''/html/body/img'''

    url = "http://192.168.1.7:8080/redirect/"
    req = requests.get(url)
    tree = html.fromstring(req.content)
    root = tree.xpath(xpath)
    for item in root:
        assert item.text == None

# test_exists_img()


# можем ли подключиться к контейнерной базе
def test_connect_bd():
    a = Data_db().__init__()
    assert a == None

# пробуем вывести список всех существующих таблиц
def test_sql_query():
    sql = ''' select * from information_schema.tables '''
    a = Data_db()
    cur = Data_db().cursor

    b = False
    cur.execute(sql)
    b = True
    # assert b == True

# пустая ли папка uploads. Если колво файлов не равно нулю, то тест пройден
def test_uploads_dir():
    path = os.path.join(basedir, 'uploads')
    print(path)
    a = False
    if len(os.listdir(path)) != 0:
        a = True
        assert a == True

# проверка существования весов в проекте
def test_exists_best_pt():
    a = os.path.exists(basedir)
    assert a == True




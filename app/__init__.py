import os
from flask_dropzone import Dropzone
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__)) # находим корневую папку для запуска проекта.

WEIGHTS = "best.pt"


app = Flask(__name__)
app.config["UPLOADED_PATH"] = os.path.join(basedir, 'uploads') #конфигурируем загрузочный путь
app.config["DROPZONE_MAX_FILE_SIZE"] = 256
app.config["DROPZONE_TIMEOUT"] = 5 * 60 * 1000 # то время через которое вылетит ошибка, если что-то пошло не так
app.config["WEIGHTS_PATH"] = os.path.join(basedir, WEIGHTS) #конфигурируем путь к весам
dropzone: Dropzone = Dropzone(app) #создаем объект класса фласк-дропзон





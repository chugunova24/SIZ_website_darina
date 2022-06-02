import os
import pathlib
import uuid

from app import app
from flask import render_template, request
from app.yolov5.detect_original import run
from threading import Thread

last_image=None


@app.route('/', methods=['GET', 'POST'])
def upload():
    global last_image
    if request.method == 'POST':
        f = request.files.get('file') #получает файл
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename)) #получаем полный путь до загруженного файла и сохраняем его по этому пути
        run(app.config["WEIGHTS_PATH"], f.filename, Fals, True)#вызов запирающей функции детекции
        last_image = f.filename #Сохраняем имя последнего изображения
    return render_template('index.html') # если метод GET, то отрисовываем страницу index


@app.route("/redirect/", methods=["GET", "POST"] )
def redirect():
    if not last_image: 
        return "Нет результата"
    else:
        return render_template('show.html', image=last_image,show_img=True) #указываем путь к изображению которое хотим показать

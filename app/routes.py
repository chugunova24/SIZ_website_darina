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
        # f = request.files.get('file')
        # f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        # #Thread(target=run, args=('best.pt', f.filename,True)).start()
        # detected_object, time_to_detect, im_path = run("best.pt", f.filename, True)
        # last_image=f.filename

        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))

        basedir = os.path.abspath(os.path.dirname(__file__))
        print(basedir)
        #path_to_pt=basedir+''
        # Получаем строку, содержащую путь к рабочей директории:
        dir_path = pathlib.Path.cwd()

        # Объединяем полученную строку с недостающими частями пути
        path = pathlib.Path(dir_path, 'app', 'best.pt')
        print('ПУТЬ',path)
        # Thread(target=run, args=('nebest.pt', f.filename,True)).start()
        detected_object = run(path, f.filename, True, True)
        last_image = f.filename
        # f = request.files.get('file')
        # file_ext = f.filename[f.filename.rfind('.'):]
        # new_filename = uuid.uuid1().hex + file_ext
        # Last_video = new_filename
        # # if WINDOWS:
        # #     new_filename_path = f"{app.config['UPLOADED_PATH']}\\{new_filename}"
        # # else:
        # new_filename_path = f"{app.config['UPLOADED_PATH']}/{new_filename}"
        # f.save(os.path.join(app.config['UPLOADED_PATH'], new_filename))
        # app.config["WEIGHTS_PATH"]
        # detect = Thread(target=run, args=(app.config["WEIGHTS_PATH"], new_filename_path, new_filename, False, False))
        # detect.start()
        # detect.join()
    return render_template('index.html')


@app.route("/redirect/", methods=["GET", "POST"] )
def redirect():
    if not last_image: 
        return "Нет результата"
    else:
        return render_template('show.html', image=last_image,show_img=True)
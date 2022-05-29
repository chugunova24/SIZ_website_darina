import os

from app import app
from flask import render_template, request
from app.yolov5.detect_original import run

last_image=None


@app.route('/', methods=['GET', 'POST'])
def upload():
    global last_image
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        #Thread(target=run, args=('nebest.pt', f.filename,True)).start()
        detected_object, time_to_detect, im_path = run("nebest.pt", f.filename, True)
        last_image=f.filename   
    return render_template('index.html')


@app.route("/redirect/",methods=["GET", "POST"] )
def redirect():
    if not last_image: 
        return "Нет результата"
    return render_template('show.html', image=last_image,show_img=True)
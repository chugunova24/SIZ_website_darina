import os
from flask_dropzone import Dropzone
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

WEIGHTS = "best.pt"


app = Flask(__name__)
# app.config.update(
#     # UPLOADED_PATH=os.path.join(basedir, 'uploads'),
#     UPLOADED_PATH=os.path.join(basedir, 'uploads'))
app.config["UPLOADED_PATH"] = os.path.join(basedir, 'uploads')
app.config["DROPZONE_MAX_FILE_SIZE"] = 256
app.config["DROPZONE_TIMEOUT"] = 5 * 60 * 1000
app.config["WEIGHTS_PATH"] = os.path.join(basedir, WEIGHTS)
# print(app.config)
dropzone: Dropzone = Dropzone(app)


# if __name__ == "__main__":
#     app.run()



import  flask
from flask import Flask, request, jsonify, make_response, redirect
from pathlib import Path
import os
# from werkzeug import redirect
from flask.helpers import send_file, url_for
app = Flask(__name__)
@app.route("/")
def home():
    return redirect(url_for('static', filename='index.html'))


@app.route("/process",methods=["POST","GET"])
def handle_image():
    if request.method=='GET':
        return redirect(url_for('static', filename='predict.html'))

    uploaded_file = request.files['file']
    location = 'upload'
    if (location.endswith('/') == False):
        location += "/"
    if (os.path.exists(location) == False):
        Path(location).mkdir(parents=True, exist_ok=True)
    path_name = location + uploaded_file.filename
    uploaded_file.save(path_name)
    #do some stuff here
    return send_file(path_name,mimetype="image/gid")

if __name__ == '__main__':
    app.run()
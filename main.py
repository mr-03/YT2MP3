from flask import Flask, redirect, url_for, render_template, request, Response, send_file
import youtube
from threading import Thread
import os
from os import path
import time
import shutil

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        
        yt_url = request.form['yturl']
        filename = youtube.get_filename(yt_url)
        filename = str(filename).replace("tmp\\", "")
        filename = filename.replace(".webm", "")
        filename = filename + ".mp3"
        
        youtube.download_mp3(yt_url)
        
        filepath = f"tmp/{filename}"
        return send_file(filepath, as_attachment=True)
    else:
        try:
            shutil.rmtree('tmp') 
        except:
            pass
        try:
            os.mkdir('tmp')
        except:
            pass
        
        return render_template("index.html")

if __name__ == "__main__":
    app.run()
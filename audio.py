from flask import Flask
from flask import request, redirect,url_for
from flask import render_template
import os
import speech

app = Flask(__name__)




@app.route("/", methods=['POST', 'GET'])
def index():
    text=""
    if request.method == "POST":
        files=request.files['audio_data']
        files.save('file.wav')
        text = speech.func()
        if(text=="e"):
            return render_template("index.html",text="Upload a clear audio file")
        return render_template("trans.html",text=text)
    return render_template("index.html",text=text)


if __name__ == "__main__":
    app.run(threaded=Tree, port= 5000)
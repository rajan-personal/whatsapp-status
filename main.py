import io
import os
from PIL import Image, ImageDraw
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post", methods=['POST'])
def post():
    # get data from form
    name = request.form.get('name')
    card = request.form.get('template')
    logo = request.files.get('upload-image')
    print(name, card, logo)
    image = Image.open('templates/' + card + '.jpg')
    image = image.resize((400, 250))
    logo = Image.open(logo)
    logo = logo.resize((180, 180))
    image.paste(logo, (50, 30))
    I1 = ImageDraw.Draw(image)
    I1.text((270, 76), name, fill=(0, 0, 0), align="center")
    image.save('static/' + 'image_with_logo' + '.jpg')
    image = os.path.join('static', 'image_with_logo.jpg')
    return render_template('result.html', image=image)


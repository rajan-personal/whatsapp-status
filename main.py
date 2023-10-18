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
    form_data = request.get_json()
    name = form_data['name']
    card = form_data['card']
    logo = form_data['logo']
    print(name, card, logo)
    # image = Image.open('templates/' + card + '.jpg')
    # logo = Image.open('logo/' + logo + '.jpeg')
    # logo = logo.resize((80, 80))  # Resize to 80x80 pixels
    # image.paste(logo, (50, 50))  # Paste the logo at the top left corner
    # I1 = ImageDraw.Draw(image)
    # I1.text((58, 136), name, fill=(0, 0, 0))
    # image.save('static/' + 'image_with_logo' + '.jpg')
    image = os.path.join('static', 'image_with_logo.jpg')
    return render_template('result.html', image=image)

@app.route("/get", methods=['GET'])
def get():
    image = os.path.join('static', 'image_with_logo.jpg')
    return render_template('result.html', image=image)


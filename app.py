import argparse
from http.client import HTTPException, HTTPResponse
from flask import Flask, request
from flask import send_file, abort, render_template
import os
from flask_cors import CORS, cross_origin
from detection import ImageDetection
import logging
import yaml
import cv2
from PIL import Image
import numpy as np
from image_processor import ImageProcessor



yamlFile = yaml.load(open("config\config.yaml"), Loader=yaml.FullLoader)
logging.basicConfig(filename='app_logger/main/main_logs.txt',
                    filemode='a', level=logging.INFO,
                    format='%(asctime)s: %(levelname)s:: %(message)s')


app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index_page():
    try:
        return render_template("index.html")
    except Exception as e:
        logging.error("index file error", str(e))

@app.route('/training', methods=['GET', 'POST'])
@cross_origin()
def train():
    pass

@app.route('/detectObject', methods=['GET', 'POST'])
@cross_origin()
def detectObject():
    try:
        if request.method == 'POST':
            img = request.files['inputImg']
            print(img.filename, type(img))
            image = Image.open(img)
            image = np.array(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (480, 480))
            # img.save(os.path.join("temp_data", img.filename))

            processor = ImageProcessor(yamlFile, image)

            return "Uploaded Successfully"

    except Exception as e:
        logging.error("Error occured while training", e)
        return "Upload Failed"

@app.route('/download', methods=['GET', 'POST'])
@cross_origin()
def downloadPage():
    pass


if(__name__) == '__main__':
    app.run(port=5000, debug=True)
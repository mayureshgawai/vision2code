import argparse
from http.client import HTTPException, HTTPResponse
from flask import Flask, request
from flask import send_file, abort, render_template
import os
from flask_cors import CORS, cross_origin
from predictor_function import ImagePredictor
import logging
import yaml
import cv2
from PIL import Image
import numpy as np

# class vision:
#
#     def __int__(self):
#         predictor = imagePredictor()
# yamlFile = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)
logging.basicConfig(filename='logs/main/main_logs.txt',
                    filemode='a', level=logging.INFO,
                    format='%(asctime)s: %(levelname)s:: %(message)s')


app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index_page():
    return render_template("index.html")

@app.route('/training', methods=['GET', 'POST'])
@cross_origin()
def train():
    pass

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    try:
        img = request.files['inputImg']
        print(img.filename, type(img))
        image = Image.open(img)
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img.save(os.path.join("temp_data", img.filename))

        predictor = ImagePredictor()
        return "Uploaded Successfully"

    except Exception as e:
        # logging.error("Error occured while training", e)
        print(e)
        return "Upload Failed"

if(__name__) == '__main__':
    app.run(port=5000, debug=True)
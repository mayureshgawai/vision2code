import argparse
from flask import Flask, request
from flask import send_file, abort, render_template
import os
from flask_cors import CORS, cross_origin
from predictor_function import imagePredictor

import yaml


class vision:

    def __int__(self):
        predictor = imagePredictor()




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index_page():
    pass

@app.route('/training', methods=['GET', 'POST'])
@cross_origin()
def train():
    pass

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def perdict():
    try:
        pass
    except Exception as e:
        print(e)
import logging
from detection import ImageDetection
import numpy as np
from app_logger.logger import logging
from app_exception import AppException
import sys
from html_process import CreateAlignment

ROWS = [[], [], [], []]

class ImageProcessor:
    def __init__(self, yamlFile, image):
        self.image = image
        self.yamlFile = yamlFile
        self.detection = ImageDetection(self.image, self.yamlFile)
        self.htmlprocess = CreateAlignment(yamlFile)
        logging.basicConfig(filename='app_logger/main/main_logs.txt',
                            filemode='a', level=logging.INFO,
                            format='%(asctime)s: %(levelname)s:: %(message)s')


    def process(self):

        '''
            To process the image through all the required detections and HTML file creations.
            params:
            return:
        '''
        try:
            # To get the all detections and the labels to pass in the HTML parsing methods.
            # Configurations for the detections are there in config file.
            box, labels = self.detection.detection()

            box = np.array(box.to("cpu"))

            # Before processing on boxes, we have to convert them all from tensors into numpy arrays.
            boxes = []
            for b in box:
                boxes.append(np.array(b.to("cpu")))

            # Now we can move to the phase of HTML creation.


        except Exception as e:
            raise AppException(e, sys)






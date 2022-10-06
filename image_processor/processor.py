import logging
from detection import ImageDetection
from detection import TextDetection
import numpy as np
from app_logger.logger import logging
from app_exception import AppException
import sys
from html_process import CreateAlignment
from html_process import TextAlignment

ROWS = [[], [], [], []]

class ImageProcessor:
    def __init__(self, yamlFile, image):
        self.image = image
        self.yamlFile = yamlFile
        self.detection = ImageDetection(self.image, self.yamlFile)
        self.textDetect = TextDetection(self.image, self.yamlFile)
        self.htmlprocess = CreateAlignment(yamlFile)
        self.textprocess = TextAlignment(yamlFile)
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
            logging.info("Text Detection and conversion stage begins here")

            box_text, labels_text = self.textDetect.detection()
            box = np.array(box.to("cpu"))

            boxes_text = []
            for b in box:
                boxes_text.append(np.array(b.to("cpu")))

            boxes_text = self.textprocess.checkForTextBboxesWithHTML(boxes_text,  boxes)
            boxes_text = self.textprocess.checkForTextBBoxes(boxes_text)

            logging.info("Text Detection and conversion stage completed")


            # Now we can move to the phase of HTML creation.
            # First we divide the elements row and columns wise.
            logging.info("HTML creation stage begins here")
            rows = self.htmlprocess.getRowsAndColumns(boxes, labels, ROWS, self.image)
            # generate(list, numpy.array()) method will create the html string list for us which we will further be
            # converted into code.
            self.html.generate(rows, self.image)
            logging.info("HTML creation stage completed and saved the code")

        except Exception as e:
            raise AppException(e, sys)






import logging
import cv2
import detectron2
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
import matplotlib.pyplot as plt
import os, json, random
from detectron2 import model_zoo
from detectron2.utils.visualizer import ColorMode
import numpy as np


class ImageDetection :

    def __init__(self, image, yamlFile):
        self.image = image
        self.yaml = yamlFile
        logging.basicConfig(filename='logs/main/main_logs.txt',
                            filemode='a', level=logging.INFO,
                            format='%(asctime)s: %(levelname)s:: %(message)s')

    def detection(self):
        try:
            # Configurations
            cfg = get_cfg()
            cfg.merge_from_file(model_zoo.get_config_file(self.yaml['detection_config']['config_file']))
            cfg.MODEL.ROI_HEADS.NUM_CLASSES = self.yaml['detection_config']['num_classes']
            cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = self.yaml['detection_config']['  score_thresh_test']
            cfg.MODEL.WEIGHTS = os.path.join("output2", "model_final.pth")
            predictor = DefaultPredictor(cfg)

            output = predictor(self.image)
            boxes = output["instances"].pred_boxes
            labels = np.array(output["instances"].pred_classes.to("cpu"))+1

        except Exception as e:
            logging.error("Error in detection method ", e)
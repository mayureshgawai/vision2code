import logging
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
import os
from detectron2 import model_zoo
import numpy as np
import boto3

class ImageDetection :

    def __init__(self, image, yamlFile):
        self.image = image
        self.yaml = yamlFile
        logging.basicConfig(filename='app_logger/main/main_logs.txt',
                            filemode='a', level=logging.INFO,
                            format='%(asctime)s: %(levelname)s:: %(message)s')

    def detection(self):
        try:
            # Configurations
            cfg = get_cfg()
            cfg.MODEL.DEVICE = "cpu"
            cfg.merge_from_file(model_zoo.get_config_file(self.yaml['detection_config']['config_file']))
            cfg.MODEL.ROI_HEADS.NUM_CLASSES = self.yaml['detection_config']['num_classes']
            cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = self.yaml['detection_config']['score_thresh_test']
            # cfg.MODEL.WEIGHTS = os.path.join(self.yaml['detection_config']['model_folder'],
            #                                  self.yaml['detection_config']['model_name'])

            drcty = os.getcwd()
            path = os.path.join(drcty, "output")

            cfg.MODEL.DEVICE = "cpu"

            modelCheck = os.listdir(path)
            print(modelCheck)
            if(self.yaml['detection_config']['model_name'] not in modelCheck):
                print("downloading od model using boto3")
                s3 = boto3.client('s3')
                s3.download_file("dt2odmodel", 'model_final.pth', path + "model_final_od.pth")

            cfg.MODEL.WEIGHTS = os.path.join(self.yaml['detection_config']['model_folder'],
                                             self.yaml['detection_config']['model_name'])


            # predictions for objects
            predictor = DefaultPredictor(cfg)

            output = predictor(self.image)
            boxes = output["instances"].pred_boxes
            labels = np.array(output["instances"].pred_classes.to("cpu"))+1


            logging.info("Boxes:")
            logging.info(boxes)
            logging.info("Labels:")
            logging.info(labels)

            return boxes, labels

        except Exception as e:
            logging.error("Error in detection method ", e)
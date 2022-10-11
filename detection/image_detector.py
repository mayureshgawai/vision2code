import logging
import cv2
import detectron2
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
import os, json, random
from detectron2 import model_zoo
from detectron2.utils.visualizer import ColorMode
import numpy as np


from detectron2.data import MetadataCatalog
from detectron2.data.datasets import register_coco_instances
from detectron2.utils.visualizer import ColorMode
from detectron2.utils.visualizer import Visualizer

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
            cfg.merge_from_file(model_zoo.get_config_file(self.yaml['detection_config']['config_file']))
            cfg.MODEL.ROI_HEADS.NUM_CLASSES = self.yaml['detection_config']['num_classes']
            cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = self.yaml['detection_config']['score_thresh_test']
            cfg.MODEL.WEIGHTS = os.path.join(self.yaml['detection_config']['model_folder'],
                                             self.yaml['detection_config']['model_name'])

            # predictions for objects
            predictor = DefaultPredictor(cfg)

            output = predictor(self.image)
            boxes = output["instances"].pred_boxes
            labels = np.array(output["instances"].pred_classes.to("cpu"))+1


            # register_coco_instances("sketches_test", {}, "data/test/_annotations.coco.json", "data/test")
            # test_metadata = MetadataCatalog.get("sketches_test")
            # output = predictor(self.image)
            # v = Visualizer(self.image, test_metadata, scale=1.2, instance_mode=ColorMode.IMAGE_BW)
            # out = v.draw_instance_predictions(output["instances"].to("cpu"))
            # cv2.imwrite("save1.jpg", out.get_image())



            return boxes, labels

        except Exception as e:
            logging.error("Error in detection method ", e)
import logging
import detectron2
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.utils.visualizer import ColorMode
import numpy as np
import sys
from app_exception import AppException

class TextDetection:
    def __init__(self, image, yamlFile):
        self.image = image
        self.yamlFile = yamlFile
        logging.basicConfig(filename='app_logger/main/main_logs.txt',
                            filemode='a', level=logging.INFO,
                            format='%(asctime)s: %(levelname)s:: %(message)s')



    def detection(self):

        try:
            cfg = get_cfg()
            cfg.merge_from_file(model_zoo.get_config_file(self.yamlFile['text_detection']['config_file']))
            cfg.MODEL.ROI_HEADS.NUM_CLASSES = self.yamlFile['text_detection']['num_classes']
            cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = self.yamlFile['text_detection']['score_thresh_test']
            # cfg.SOLVER.BASE_LR = self.yamlFile['text_detection']['base_lr']
            # cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 32

            predictor = DefaultPredictor(cfg)

            output = predictor(self.image)
            boxes = output["instances"].pred_boxes
            labels = np.array(output["instances"].pred_classes.to("cpu"))+1

        except Exception as e:
            raise AppException(e, sys)
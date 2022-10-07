import logging
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.engine import default_argument_parser
from detectron2 import model_zoo
from detectron2.engine import default_setup
import numpy as np
import os
import sys
from app_exception import AppException


import cv2
from detectron2.utils.visualizer import ColorMode
from detectron2.utils.visualizer import Visualizer
from detectron2.data.datasets import register_coco_instances
from detectron2.data import MetadataCatalog, DatasetCatalog
import matplotlib.pyplot as plt



class TextDetection:
    def __init__(self, image, yamlFile):
        self.image = image
        self.yamlFile = yamlFile
        logging.basicConfig(filename='app_logger/main/main_logs.txt',
                            filemode='a', level=logging.INFO,
                            format='%(asctime)s: %(levelname)s:: %(message)s')



    def detection(self):

        try:
            parser = default_argument_parser()
            args = parser.parse_args(str("--config-file "+self.yamlFile['text_detection']['config_file']+
                                     " MODEL.WEIGHTS "+ os.path.join(
                                        self.yamlFile['text_detection']['model_folder'],
                                        self.yamlFile['text_detection']['model_name']
                                    )).split())

            cfg = self.setup_cfg(args)

            predictor = DefaultPredictor(cfg)

            output = predictor(self.image)
            boxes = output["instances"].pred_boxes
            labels = np.array(output["instances"].pred_classes.to("cpu"))+1


            # register_coco_instances("sketches_test", {}, "data/test/_annotations.coco.json", "data/test")
            # test_metadata = MetadataCatalog.get("sketches_test")
            # v = Visualizer(self.image, test_metadata, scale=1.2, instance_mode=ColorMode.IMAGE_BW)
            # out = v.draw_instance_predictions(output["instances"].to("cpu"))
            # plt.figure(figsize=(20, 20))
            # cv2.imwrite("save1.jpg", out.get_image())
            # plt.imshow(out.get_image())


            return boxes, labels

        except Exception as e:
            raise AppException(e, sys)

    def setup_cfg(self, args):
        """
        Create configs and perform basic setups.
        """
        cfg = get_cfg()
        con = args.config_file
        cfg.merge_from_file(args.config_file)
        cfg.merge_from_list(args.opts)
        cfg.freeze()
        default_setup(cfg, args)
        return cfg

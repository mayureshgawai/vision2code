import logging


class ImageDetection:

    def __init__(self, image):
        self.image = image
        # self.yaml = yamlFile
        logging.basicConfig(filename='logs/main/main_logs.txt',
                            filemode='a', level=logging.INFO,
                            format='%(asctime)s: %(levelname)s:: %(message)s')

    def detectionPipeline(self):
        pass

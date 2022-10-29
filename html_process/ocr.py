from mmocr.utils.ocr import MMOCR
from app_logger.logger import logging

LEFT_PADDING = 50
RIGHT_PADDING = 50
TOP_PADDING = 50
BOTTOM_PADDING = 50

class ApplyOCR:

    '''
        This class is responsible to provide the function to perform Optical Character Recognition.
    '''

    def __init__(self, yamlFile, image):
        self.yamlFile = yamlFile
        self.image = image



    def getOCRText(self, box):

        '''
            This method uses MMOCR to perform ocr on the image text.
            param: list
            return: str
        '''

        try:
            logging.info("Getting OCR in progress...")
            img = self.image[box[1]:box[3], box[0]:box[2]]

            ocr = MMOCR(det=self.yamlFile['ocr']['detection'], recog=self.yamlFile['ocr']['recognition']
                        , config_dir=self.yamlFile['ocr']['config_dir'])

            result = ocr.readtext(img, print_result=True)
            text = ""

            for results in result[0]['text']:
                text += str(results) + " "

            logging.info("Characters recognized successfully!")
            return text

        except Exception as e:
            logging.error("Error occurred while getting OCR text! ", e)



    # def addThreshold(self, img, threshold):
    #     return cv2.adaptiveThreshold(img, 255, threshold, cv2.THRESH_BINARY, 11, 2)
    #
    # def applyPadding(self, img):
    #
    #     result = cv2.copyMakeBorder(img, TOP_PADDING, BOTTOM_PADDING, LEFT_PADDING, RIGHT_PADDING,
    #                                 cv2.BORDER_CONSTANT, None, [0, 0, 0])
    #     return result


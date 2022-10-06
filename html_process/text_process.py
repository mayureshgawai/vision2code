
import sys
from app_logger.logger import logging
from app_exception import AppException
from utils import AppUtils
class TextAlignment:
    def __init__(self, yamlFile):
        self.yaml = yamlFile
        self.util = AppUtils()

    def checkForTextBboxesWithHTML(self, boxes, labels, htmlBoxes):

        '''
            Purpose of this method is to check the overlapping of the text detection bboxes with html elements.
            If the overlapping is above specified limit then form the new bbox using their coordinates.
            Conditions we have to check:
                1. Other at bottom right
                2. Other at top right
                3. Other at top left
                4. Other at bottom left
                5. Other at exact right
                6. Other at exact left
                7. Other at exact bottom
                8. Other at exact top
                9. In the middle
            param: boxes, labels
            return: list
        '''


        try:
            logging.info("Checking for text bboxes...")

            for t in boxes:
                for h in htmlBoxes:

                    # check for bottom right
                    if(t[1] < h[3] and t[1] > h[1] and t[0] < h[2] and t[2] > h[2] and t[2] > h[2]):
                        points = [t[3], h[1], h[3], t[1], t[2], h[0], h[2], t[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)

                    # check for top right
                    elif(t[1] < h[1] and (h[3] > t[3] > h[1]) and (h[0] < t[0] < h[2]) and t[3] > h[3]):
                        points = [h[3], t[1], t[3], h[1], t[2], h[0], h[2], t[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)

                    # check for top left
                    elif(t[1] < h[1] and (h[3] > t[3] > h[1]) and (h[0] < t[2] < h[2]) and t[0] < h[0]):
                        points = [h[3], t[1], t[3], h[1], h[2], t[0], t[2], h[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)

                    # check for bottom left
                    elif((h[0] < t[1] < h[3]) and t[3] > h[3] and t[0] < h[0] and (h[0] < t[2] < h[2])):
                        points = [t[3], h[1], h[3], t[1], h[2], t[0], t[2], h[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)

                    # check for exact right
                    elif((h[1] < t[1] < h[3]) and (h[1] < t[3] < h[3]) and (h[0] < t[0] < h[2]) and t[2] > h[2]):
                        points = [t[2], h[0], h[2], t[0]]
                        horizontalDistance = self.util.getDistance(points, True)

                    # check for exact left
                    elif(t[0] < h[0] and (h[0] < t[2] < h[2]) and (h[1] < t[1] < h[3]) and (h[1] < t[3] < h[3])
                        and (h[1] < t[3] < h[3])):

                        points = [h[2], t[0], t[2], h[0]]
                        horizontalDistance = self.util.getDistance(points, True)

                    # check for exact bottom
                    elif((h[0] < t[0] < h[2]) and (h[0] < t[2] < h[2]) and (h[1] < t[1] < h[3]) and h[3] < t[3]):
                        points = [t[3], h[1], h[3], t[1]]
                        verticalDistance = self.util.getDistance(points, True)

                    # check for exact top
                    elif(t[1] < h[1] and (h[1] < t[3] < h[3]) and (h[0] < t[0] < h[2]) and (h[0] < t[2] < h[2])):
                        points = [h[3], t[1], t[3], h[1]]
                        verticalDistance = self.util.getDistance(points, True)

                    # check in the middle
                    elif((h[0] < t[0] < h[2]) and (h[0] < t[2] < h[2]) and (h[1] < t[1] < h[3]) and (h[1] < t[3] < h[3])):
                        pass


        except Exception as e:
            logging.error("Error occurred while checking for text bboxes. ", e)

import sys
from app_logger.logger import logging
from app_exception import AppException
from utils import AppUtils
import numpy as np

class TextAlignment:
    def __init__(self, yamlFile):
        self.yaml = yamlFile
        self.util = AppUtils()

    def checkForTextBboxesWithHTML(self, boxes, htmlBoxes):

        '''
            Purpose of this method is to check the overlapping of the text detection bboxes with html elements.
            If the overlapping is above of specified limit then we simply delete that text detection box.
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
            param: boxes, labels, htmlboxes
            return: list
        '''


        try:
            logging.info("Checking for text bboxes with HTML bboxes...")

            for t in boxes:
                for h in htmlBoxes:

                    # check for bottom right
                    if(t[1] < h[3] and t[1] > h[1] and t[0] < h[2] and t[2] > h[2] and t[2] > h[2]):
                        points = [t[3], h[1], h[3], t[1], t[2], h[0], h[2], t[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                        if(verticalDistance >= 75):
                            if(horizontalDistance >= 70):
                                # newOne = [h[0], h[1], t[2], t[3]]
                                # newBoxes.append(np.array(newOne, np.uint8))
                                boxes.remove(t)

                    # check for top right
                    elif(t[1] < h[1] and (h[3] > t[3] > h[1]) and (h[0] < t[0] < h[2]) and t[3] > h[3]):
                        points = [h[3], t[1], t[3], h[1], t[2], h[0], h[2], t[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                        if(verticalDistance >= 75):
                            if(horizontalDistance >= 70):
                                # newOne = [h[0], t[1], t[2], h[3]]
                                # newBoxes.append(np.array(newOne, np.uint8))
                                boxes.remove(t)

                    # check for top left
                    elif(t[1] < h[1] and (h[3] > t[3] > h[1]) and (h[0] < t[2] < h[2]) and t[0] < h[0]):
                        points = [h[3], t[1], t[3], h[1], h[2], t[0], t[2], h[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                        if (verticalDistance >= 75):
                            if (horizontalDistance >= 70):
                                # newOne = [t[0], t[1], h[2], h[3]]
                                # newBoxes.append(np.array(newOne, np.uint8))
                                boxes.remove(t)

                    # check for bottom left
                    elif((h[0] < t[1] < h[3]) and t[3] > h[3] and t[0] < h[0] and (h[0] < t[2] < h[2])):
                        points = [t[3], h[1], h[3], t[1], h[2], t[0], t[2], h[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                        if (verticalDistance >= 75):
                            if (horizontalDistance >= 70):
                                # newOne = [t[0], h[1], t[2], h[3]]
                                # newBoxes.append(np.array(newOne, np.uint8))
                                boxes.remove(t)

                    # check for exact right
                    elif((h[1] < t[1] < h[3]) and (h[1] < t[3] < h[3]) and (h[0] < t[0] < h[2]) and t[2] > h[2]):
                        points = [t[2], h[0], h[2], t[0]]
                        horizontalDistance = self.util.getDistance(points, True)
                        if(horizontalDistance >= 70):
                            # newOne = [h[0], h[1], t[2], h[3]]
                            # newBoxes.append(np.array(newOne, np.uint8))
                            boxes.remove(t)

                    # check for exact left
                    elif(t[0] < h[0] and (h[0] < t[2] < h[2]) and (h[1] < t[1] < h[3]) and (h[1] < t[3] < h[3])
                        and (h[1] < t[3] < h[3])):

                        points = [h[2], t[0], t[2], h[0]]
                        horizontalDistance = self.util.getDistance(points, True)
                        if (horizontalDistance >= 70):
                            # newOne = [t[0], h[1], h[2], h[3]]
                            # newBoxes.append(np.array(newOne, np.uint8))
                            boxes.remove(t)

                    # check for exact bottom
                    elif((h[0] < t[0] < h[2]) and (h[0] < t[2] < h[2]) and (h[1] < t[1] < h[3]) and h[3] < t[3]):
                        points = [t[3], h[1], h[3], t[1]]
                        verticalDistance = self.util.getDistance(points, True)
                        if (verticalDistance >= 70):
                            # newOne = [h[0], h[1], h[2], t[3]]
                            # newBoxes.append(np.array(newOne, np.uint8))
                            boxes.remove(t)

                    # check for exact top
                    elif(t[1] < h[1] and (h[1] < t[3] < h[3]) and (h[0] < t[0] < h[2]) and (h[0] < t[2] < h[2])):
                        points = [h[3], t[1], t[3], h[1]]
                        verticalDistance = self.util.getDistance(points, True)
                        if (verticalDistance >= 70):
                            # newOne = [h[0], t[1], h[2], h[3]]
                            # newBoxes.append(np.array(newOne, np.uint8))
                            boxes.remove(t)


                    # check in the middle
                    elif((h[0] < t[0] < h[2]) and (h[0] < t[2] < h[2]) and (h[1] < t[1] < h[3]) and (h[1] < t[3] < h[3])):
                        boxes.remove(t)

            logging.info("Checking for text bboxes with HTML bboxes...")

            return boxes

        except Exception as e:
            logging.error("Error occurred while checking for text bboxes. ", e)


    def checkForTextBBoxes(self):
        '''
            Purpose of this method is to check the overlapping of the text detection bboxes with other text bboxes.
            If the overlapping is above of specified limit then form the new bbox using their coordinates.
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
            param: boxes, labels, htmlboxes
            return: list
        '''
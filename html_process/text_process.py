
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
            boxesToRemove = []
            logging.info("Checking for text bboxes with HTML bboxes...")

            for t in boxes:
                for h in htmlBoxes:

                    # check for bottom right
                    if(t[1] < h[3] and t[1] > h[1] and t[0] < h[2] and t[2] > h[2] and t[2] > h[2]):
                        points = [t[3], h[1], h[3], t[1], t[2], h[0], h[2], t[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                        if(verticalDistance >= 75):
                            if(horizontalDistance >= 70):
                                boxesToRemove.append(t)
                                break

                    # check for top right
                    elif(t[1] < h[1] and (h[3] > t[3] > h[1]) and (h[0] < t[0] < h[2]) and t[2] > h[2]):
                        points = [h[3], t[1], t[3], h[1], t[2], h[0], h[2], t[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                        if(verticalDistance >= 75):
                            if(horizontalDistance >= 70):
                                boxesToRemove.append(t)
                                break

                    # check for top left
                    elif(t[1] < h[1] and (h[3] > t[3] > h[1]) and (h[0] < t[2] < h[2]) and t[0] < h[0]):
                        points = [h[3], t[1], t[3], h[1], h[2], t[0], t[2], h[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                        if (verticalDistance >= 75):
                            if (horizontalDistance >= 70):
                                boxesToRemove.append(t)
                                break

                    # check for bottom left
                    elif((h[0] < t[1] < h[3]) and t[3] > h[3] and t[0] < h[0] and (h[0] < t[2] < h[2])):
                        points = [t[3], h[1], h[3], t[1], h[2], t[0], t[2], h[0]]
                        verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                        if (verticalDistance >= 75):
                            if (horizontalDistance >= 70):
                                boxesToRemove.append(t)
                                break

                    # check for exact right
                    elif((h[1] < t[1] < h[3]) and (h[1] < t[3] < h[3]) and (h[0] < t[0] < h[2]) and t[2] > h[2]):
                        points = [t[2], h[0], h[2], t[0]]
                        horizontalDistance = self.util.getDistance(points, True)
                        if(horizontalDistance >= 70):
                            boxesToRemove.append(t)
                            break

                    # check for exact left
                    elif(t[0] < h[0] and (h[0] < t[2] < h[2]) and (h[1] < t[1] < h[3]) and (h[1] < t[3] < h[3])
                        and (h[1] < t[3] < h[3])):

                        points = [h[2], t[0], t[2], h[0]]
                        horizontalDistance = self.util.getDistance(points, True)
                        if (horizontalDistance >= 70):
                            boxesToRemove.append(t)
                            break

                    # check for exact bottom
                    elif((h[0] < t[0] < h[2]) and (h[0] < t[2] < h[2]) and (h[1] < t[1] < h[3]) and h[3] < t[3]):
                        points = [t[3], h[1], h[3], t[1]]
                        verticalDistance = self.util.getDistance(points, True)
                        if (verticalDistance >= 70):
                            boxesToRemove.append(t)
                            break

                    # check for exact top
                    elif(t[1] < h[1] and (h[1] < t[3] < h[3]) and (h[0] < t[0] < h[2]) and (h[0] < t[2] < h[2])):
                        points = [h[3], t[1], t[3], h[1]]
                        verticalDistance = self.util.getDistance(points, True)
                        if (verticalDistance >= 70):
                            boxesToRemove.append(t)
                            break

                    # check in the middle
                    elif((h[0] < t[0] < h[2]) and (h[0] < t[2] < h[2]) and (h[1] < t[1] < h[3]) and (h[1] < t[3] < h[3])):
                        boxesToRemove.append(t)
                        break

            logging.info("Checking for text bboxes with HTML bboxes...")

            return boxesToRemove

        except Exception as e:
            logging.error("Error occurred while checking for text bboxes. ", e)


    def checkForTextBBoxes(self, boxes):
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

        try:
            logging.info("Checking for text bboxes with HTML bboxes...")

            t = 0
            h = 0

            for box in range(0, len(boxes)):
                h = 0
                for nbox in range(0, len(boxes)):
                    if (boxes[t][0] == boxes[h][0] and boxes[t][3] == boxes[h][3]):
                        h += 1
                        continue

                    # check for bottom right
                    if (boxes[t][1] < boxes[h][3] and boxes[t][1] > boxes[h][1] and boxes[t][0] < boxes[h][2] and
                        boxes[t][2] > boxes[h][2] and boxes[t][2] > boxes[h][2]):
                            points = [boxes[t][3], boxes[h][1], boxes[h][3], boxes[t][1], boxes[t][2], boxes[h][0],
                                      boxes[h][2], boxes[t][0]]
                            verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                            if (verticalDistance >= 68):
                                if (horizontalDistance >= 0.3):
                                    newOne = [boxes[h][0], boxes[h][1], boxes[t][2], boxes[t][3]]
                                    boxes.append(np.array(newOne, np.uint16))
                                    if (h > t):
                                        boxes.pop(t)
                                        # we have to use h - 1, because after deleting t th element, h might point
                                        # element of position one index forward. Same for condition (h < t)
                                        boxes.pop(h - 1)
                                    elif(h < t):
                                        boxes.pop(h)
                                        boxes.pop(t - 1)
                                    t -= 1
                                    break

                    # check for top right
                    if (boxes[t][1] < boxes[h][1] and (boxes[h][3] > boxes[t][3] > boxes[h][1]) and
                          (boxes[h][0] < boxes[t][0] < boxes[h][2]) and boxes[t][2] > boxes[h][2]):
                            points = [boxes[h][3], boxes[t][1], boxes[t][3], boxes[h][1], boxes[t][2], boxes[h][0],
                                      boxes[h][2], boxes[t][0]]
                            verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                            if (verticalDistance >= 68):
                                if (horizontalDistance >= 0.3):
                                    newOne = [boxes[h][0], boxes[t][1], boxes[t][2], boxes[h][3]]
                                    boxes.append(np.array(newOne, np.uint16))
                                    if (h > t):
                                        boxes.pop(t)
                                        boxes.pop(h - 1)
                                    elif (h < t):
                                        boxes.pop(h)
                                        boxes.pop(t - 1)
                                    t -= 1
                                    break

                    # check for top left
                    if (boxes[t][1] < boxes[h][1] and (boxes[h][3] > boxes[t][3] > boxes[h][1]) and
                          (boxes[h][0] < boxes[t][2] < boxes[h][2]) and boxes[t][0] < boxes[h][0]):

                            points = [boxes[h][3], boxes[t][1], boxes[t][3], boxes[h][1], boxes[h][2], boxes[t][0],
                                      boxes[t][2], boxes[h][0]]
                            verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                            if (verticalDistance >= 68):
                                if (horizontalDistance >= 0.3):
                                    newOne = [boxes[t][0], boxes[t][1], boxes[h][2], boxes[h][3]]
                                    boxes.append(np.array(newOne, np.uint16))
                                    if (h > t):
                                        boxes.pop(t)
                                        boxes.pop(h - 1)
                                    elif (h < t):
                                        boxes.pop(h)
                                        boxes.pop(t - 1)
                                    t -= 1
                                    break

                    # check for bottom left
                    if ((boxes[h][0] < boxes[t][1] < boxes[h][3]) and boxes[t][3] > boxes[h][3] and boxes[t][0] <
                          boxes[h][0] and (boxes[h][0] < boxes[t][2] < boxes[h][2])):

                            points = [boxes[t][3], boxes[h][1], boxes[h][3], boxes[t][1], boxes[h][2], boxes[t][0],
                                      boxes[t][2], boxes[h][0]]
                            verticalDistance, horizontalDistance = self.util.getDistance(points, False)
                            if (verticalDistance >= 68):
                                if (horizontalDistance >= 0.3):
                                    newOne = [boxes[t][0], boxes[h][1], boxes[t][2], boxes[h][3]]
                                    boxes.append(np.array(newOne, np.uint16))
                                    if (h > t):
                                        boxes.pop(t)
                                        boxes.pop(h - 1)
                                    elif (h < t):
                                        boxes.pop(h)
                                        boxes.pop(t - 1)
                                    t -= 1
                                    break

                    # check for exact right
                    if ((boxes[h][1] < boxes[t][1] < boxes[h][3]) and (boxes[h][1] < boxes[t][3] < boxes[h][3]) and
                          (boxes[h][0] < boxes[t][0] < boxes[h][2]) and boxes[t][2] > boxes[h][2]):

                            points = [boxes[t][2], boxes[h][0], boxes[h][2], boxes[t][0]]
                            horizontalDistance = self.util.getDistance(points, True)
                            if (horizontalDistance >= 0.3):
                                newOne = [boxes[h][0], boxes[h][1], t[2], boxes[h][3]]
                                boxes.append(np.array(newOne, np.uint16))
                                if (h > t):
                                    boxes.pop(t)
                                    boxes.pop(h - 1)
                                elif (h < t):
                                    boxes.pop(h)
                                    boxes.pop(t - 1)
                                t -= 1
                                break

                    # check for exact left
                    if (boxes[t][0] < boxes[h][0] and (boxes[h][0] < boxes[t][2] < boxes[h][2]) and
                          (boxes[h][1] < boxes[t][1] < boxes[h][3]) and (boxes[h][1] < boxes[t][3] < boxes[h][3]) and
                          (boxes[h][1] < boxes[t][3] < boxes[h][3])):

                            points = [boxes[h][2], boxes[t][0], boxes[t][2], boxes[h][0]]
                            horizontalDistance = self.util.getDistance(points, True)
                            if (horizontalDistance >= 0.3):
                                newOne = [boxes[t][0], boxes[h][1], boxes[h][2], boxes[h][3]]
                                boxes.append(np.array(newOne, np.uint16))
                                if (h > t):
                                    boxes.pop(t)
                                    boxes.pop(h - 1)
                                elif (h < t):
                                    boxes.pop(h)
                                    boxes.pop(t - 1)
                                t -= 1
                                break

                    # check for exact bottom
                    if ((boxes[h][0] < boxes[t][0] < boxes[h][2]) and (boxes[h][0] < boxes[t][2] < boxes[h][2]) and
                          (boxes[h][1] < boxes[t][1] < boxes[h][3]) and boxes[h][3] < boxes[t][3]):

                            points = [boxes[t][3], boxes[h][1], boxes[h][3], boxes[t][1]]
                            verticalDistance = self.util.getDistance(points, True)
                            if (verticalDistance >= 68):
                                newOne = [boxes[h][0], boxes[h][1], boxes[h][2], boxes[t][3]]
                                boxes.append(np.array(newOne, np.uint16))
                                if (h > t):
                                    boxes.pop(t)
                                    boxes.pop(h - 1)
                                elif (h < t):
                                    boxes.pop(h)
                                    boxes.pop(t - 1)
                                t -= 1
                                break

                    # check for exact top
                    if (boxes[t][1] < boxes[h][1] and (boxes[h][1] < boxes[t][3] < boxes[h][3]) and
                          (boxes[h][0] < boxes[t][0] < boxes[h][2]) and (boxes[h][0] < boxes[t][2] < boxes[h][2])):

                            points = [boxes[h][3], boxes[t][1], boxes[t][3], boxes[h][1]]
                            verticalDistance = self.util.getDistance(points, True)
                            if (verticalDistance >= 68):
                                newOne = [boxes[h][0], boxes[t][1], boxes[h][2], boxes[h][3]]
                                boxes.append(np.array(newOne, np.uint16))
                                if (h > t):
                                    boxes.pop(t)
                                    boxes.pop(h - 1)
                                elif (h < t):
                                    boxes.pop(h)
                                    boxes.pop(t - 1)
                                t -= 1
                                break

                    # check in the middle
                    if ((boxes[h][0] < boxes[t][0] < boxes[h][2]) and (boxes[h][0] < boxes[t][2] < boxes[h][2]) and
                          (boxes[h][1] < boxes[t][1] < boxes[h][3]) and (boxes[h][1] < boxes[t][3] < boxes[h][3])):
                            boxes.pop(t)
                            t -= 1
                            break
                    h += 1
                t += 1

            logging.info("Checking for text bboxes with HTML bboxes...")

            return boxes

        except Exception as e:
            logging.error("Error occurred while checking for text bboxes. ", e)


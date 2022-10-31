from app_logger.logger import logging
from utils import AppUtils
import numpy as np
from app_exception import AppException
import sys
from html_process.createPage import CreateHTML

class CreateAlignment:
    def __init__(self, yamlFile, image):
        self.image = image
        self.yamlFile = yamlFile
        self.utils = AppUtils()
        self.chtml = CreateHTML(self.yamlFile, self.image)


    def getRowsAndColumns(self, boxes):
        rows = [[], [], [], []]
        '''
            Description: To get actual intuition about where the element is resides in sketch, we have to place it into
            specific row and column in the grid structure.
            param: boxes, rows
            return:
        '''

        try:
            logging.info("Started calculating rows and column for all the Bboxes of image")
            for box in boxes:
                box = np.array(box)

                row_num1 = self.utils.getRowNumber(box[1])  # get for y1
                row_num2 = self.utils.getRowNumber(box[3])  # get for y2

                row = self.utils.getActualRowNumber(row_num1, row_num2, box)

                if (len(rows[row]) == 0):
                    rows[row].append([box])
                else:

                    inserted = False
                    for col in range(len(rows[row])):

                        for elm in range(len(rows[row][col])):

                            e = rows[row][col][elm]
                            if ((((box[0] < e[0]) and (box[2] < e[2]) and (box[2] > e[0])) or
                                 ((box[0] > e[0]) and (box[2] > e[2]) and (box[0] < e[2])) or
                                 ((box[0] > e[0]) and (box[2] < e[2])) or
                                 ((box[0] < e[0]) and (box[2] > e[2])))):

                                rows[row][col].append(box)
                                rows[row][col] = sorted(rows[row][col], key=lambda x: x[1])
                                inserted = True
                                break

                        if (inserted):
                            break
                        else:
                            if (col == len(rows[row]) - 1):
                                # check if we are at last column
                                rows[row].append([box])
                                inserted = True
                                break

            rows_new = self.utils.sortColumns(rows)
            logging.info("Calculated rows and columns all the Bboxes")
            return rows_new

        except Exception as e:
            logging.error("Error occurred while getting rows and column...", e)
            raise AppException(e, sys)

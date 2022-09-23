from app_logger.logger import logging
from app_exception import AppException
import sys

class AppUtils:

    """
    Organization: iNeuron Intelligence Private Limited
    AppException is customized exception class designed to capture refined details about exception
    such as python script file line number along with error message
    With custom exception one can easily spot source of error and provide quick fix.

    """

    def getRowNumber(self, num):
        '''
            It is important to know that in which part of the image the element resides. This function calculates row number
            param: num (Y1)
            return: int
        '''
        try:
            if (120 >= num > 0):
                return 0
            elif (240 >= num > 120):
                return 1
            elif (360 >= num > 240):
                return 2
            elif (480 >= num > 360):
                return 3
        except Exception as e:
            raise AppException(e, sys)

    def getActualRowNumber(self, row_num1, row_num2, box):
        '''
            To get actual row number in case if element resides in 2 consecutive rows. (for eg. y1 in row-1 and y2 in
            row2)
            param:row_num1, row_num2, box
            return: int
        '''
        try:
            logging.info("Getting actual row number for row_num1:"+str(row_num1)+" row_num2"+str(row_num1))
            if (row_num1 == row_num2):
                return row_num1
            if (row_num2 == row_num1 + 2):
                return row_num2 - 1

            distance1 = abs(120 * (row_num1 + 1) - box[1])
            distance2 = abs(120 * (row_num2) - box[3])

            actualRow = 0
            if (distance1 > distance2):
                actualRow = row_num1
            elif (distance2 > distance1):
                actualRow = row_num2

            logging.info("Calculated row number for row_num1:" + str(row_num1) + " row_num2" + str(row_num1) + " is "
                         +str(actualRow))

            return actualRow
        except Exception as e:
            raise AppException(e, sys)

    def attachLabels(self, rows, labels):

        '''
            To combine the bbox and labels into a single list
            param: rows, labels
            return: list
        '''

        for e, l in zip(rows, labels):
            e.append(l)
        return rows

    def sortColumns(self, rows):

        '''
            Sorting of elements placed in columns to perfectly align them on the page
        '''

        # selection sort
        try:
            for column in rows:

                for idx in range(len(column) - 1):
                    min = idx
                    for new in range(idx, len(column)):
                        if (column[new][0][0] < column[min][0][0]):
                            min = new

                    temp = column[idx]
                    column[idx] = column[min]
                    column[min] = temp

            logging.info("Columns sorted...")
            logging.info(rows)

            return rows
        except Exception as e:
            raise AppException(e, sys)


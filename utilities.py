import sys


class Utilities:

    @staticmethod
    def sumOfPixelValues(res):
        total = 0
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                total += res[i][j]
        return total

    @staticmethod
    def sumOfFilter(res):
        total = 0
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                total += res[i][j]
        return total

    @staticmethod
    def divideBySum(filter_name, res, sum):
        if filter_name == "gaussian":
            return res/sum

        return res

    @staticmethod
    def findMin(image):
        min_val = image[0][0]

        for row in range(len(image)):
            for col in range(len(image[0])):
                min_val = image[row][col] if min_val >= image[row][col] else min_val
        return min_val

    @staticmethod
    def findMax(image):
        max_val = image[0][0]

        for row in range(len(image)):
            for col in range(len(image[0])):
                max_val = image[row][col] if max_val <= image[row][col] else max_val
        return max_val

    @classmethod
    def checkOutOfBounds(self, pixel_value):

        if pixel_value < 0:
            pixel_value = 0
        elif pixel_value > 255:
            pixel_value = 255

        return pixel_value

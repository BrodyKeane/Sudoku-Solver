import cv2
import numpy as np
import pytesseract
from matplotlib import pyplot as plt
import concurrent.futures

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

SUDOKU_GRID_SIZE = 9
UNASSIGNED_CELL = 0

class SudokuReader:
    def __init__(self, path):
        self.image = cv2.imread(path)

    def image_to_matrix(self):
        self.preprocess_image()
        self.resize_image()
        sudoku = self.read_cells()
        return sudoku

    def preprocess_image(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    def resize_image(self):
        contours, _ = cv2.findContours(self.image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return
        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
        second_largest_contour = sorted_contours[1]
        x, y, w, h = cv2.boundingRect(second_largest_contour)
        offset = 9
        cropped_image = self.image[y+offset:y+h-offset, x+offset:x+w-offset]
        resized_image = cv2.resize(cropped_image, ((270, 270)))
        self.image = resized_image
        h, w = self.image.shape
        if h % SUDOKU_GRID_SIZE != 0 or w % SUDOKU_GRID_SIZE != 0:

            excess_h = h % SUDOKU_GRID_SIZE
            excess_top = excess_h // 2
            excess_bottom = excess_h // 2
            if excess_h % 2 == 1:
                excess_top += 1

            excess_w = w % SUDOKU_GRID_SIZE
            excess_left = excess_w // 2
            excess_right = excess_w // 2
            if excess_w % 2 == 1:
                excess_left += 1

            self.image = self.image[excess_top: h-excess_bottom, excess_left: w-excess_right]

    def read_cells(self):
        cells = [np.hsplit(row, SUDOKU_GRID_SIZE) for row in np.vsplit(self.image, SUDOKU_GRID_SIZE)]
        sudoku = np.zeros((SUDOKU_GRID_SIZE, SUDOKU_GRID_SIZE), dtype=np.int32)
        whitelist = '123456789'

        def process_cell(cell):
            contours, _ = cv2.findContours(cell, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) > 0:
                x, y, w, h = cv2.boundingRect(contours[0])
                digit = cell[y:y+h, x:x+w]
                text = pytesseract.image_to_string(digit, config='--psm 10 --oem 3 -c tessedit_char_whitelist={}'.format(whitelist))

                if text:
                    return int(text[0])
                else:
                    return UNASSIGNED_CELL
            else:
                return UNASSIGNED_CELL

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_cell, cell) for row in cells for cell in row]
            results = [f.result() for f in futures]

        for i, result in enumerate(results):
            row = i // SUDOKU_GRID_SIZE
            col = i % SUDOKU_GRID_SIZE
            sudoku[row, col] = result

        return sudoku


    def view_image(self):
        plt.imshow(self.image)
        plt.axis(False)
        plt.show()

# expected = [
#     [4, 0, 1, 3, 2, 0, 0, 0, 0],
#     [0, 0, 0, 0, 8, 0, 0, 1, 0],
#     [0, 0, 7, 0, 0, 9, 2, 0, 3],
#     [9, 2, 0, 0, 0, 0, 1, 7, 0],
#     [3, 7, 0, 4, 0, 2, 0, 5, 9],
#     [0, 1, 4, 0, 0, 0, 0, 2, 6],
#     [7, 0, 5, 2, 0, 0, 6, 0, 0],
#     [0, 9, 0, 0, 5, 0, 0, 0, 0],
#     [0, 0, 0, 0, 3, 7, 5, 0, 8]]

# path = 'images/s3.PNG'
# reader = SudokuReader(path)
# sudoku = reader.image_to_matrix()
# # reader.view_image()
# expected = np.array(expected)
# print(np.array_equal(expected, sudoku))
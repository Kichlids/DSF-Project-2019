#!usr/bin/env python3

import pytesseract
import cv2

# Tesseract version 4
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

def main():

    num_success = 0

    # List of alphabet test cases
    # test_cases = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  # 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  # 'Y', 'Z']
    test_cases = ['color_blind_S_filtered6']

    index = 0

    while index < len(test_cases):
        # Append file type to the end
        test_file_name = test_cases[index] + '.png'
        print('Testing: ' + test_file_name)
        text_read = read_text(test_file_name)
        print('Read: ' + text_read)
        index = index + 1

def read_text(file_name):
    image = cv2.imread(file_name)
    text = pytesseract.image_to_string(image, config = '--psm 10')
    return text

if __name__ == "__main__":
    main()
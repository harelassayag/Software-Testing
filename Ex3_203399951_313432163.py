#!/usr/bin/python
import csv
import sys
import re
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path_to_csv = ''
table = []
histogram = dict()

def setUp():
    with open(path_to_csv, 'r') as data:
        for line in csv.DictReader(data):
            table.append(line)


def test():
    for line in table:
        ocr_text = pytesseract.image_to_string(Image.open(line['Path'] + line['Filename'])).strip()
        spliced_filename = re.split("_|pt", line['Filename'])
        font, size = spliced_filename[0], int(spliced_filename[1])
        if line['Text'] == ocr_text:
            if font in histogram.keys():
                if size < histogram[font]:
                    histogram[font] = size
            else:
                histogram[font] = size


def printfont():
    for (font, size) in histogram.items():
        print(font+','+str(size))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("please enter one arg with csv file path")
    path_to_csv = sys.argv[1]
    setUp()
    test()
    printfont()

# This code reads the images in the "per_pictures" and "eng_pictures" folders and converts them to text using pytesseract.
# You should have created the "per_pictures" and "eng_pictures" folders and put the images you want to convert in them.
# you can also translate the text into Persian.

from PIL import Image
import pytesseract
import pathlib
from googletrans import Translator
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
translator = Translator()

text = ""
ans = input("Do you want the photos to be translated into Persian?(y/n):")

for path in pathlib.Path("convert-photo-to-text-with-translation/per_pictures").iterdir():
    if path.is_file():
        text += pytesseract.image_to_string(Image.open(path), lang="fas")
        text += "\n" + 50 * "_" + "\n"

for path in pathlib.Path("convert-photo-to-text-with-translation/eng_pictures").iterdir():
    if path.is_file():
        eng = pytesseract.image_to_string(Image.open(path), lang="eng")
        if "y" in ans.lower():
            text += str(translator.translate(eng, src="en", dest="fa"))
        else:
            text += eng
        text += "\n" + 50 * "_" + "\n"

with open("convert-photo-to-text-with-translation/text.txt", "w", encoding="utf-8") as f:
    f.write(text)
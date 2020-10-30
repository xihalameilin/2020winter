
import pytesseract
from PIL import Image
img = Image.open('./test.png')
s = pytesseract.image_to_string(img)
print(s)

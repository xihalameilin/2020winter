
import pytesseract2
from PIL import Image
img = Image.open('./test.png')
s = pytesseract2.image_to_string(img)
print(s)

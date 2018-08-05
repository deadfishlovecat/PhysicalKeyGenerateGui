__author__ = 'caocongcong'
from PIL import Image
import PIL
import numpy as np
im = Image.open('../data/seu.png')
img = im.convert('L')
img.thumbnail((120, 120))
img_data = np.array(img)
img = img.resize((300, 300), PIL.Image.ANTIALIAS)
print(img.size)
img.show()
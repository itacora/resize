import os
import glob
from PIL import Image

files = glob.glob('C:\\Users\\hogehoge\\*.png')
a = 0
for f in files:
    a = a+1
    img = Image.open(f)
    img_resize = img.resize((128, 128))
    ftitle, fext = os.path.splitext(f)
    img_resize.save('C:\\Users\\hogehoge\\' + str(a) + '_tr_' + fext)

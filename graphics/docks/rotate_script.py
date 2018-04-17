import os

from PIL import Image
from copy import deepcopy

for filename in os.listdir("."):
    if filename.endswith(".png"):
        for i in [0, 60, 120, 180, 240, 300]:
            img = Image.open(filename)
            img = img.rotate(i, expand=True)
            img.save("{}/{}".format(i, filename))

import value as value
from PIL import Image
import random

im = Image.open('dog.jpg') # Can be many different formats.
pix = im.load()
print (im.size)  # Get the width and height of the image for iterating over
print (pix[random.randint(1, 50), random.randint(1, 50)])# Get the RGBA Value of the a pixel of an image ##change x , and y to values
pix[random,random] = random.randint(x,y) # Set the RGBA Value of the image (tuple)
#im.save('alive_parrot.png')  # Save the modified pixels as .png
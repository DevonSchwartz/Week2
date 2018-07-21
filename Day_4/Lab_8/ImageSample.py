'''
Created on Oct 23, 2016

@author: Susan Rodger
'''
from PIL import Image

# Sample Program
img = Image.open("dukelogo.png") 
img.show()
pixels = [(0,b,g) for (r,g,b) in img.getdata()] 
img.putdata(pixels) 
img.show() 
'''
Created on Oct 25, 2011
Modified on Oct 31, 2012
Modified on Mar 4, 2017 by Susan Rodger

@author: rcd, alexandrudutu, ola
'''
from PIL import Image

# alternatively, try the line below
#import Image    # standard python image library


def apply_filter(image, filter):
    '''
    Create and return a NEW image, based on a
    transform of each pixel in the given image using the given filter
    image is an open Image object
    filter is a function to apply to each pixel in image
    return new image, same size, to which filter has been applied to each pixel of image
    '''
    pixels = [ filter(p) for p in image.getdata() ]
    nim = Image.new("RGB",image.size)
    nim.putdata(pixels)
    return nim

def open_image(filename):
    '''
    opens the given image and converts it to RGB format
    returns a default image if the given one cannot be opened
    filename is the name of a PNG, JPG, or GIF image file
    '''
    image = Image.open(filename)
    if image == None:
        print("Specified input file " + filename + " cannot be opened.")
        return Image.new("RGB", (400, 400))
    else:
        print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
        return image.convert("RGB")


'''
During this lab a pixel is a tuple of 3 values (R, G, B)
representing the red, green, and blue components of a color
that each range from [0-255] inclusive.
The filter functions:
    - take one pixel as an argument,
    - modify the channels of the pixel and
    - return the transformed pixel
'''
def identity(pixel):
    '''
    returns a pixel that is unchanged from the original
    '''
    r,g,b = pixel
    return (r,g,b)


def invert(pixel):
    '''
    returns a pixel where every pixel channel is 255 minus its value
    '''
    r,g,b = pixel
    return (255-r, 255-g, 255-b)

def darken(pixel):
    """
    returns a pixel whose red, green, and blue values are all 90% of those given
    """
    r,g,b = pixel
    return (int(.25 * r), int(.25 * g), int(.25 * b))

def brighten(pixel):
    """
    returns a pixel whose red, green, and blue values are all 110% of those given
    but not over 255 (the maximum value).
    """
    r,g,b = pixel
    return (int(1.75 * r), int(1.75 * g), int(1.75 * b))

def gray_scale(pixel):
    '''
    returns a pixel whose red, green, and blue values are all set to the same value:
      the average of the original channels
    '''
    r,g,b = pixel
    x = (r + g + b) / 3
    return (int(x),int(x),int(x))

def posterize(pixel):
    """
    returns a pixel whose red, green, and blue values are all changed in
    the following way:
     - divide channel's range into 4 equal pieces (i.e., 0-63, 64-127, 128-191, 192-255)
     - set the channel's value to a fixed value within that range (i.e., 50, 100, 150, 200)
    """
    r,g,b = pixel
    if r >= 0 and r<= 63:
        r = 50
    elif r >= 64 and r<= 127:
        r = 100
    elif r >= 128 and r<= 191:
        r = 150
    elif r >= 192 and r<=255:
        r = 200

    if g >= 0 and g <= 63:
        g = 50
    elif g >= 64 and g <= 127:
        g = 100
    elif g >= 128 and g <= 191:
        g = 150
    elif g >= 192 and g <=255:
        g = 200

    if b >= 0 and b <= 63:
        b = 50
    elif b >= 64 and b <= 127:
        b = 100
    elif b >= 128 and b <= 191:
        b = 150
    elif b >= 192 and b <=255:
        b = 200
    return (r,g,b)

def solarize(pixel):
    """
    returns a pixel whose red, green, and blue values are all changed in
    the following way:
     - if the value is less than 128, set it to 255 - the original value.
     - if the value is 128 or greater, don't change it.
    """
    r,g,b = pixel
    if r < 128:
        r = 255 - r
    if g < 128:
        g = 255 - g
    if b < 128:
        b = 255 - b
    return(r,g,b)

def denoise(pixel):
    '''
    take noise out of a pixel
    '''
    r,g,b = pixel

    g = 0
    b = 0
    r = r * 10

    return (r,g,b)

def denoise2(pixel):
    '''
    take noise out of a pixel
    '''
    r,g,b = pixel
    r = 0
    b = b * 19
    g = g * 19
    return (r,g,b)



def denoise3(pixel):
    '''
    take noise out of a pixel
    '''
    r,g,b = pixel
    if r == 255 and g == 255 and b == 255:
        r = 0
        g = 0
        b = 0
    if r == 255 and g == 0 and b == 0:
        r = 0
    return (r,g,b)
def load_and_go(fname,filterfunc):
    image = open_image(fname)
    nimage = apply_filter(image,filterfunc)
    image.show()
    nimage.show()
    '''
    processedImage.jpg is the name of the file
    the image is saved in. The first time you do
    this you may have to refresh to see it.
    '''
    nimage.save("processedImage.jpg")


if __name__ == "__main__":
    ''' Change the name of the file and the function
        to apply to the file in the line below
    '''
    input_file = "bluedevil.jpg"
    load_and_go(input_file, gray_scale)

gray_scale(pixel)

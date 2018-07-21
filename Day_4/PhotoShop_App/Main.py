from PIL import Image

from PIL import ImageFilter

def apply_filter(image,filter):
    pixels = [filter(p) for p in image.getdata()]
    nim = Image.new('RGB', image.size)
    nim.putdata(pixels)
    return nim

def open_image(filename):
    image = Image.open(filename)
    if image == None:
        print ("Specified Input file " + filename + "cannot be opened")
        return Image.new('RBG', image.size)

    else:
        print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
        return image.convert("RGB")


def invert(pixel):

    r,g,b = pixel
    return (255-r, 255-g, 255-b)

def darken(pixel):

    r,g,b = pixel
    return (int(.5 * r), int(.5 * g), int(.5 * b))

def brighten(pixel):
    r,g,b = pixel
    return (int(1.5 * r), int(1.5 * g), int(1.5 * b))

def gray_scale(pixel):
    r,g,b = pixel
    x = (r + g + b) / 3
    return (int(x),int(x),int(x))

def posterize(pixel):
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

    r,g,b = pixel
    if r < 128:
        r = 255 - r
    if g < 128:
        g = 255 - g
    if b < 128:
        b = 255 - b
    return(r,g,b)

def crop(image,coordinates):
    crop = image.crop(coordinates)
    image.show()
    crop.show()
    crop.save("processedImage.jpg")
    return (crop)

def blur(image,radius):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
    image.show()
    blurred_image.show()
    blurred_image.save("processedImage.jpg")

def sharpen(image):
    inpt_radius = eval(input("What radius would you like?(Choose number 1 - 3): "))
    inpt_percent = eval(input("What percentage would you like?(Choose a number 100 - 300): "))
    inpt_threshold = eval(input("What threshold would you like?(Choose a number from 3 - 5): "))
    sharpened_image = image.filter(ImageFilter.UnsharpMask(radius = int(inpt_radius), percent = int(inpt_percent), threshold = int(inpt_threshold)))
    image.show()
    sharpened_image.show()
    sharpened_image.save("processedImage.jpg")





def load_and_go (fname,filterfunc):
    image = open_image(fname)
    nimage = apply_filter(image,filterfunc)
    image.show()
    nimage.show()
    nimage.save("processedImage.jpg")







def Choice():
    input_filename = input("What file would you like?")
    image = Image.open(input_filename)
    print ("You can invert, darken, brighten, turn the image black and white(press b),")
    print ("posterize, solarize, crop, blur, or sharpen")
    choice = input("What would you like to do?: ")

    if choice == ("crop"):
        print(str(image.size))
        print(str(len(image.getdata())))
        print("Input the coordinates you would like to crop out.")
        print("It will crop out your coordinates and everything in between")
        print("Your first input will specify the upper-x coordinate of your area")
        print("Your second input will specify the upper-y coordinate of your area ")
        print("Your third input will specify the lower-x coordinate of your area")
        print ("Your fourth input will specify the lower-y coordinate corner of your area")
        print("The (0,0) or origin of the picture is the top-left, not the bottom left")
        upper_left = eval(input("Input a coordinate (upper-x): "))
        upper_right = eval(input("Input a coordinate(upper-y): "))
        lower_left = eval(input("Input a coordinate(lower-x): "))
        lower_right = eval(input("Input a coordinate(lower-y): "))
        coordinates = (int(upper_left),int(upper_right),int(lower_left),int(lower_right))
        print (coordinates)
        crop(image, coordinates)

    elif choice == ('invert'):
        load_and_go(input_filename,invert)
        invert(pixel)

    elif choice == ('darken'):
        percentage = float(input("What percentage would you like to darken? : "))
        percentage = percentage / 100
        load_and_go(input_filename,darken)
        darken(pixel, percentage)

    elif choice == ('brighten'):
        percentage = float(input("What percentage would you like to brighten? : "))
        percentage = percentage / 100
        load_and_go(input_filename,brighten)
        brighten(pixel, percentage)

    elif choice == ('b'):
        load_and_go(input_filename,gray_scale)
        gray_scale(pixel)

    elif choice == ('posterize'):
        load_and_go(input_filename,posterize)
        posterize(pixel)

    elif choice == ('solarize'):
        load_and_go(input_filename,solarize)

        solarize(pixel)

    elif choice == ("blur"):
        radius = eval(input("What radius would you like?: "))

        blur(image,radius)

    elif choice == ("sharpen"):

        sharpen(image)

if __name__ == "__main__":
    Choice()

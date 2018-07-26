from PIL import Image, ImageColor, ImageDraw
import random

im = Image.new('RGBA', (500,500))
imWidth, imHeight = im.size
im.save('imagebase.png')

red = ImageColor.getcolor('red', 'RGBA')
blue = ImageColor.getcolor('blue', 'RGBA')

filename = 'generatedImg'
num = 0
for i in range(5):

    for x in range(imWidth):
        for y in range(imHeight):

            state = random.randint(0,1)
            horizon = random.randrange(-100,100)

            if y < ((imHeight/2) - horizon):

                if state == 0:
                    im.putpixel((x,y), (210,210,210,50))
                else:
                    im.putpixel((x,y),(210,210,210))
            else:
            
                if state == 0:
                    im.putpixel((x,y),red)
                else:
                    im.putpixel((x,y),blue)

    num += 1 
    im.save(filename + str(num) + '.png')
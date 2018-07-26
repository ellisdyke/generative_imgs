from PIL import Image, ImageColor, ImageDraw
import random

im = Image.new('RGBA', (500,500))
imWidth, imHeight = im.size
draw = ImageDraw.Draw(im)
px = 10
rows = imWidth / px
cols = imHeight / px

im.save('imagebase.png')

red = ImageColor.getcolor('red', 'RGBA')
blue = ImageColor.getcolor('blue', 'RGBA')

filename = 'generatedImg'
num = 0
for i in range(1):

    for x in range(imWidth):
        for y in range(imHeight):

            state = random.randint(0,1)
            horizon = random.randrange(-100,100)

            if y < ((imHeight/2) - horizon):

                path_pts = [(x,y)]

                for i in range(random.randrange(-100,100)):
                    if x < imWidth and y < imHeight:
                        x2 = x + 1 
                        y2 = y + 1
                        path_pts.append((x2,y2))

                #if state == 0:
                    #draw.line(path_pts, (210,210,210,50))
                #else:
                    draw.line(path_pts,(210,210,210),10)

            else:
                if state == 0:
                    im.putpixel((x,y),red)
                else:
                    im.putpixel((x,y),blue)

    num += 1 
    im.save(filename + str(num) + '.png')

from PIL import Image, ImageColor, ImageDraw
import random

red = ImageColor.getcolor('red', 'RGB')
blue = ImageColor.getcolor('blue', 'RGB')
white = ImageColor.getcolor('white', 'RGB')
light_gray = ImageColor.getcolor('lightgray', 'RGB')

filename = 'test'
num = 0

im = Image.new('RGB', (500,500), light_gray)
imWidth, imHeight = im.size

im.save('base.jpg')
draw = ImageDraw.Draw(im)



for i in range(2):


    for x in range(imWidth):
        for y in range(imHeight):

            state = random.randint(0,1)
            horizon = random.randrange(-100,50)

            draw.rectangle((x, y, imWidth, imHeight), (135,206,235))
       

            if y > ((imHeight/2) - horizon):

                randomize = random.randint(-30, 30)
                lightest = 400 + randomize
                mid = 450 + randomize

                if state == 1:#shades of red
                    if y <= lightest:
                        draw.rectangle((x, y, x + 100, y + 100),(255,99,71))

                    elif y <= mid:
                        draw.rectangle((x,y,x+100,y+100), (229,89,63))
                    
                    else:
                        draw.rectangle((x,y,x+100,y+100), (204,79,56))
                        
                if state == 0: #shades of blue
                    if y >= mid:
                        draw.rectangle((x,y,x+100,y+100), (121,185,211)) 

                    else:
                        draw.rectangle((x,y,x+100,y+100), (108,164,188))                     

    num += 1
    n = str(num)
    im.save(filename + n + '.jpg')
    im.show()

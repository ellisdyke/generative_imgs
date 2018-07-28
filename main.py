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



for i in range(1):


    for x in range(imWidth):
        for y in range(imHeight):

            state = random.randint(0,1)
            horizon = random.randrange(-100,50)

            draw.rectangle((x, y, imWidth, imHeight), (135,206,235))
       
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
                    draw.line(path_pts,(135,206,235),10)

            if y > ((imHeight/2) - horizon):

                randomize = random.randint(-30, 30)
                px_size = random.randint(0,2)
                #lightest = 400 + randomize
                #mid = 450 + randomize

                if state == 1:#shades of red
                    #if y <= lightest:
                     #   draw.rectangle((x, y, x + 100, y + 100),(255,99,71))

                    #elif y <= mid:
                     #   draw.rectangle((x,y,x+100,y+100), (229,89,63))
                    
                    #else:
                    draw.rectangle((x,y,x+px_size,y+px_size), (204,79,56))
                        
                if state == 0: #shades of blue
                   
                    draw.rectangle((x,y,x+100,y+100), blue)                     

    num += 1
    n = str(num)
    im.save(filename + n + '.jpg')
    im.show()

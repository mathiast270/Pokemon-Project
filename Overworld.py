#For gym similar to minimax AI 
#Store data in dictionary, room size/ center position
# room size will be a random from 1/4 of prev to 1/2 of prev


from cmu_112_graphics import *
import random
ls = []
def distance(x1, y1, x2, y2):
    x = ((x2-x1)**2 + (y2-y1)**2)**0.5  # used formula
    return x

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    x = distance(x1,y1,x2,y2)
    result = (x <= r1+r2)
    return result

def appStarted(app):
    app.scrollY = 0
    app.scrollX = 0
    app.dotsgrass = [(random.randrange(app.width),
                  random.randrange(60, app.height)) for _ in range(10)]
    app.dotstrees = [(random.randrange(app.width),
                  random.randrange(60, app.height)) for _ in range(10)]
    url2 = 'Sprites/Grass 2.png'
    app.spritestrip2 = app.loadImage(url2)
    url3 = 'Sprites/Trees.png'
    app.spritestrip3 = app.loadImage(url3)
    url = 'Sprites/boy_run_1.png'
    app.spritestrip = app.loadImage(url)
    url4 = 'Sprites/Grass.png'
    app.spritestrip4 = app.loadImage(url4)
    url5 = 'Sprites/Gymleader.png'
    app.spritestrip5 = app.loadImage(url5)
    app.temp = [ ]
    app.sprite2 = []
    app.pos = 0
    for j in range(4):
        app.temp = [ ]
        for i in range(4):
            sprite = app.spritestrip.crop((0+60*i,10+60*j,60*(i+1),10+60*(j+1)))
            app.temp.append(sprite)
        app.sprite2.append(app.temp) 
    app.spriteCounter = 0
    BSPTree(600,600,0,0)
    count = 0
    for i in ls:
        if(i[3] == 2 and count == 0):
            app.cx, app.cy= i[0], i[1]
            count+=1
        elif(i[3] == 2 and count == 1):
            app.gymx,app.gymy = i[0], i[1]
            break
def isin(cx,cy,roomsize):
    for i in ls:
        if((i[0]-i[2]/2)<cx+roomsize/2 and (i[0]+i[2]/2)>cx-roomsize/2 and (i[1] -i[2]/2)<cy+roomsize/2 and (i[1]+i[2]/2)>cy-roomsize/2):
            return True
    return False


def BSPTree(width,height,depth,vorh):   
    if(depth == 3):
        return 
    else:
        if(vorh%2 == 0):
            cx = random.randint(0,width//2)
            cx2 = random.randint(width//2,width)
            cy = random.randint(0,height)
            roomsize = random.randint(50,100)
            if(isin(cx,cy,roomsize) == False):
                ls.append([cx,cy,roomsize,depth])
                BSPTree(width//2,height,depth+1,vorh+1)
            if(isin(cx2,cy,roomsize) == False):
                ls.append([cx2,cy,roomsize,depth])
                BSPTree(width,height,depth+1,vorh+1)
        elif(vorh%2 == 1):
            cx = random.randint(0,width)
            cy = random.randint(0,height//2)
            cy2 = random.randint(height//2,height)
            roomsize = random.randint(50,100)
            if(isin(cx,cy,roomsize) == False):
                ls.append([cx,cy,roomsize,depth])
                BSPTree(width,height//2,depth+1,vorh+1)
            if(isin(cx,cy2,roomsize) == False):
                ls.append([cx,cy2,roomsize,depth])
                BSPTree(width,height,depth+1,vorh+1)

            

def keyPressed(app, event):
    if (event.key == "Left"):    
        app.scrollX -= 5
        app.pos = 1
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app) == False):
            app.scrollX+=5
    elif (event.key == "Right"): 
        app.scrollX += 5
        app.pos = 2
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app) == False):
            app.scrollX-=5
    elif(event.key == "Up"):    
        app.scrollY +=5
        app.pos = 3
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app)== False):
            app.scrollY-=5
    elif(event.key == "Down"):  
        app.scrollY -=5
        app.pos = 0
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app) == False):
            app.scrollY+=5
def ifanyin(app):
    best = 10000000
    cx2 = None
    for (cx, cy,roomsize,depth) in ls:
        x = ls.index([cx,cy,roomsize,depth])+1
        cx -= app.scrollX
        cy +=app.scrollY 
        if(depth == 2):
            if(x<len(ls)-1):
                for j in range(x,len(ls)):
                    if(j<len(ls) and ls[j][3] == 2):
                        (cx2,cy3,roomsize2, depth2) = ls[j]
                        cx2 -=app.scrollX
                        cy3 +=app.scrollY
                       
                        if(cx2>cx):
                            if(cx+roomsize/2<app.cx<cx2+roomsize2/2 and cy-5<app.cy<cy+5):
                                return True
                        elif(cx>cx2):
                            if(cx2+roomsize2/2<app.cx<cx+roomsize/2 and cy-5<app.cy<cy+5):
                                return True
                        if(cy3>cy):
                            if(cy+roomsize/2<app.cy<cy3+roomsize2/2 and cx2-5<app.cx<cx2+5):
                                return True
                        elif(cy>cy3):
                            if(cy3+roomsize2/2<app.cy<cy+roomsize/2 and cx2-5<app.cx<cx2+5):
                                return True
            if(best>distance(cx,cy,app.cx,app.cy)):
                cx1 = cx
                cy2 = cy
                room = roomsize
                best = distance(cx,cy,app.cx,app.cy)
                y = x
    
    
    if((cx1-room/2<app.cx<cx1+room/2 and cy2-room/2<app.cy<cy2+room/2)):
         return True
    return False      
def redrawAll(app, canvas):
    thickness = 5
    canvas.create_rectangle(0,0,app.width,app.height,fill = 'black')
    alreadin = []
    for (cx,cy,roomsize,depth) in ls:
        if(depth == 2):
            x = ls.index([cx,cy,roomsize,depth])+1
            cx-=app.scrollX
            cy += app.scrollY
            
            canvas.create_rectangle(cx - (roomsize/2),cy-(roomsize/2),cx + (roomsize/2), cy + (roomsize/2),fill= 'green')
            
            for j in range(x,len(ls)):
                if(j<len(ls) and ls[j][3] == 2):
                    canvas.create_rectangle(ls[j][0] + ls[j][2]/2-app.scrollX,cy - thickness,cx + roomsize/2, cy +thickness,fill = 'blue')
                    canvas.create_rectangle(ls[j][0] + ls[j][2]/2-app.scrollX- thickness,ls[j][1]  +ls[j][2]/2+app.scrollY,ls[j][0] + ls[j][2]/2 + thickness - app.scrollX,cy,fill = 'blue')
                    alreadin.append(j)

    x = app.width/2
    canvas.create_text(x, 20, text='Use arrows to move left or right')
    canvas.create_text(x, 40, text=f'app.scrollX = {app.scrollX}')
    sprite = app.sprite2[app.pos][app.spriteCounter]
    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(sprite))
    canvas.create_image(app.gymx-app.scrollX, app.gymy+app.scrollY, image=ImageTk.PhotoImage(app.spritestrip5))

runApp(width=600, height=600)

# list I should use for grass = 
# for j in (4):
#   for i in (app.width/24):
#       app.dotgrass.append((i*24,-300 + j*21))
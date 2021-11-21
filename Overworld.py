# SideScroller1:

from cmu_112_graphics import *
import random
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
    
def keyPressed(app, event):
    if (event.key == "Left"):    
        app.scrollX -= 5
        app.pos = 1
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app)):
            app.scrollX+=5
    elif (event.key == "Right"): 
        app.scrollX += 5
        app.pos = 2
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app)):
            app.scrollX-=5
    elif(event.key == "Up"):    
        app.scrollY +=5
        app.pos = 3
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app)):
            app.scrollY-=5
    elif(event.key == "Down"):  
        app.scrollY -=5
        app.pos = 0
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app)):
            app.scrollY+=5
def timerFired(app):
    return
def ifanyin(app):
    for (cx, cy) in app.dotstrees:
        cx -= app.scrollX
        cy +=app.scrollY
        if(circlesIntersect(cx,cy,10,app.width/2,app.height/2,10)):
            return True
    return False
def redrawAll(app, canvas):
    
    for j in range(16):
        for i in range(16):
             canvas.create_image(i*20, j*20, image=ImageTk.PhotoImage(app.spritestrip4))

    
    for (cx, cy) in app.dotsgrass:
        cx -= app.scrollX  
        cy += app.scrollY
        canvas.create_image(cx, cy, image=ImageTk.PhotoImage(app.spritestrip2))
    for (cx, cy) in app.dotstrees:
        cx -= app.scrollX
        cy += app.scrollY
                 
        canvas.create_image(cx, cy, image=ImageTk.PhotoImage(app.spritestrip3))
    x = app.width/2 - app.scrollX 
    y = app.height/2


    x = app.width/2
    canvas.create_text(x, 20, text='Use arrows to move left or right')
    canvas.create_text(x, 40, text=f'app.scrollX = {app.scrollX}')
    sprite = app.sprite2[app.pos][app.spriteCounter]
    cx, cy, r = app.width/2, app.height/2, 10
    canvas.create_image(cx, cy, image=ImageTk.PhotoImage(sprite))

runApp(width=300, height=300)

# list I should use for grass = [(200,150),]
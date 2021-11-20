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

    
def keyPressed(app, event):
    if (event.key == "Left"):    
        app.scrollX -= 5
        if(ifanyin(app)):
            app.scrollX+=5
    elif (event.key == "Right"): 
        app.scrollX += 5
        if(ifanyin(app)):
            app.scrollX-=5
    elif(event.key == "Up"):    
        app.scrollY +=5
        if(ifanyin(app)):
            app.scrollY-=5
    elif(event.key == "Down"):  
        app.scrollY -=5
        if(ifanyin(app)):
            app.scrollY+=5
def timerFired(app):
    return
def ifanyin(app):
    for (cx, cy) in app.dotstrees:
        cx -= app.scrollX#account for each x and y separtly
        cy +=app.scrollY
        if(circlesIntersect(cx,cy,10,app.width/2,app.height/2,10)):
            return True
    return False
def redrawAll(app, canvas):
    # draw the player fixed to the center of the scrolled canvas
    cx, cy, r = app.width/2, app.height/2, 10
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='cyan')

    # draw the dots, shifted by the scrollX offset
    for (cx, cy) in app.dotsgrass:
        cx -= app.scrollX  # <-- This is where we scroll each dot!!!
        cy += app.scrollY
        canvas.create_image(cx, cy, image=ImageTk.PhotoImage(app.spritestrip2))
    for (cx, cy) in app.dotstrees:
        cx -= app.scrollX
        cy += app.scrollY
                  # <-- This is where we scroll each dot!!!
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='blue')
    # draw the x and y axes
    x = app.width/2 - app.scrollX # <-- This is where we scroll the axis!
    y = app.height/2
    canvas.create_line(x, 0, x, app.height)
    canvas.create_line(0, y, app.width, y)

    # draw the instructions and the current scrollX
    x = app.width/2
    canvas.create_text(x, 20, text='Use arrows to move left or right')
    canvas.create_text(x, 40, text=f'app.scrollX = {app.scrollX}')

runApp(width=300, height=300)
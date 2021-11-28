from Pokemon import*
from cmu_112_graphics import*
from Gameai import*
import math
gymw = 250
gymh = 135
ls = []
def distance(x1, y1, x2, y2):
    x = ((x2-x1)**2 + (y2-y1)**2)**0.5  # used formula
    return x

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    x = distance(x1,y1,x2,y2)
    result = (x <= r1+r2)
    return result

def appStarted(app):
    app.mode = 'overworld'
    app.counter = 0
    app.Trainer1 = Trainer1
    app.Trainer2 = Trainer2
    app.Poke1col = 'green'
    app.Poke2col = 'green'
    app.allowmove = True 
    app.count = 0
    app.currmove = None
    app.currmove2 = None
    app.pokeswitch = None
    app.allowmove2 = True
    app.allowmoves = False
    #for sprite drawing
    url = 'Sprites/Garchomp back.png'
    app.spritestrip = app.loadImage(url)
    app.sprites = [ ]
    app.spritesdict = {}
    app.spritedict2 = {}
    url = 'Sprites/Battlebackground.png'
    app.sprite8 = app.loadImage(url)
    app.count = 0
    app.spritestrip2 = app.loadImage(url)
    for k in app.Trainer1.poklist: 
        app.sprites = [ ]
        url = k.sprite
        app.spritestrip = app.loadImage(url)
        for j in range(len(k.slist)):
            for i in range(len(k.slist[0])):
                if(k.slist[j][i] == (0,0,0,0)):
                    continue
                sprite = app.spritestrip.crop((k.slist[j][i][0], k.slist[j][i][1] ,k.slist[j][i][2], k.slist[j][i][3]))
                app.sprites.append(sprite)
        app.spritesdict[k.name] = app.sprites
    for a in app.Trainer2.poklist: 
        app.sprites2 = [ ]
        url = a.sprite
        app.spritestrip2 = app.loadImage(url)
        for j in range(len(a.slist)):
            for i in range(len(a.slist[0])):
                if(a.slist[j][i] == (0,0,0,0)):
                    continue
                sprite = app.spritestrip2.crop((a.slist[j][i][0], a.slist[j][i][1] ,a.slist[j][i][2], a.slist[j][i][3]))
                app.sprites2.append(sprite)
        app.spritedict2[a.name] = app.sprites2
    app.spriteCounter1 = 0
    app.spriteCounter2 = 0
    app.scrollY = 0
    app.scrollX = 0
    app.dotsgrass = []
    for j in range(4):
       for i in range(app.width//24):
          app.dotsgrass.append((i*24,-300 + j*21))
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
    url5 = 'Sprites/Gym.png'
    app.spritestrip5 = app.loadImage(url5)
    app.gym = (200,-500)
    for j in range(4):
        app.temp = [ ]
        for i in range(4):
            sprite = app.spritestrip.crop((0+60*i,10+60*j,60*(i+1),10+60*(j+1)))
            app.temp.append(sprite)
        app.sprite2.append(app.temp) 
    app.spriteCounter = 0
    app.count = 0
    url6= 'Sprites/Gymleader.png'
    app.spritestrip6 = app.loadImage(url6)
    BSPTree(app.width,app.height,0,0)
    count = 0
    for i in ls:
        if(i[3] == 2 and count == 0):
            app.cx, app.cy= i[0], i[1]
            count+=1
        elif(i[3] == 2 and count == 1):
            app.gymx,app.gymy = i[0], i[1]
            break
    print(app.cx)
    app.scrollX2 = 0
    app.scrollY2 = 0
def battle(app,Trainer1s,Trainer2s):
            moveai = ai(Trainer2s,Trainer1s)
           # print(moveai.name)
            Pokemon1 = Trainer1s.curr
            Pokemon2 = Trainer2s.curr   
            if(app.currmove == 'switch'):
                Trainer1s.curr = app.pokeswitch
            if(type(moveai) == str):
                pokeswitchs = moveai.split('+')[1]
                for i in Trainer2.pokelist():
                    if(i.name == pokeswitchs):
                        Trainer2s.curr = i
            if(Pokemon1.currspeed>Pokemon2.currspeed):
                if(app.currmove != 'switch'):
                    damages = damage(Pokemon1,Pokemon2,app.currmove)
                    Pokemon2.currhp -=damages
                if(Pokemon2.currhp<0):
                    print(f'{Pokemon1.name} wins')
                    return
                if(type(moveai) != str):
                    app.currmove2 = moveai
                    damages2 = damage(Pokemon2,Pokemon1,moveai)
                    Pokemon1.currhp -= damages2
            else:
                if(type(moveai) != string):
                    damages2 = damage(Pokemon2,Pokemon1,moveai)
                    Pokemon1.currhp -= damages2
                if(Pokemon1.currhp<0):
                    print(f'{Pokemon2.name} wins')
                    return
                if(app.currmove != 'switch'):
                    damages = damage(Pokemon1,Pokemon2,app.currmove)
                    Pokemon2.currhp -=damages

def battle_timerFired(app):
    if( (app.Trainer1.teamalive() and app.Trainer2.teamalive()) and (app.allowmoves)): 
        battle(app,app.Trainer1,app.Trainer2)
        app.allowmove = False
        app.allowmoves = False
        
        app.count +=1
    app.spriteCounter1 = (1 + app.spriteCounter1) % len(app.spritesdict[app.Trainer1.curr.name])
    app.spriteCounter2 = (1 + app.spriteCounter2) % len(app.spritedict2[app.Trainer2.curr.name])
    if(app.Trainer2.curr.currhp<=0):
        for i in range(len(app.Trainer2.pokelist())):
            if(app.Trainer2.pokelist()[i].currhp>0):
                Trainer2.curr  = app.Trainer2.pokelist()[i]
                app.spriteCounter2 = 0
                break
    if(app.Trainer1.curr.currhp<=0):
        for i in range(len(app.Trainer1.pokelist())):
            if(app.Trainer1.pokelist()[i].currhp>0):
                Trainer1.curr  = app.Trainer1.pokelist()[i]
                app.spriteCounter1 = 0
                break
    if(app.Trainer2.teamalive() == False or app.Trainer1.teamalive() == False):
        app.Trainer2.restoreall()
        app.Trainer1.restoreall()
        app.mode = 'overworld'
        
    
      
def battle_mousePressed(app, event):
        app.count+=1    #What I need to do: If my Pokemon is dead let me switch for free
    #if(app.allowmove and app.allowmove2):
        if(event.x>(2.5/5)*app.width and event.x<(3.5/5)*app.width and #and if enemy is dead 
            event.y>(2.5/5)*app.height and event.y<(3/5)*app.height ):
            app.allowmoves = True
            app.currmove = app.Trainer1.curr.moves[0]
        elif(event.x>(3.5/5)*app.width and event.x<(4.5/5)*app.width and  
            event.y>(2.5/5)*app.height and event.y<(3/5)*app.height ):
            app.allowmoves = True
            app.currmove = app.Trainer1.curr.moves[1]
        elif(event.x>(2.5/5)*app.width and event.x<(3.5/5)*app.width and  
            event.y>(3/5)*app.height and event.y<(3.5/5)*app.height ):
            app.allowmoves = True
            app.currmove = app.Trainer1.curr.moves[2]
        elif(event.x>(3.5/5)*app.width and event.x<(4.5/5)*app.width and  
            event.y>(3/5)*app.height and event.y<(3.5/5)*app.height ):
            app.allowmoves = True
            app.currmove = app.Trainer1.curr.moves[0]
        elif(event.x>(1/7)*app.width and event.x<(2/7)*app.width and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[0].currhp >0):
            app.pokeswitch = app.Trainer1.pokelist()[0]
            app.allowmoves = True
            app.currmove = 'switch'
        elif(event.x>(2/7)*app.width and event.x<(3/7)*app.width and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[1].currhp >0):
            app.pokeswitch = app.Trainer1.pokelist()[1]
            app.allowmoves = True
            app.currmove = 'switch'
        elif(event.x>(3/7)*app.width and event.x<(4/7)*app.width and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[2].currhp >0):
            app.pokeswitch = app.Trainer1.pokelist()[2]
            app.allowmoves = True
            app.currmove = 'switch'
        elif(event.x>(4/7)*app.width and event.x<(5/7)*app.width and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[3].currhp >0):
            app.pokeswitch = app.Trainer1.pokelist()[3]
            app.allowmoves = True
            app.currmove = 'switch'
        elif(event.x>(4/7)*app.width and event.x<(5/7)*app.width and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[4].currhp >0):
            app.pokeswitch = app.Trainer1.pokelist()[4]
            app.allowmoves = True
            app.currmove = 'switch'
        app.counter += 1
        app.count +=1
    
def battle_redrawAll(app, canvas):
    canvas.create_image(app.width/2,app.height/2,image=ImageTk.PhotoImage(app.sprite8))
    sprite = app.spritesdict[app.Trainer1.curr.name][app.spriteCounter1]
    sprite2 = app.spritedict2[app.Trainer2.curr.name][app.spriteCounter2]
    canvas.create_image(app.width*(75/400), app.height*(250/400), image=ImageTk.PhotoImage(sprite))
    canvas.create_image(app.width*(3/4), app.width*(1/4), image=ImageTk.PhotoImage(sprite2))
    canvas.create_text(app.width*(3.5/5), app.height*(2.3/5),
                       text= 'Moves', font='Arial 12 bold')
    canvas.create_text(app.width*(3/5), app.height*(2.75/5),
                       text= app.Trainer1.curr.moves[0].name, font='Arial 10 bold')

    canvas.create_text(app.width*(4/5), app.height*(2.75/5),
                       text= app.Trainer1.curr.moves[1].name, font='Arial 10 bold')

    canvas.create_text(app.width*(3/5), app.height*(3.25/5),
                       text= app.Trainer1.curr.moves[2].name, font='Arial 10 bold')

    canvas.create_text(app.width*(4/5), app.height*(3.25/5),
                       text= app.Trainer1.curr.moves[3].name, font='Arial 10 bold')

    canvas.create_line(app.width*(3.5/5),app.height*(2.5/5),app.width*(3.5/5),
    app.height*(3.5/5))

    canvas.create_line(app.width*(2.5/5),app.height*(3/5),app.width*(4.5/5),
    app.height*(3/5))

    canvas.create_rectangle(app.width*(2.5/5),app.height*(2.5/5),
    app.width*(4.5/5),app.height*(3.5/5))


    canvas.create_text(app.width*(1/5), app.height*(2/5),
                       text= 'hp', font='Arial 15 bold')
    canvas.create_text(app.width*(1/5), app.height*(1.7/5),
                       text= app.Trainer1.curr.name, font='Arial 15 bold')
    canvas.create_text(app.width*(3.7/5), app.height*(0.3/5),
                       text= 'hp', font='Arial 12 bold')
    for i in range(len(app.Trainer1.pokelist())):                   
        canvas.create_rectangle(app.width*((i+1)/7),app.height*(4/5),app.width*((i+2)/7),app.height*(4.5/5))
        canvas.create_text((app.width*((i+1)/7)+app.width*((i+2)/7))/2,app.height*(4.25/5),text= app.Trainer1.pokelist()[i].name,
        font='Arial 7 bold')

    if(app.Trainer2.teamalive == False):
        canvas.create_text(app.width/2, app.height/2.5,
                       text= f'{app.Trainer1.name} wins', font='Arial 12 bold')
    elif(app.Trainer1.teamalive == False):
        canvas.create_text(app.width/2, app.height/2.5,
                       text= f'{app.Trainer2.name} wins', font='Arial 12 bold')

    #if(app.Trainer1.curr.currhp>0 and app.allowmove == False):
     #   canvas.create_text(app.width/2, app.height*(3.5/5), text = f'{app.Trainer1.curr.name} used {app.currmove.name}' )

    #for i in range(int(50*(app.Trainer1.curr.currhp/app.Trainer1.curr.hp))):
     #   canvas.create_rectangle(i*2+30,app.height*(2/5)+25,(i+1)*2+30,
      #  app.height*(2/5)+30,fill = 'green')

    if(app.Trainer1.curr.currhp>0): #and app.allowmove == True):
        for i in range(int(50*(app.Trainer1.curr.currhp/app.Trainer1.curr.hp))):
            canvas.create_rectangle(i*2+30,app.height*(2/5)+25,(i+1)*2+30,
                    app.height*(2/5)+30,fill = 'green')

    #if(app.Trainer2.curr.currhp>0 and app.allowmove2 == False):
       # canvas.create_text(app.width/2, app.height*(3.5/5), text = f'{app.Trainer2.curr.name} used {app.currmove2.name}!' )
       # for j in range(int(50*(app.Trainer2.curr.currhp/app.Trainer2.curr.hp))):
        #    canvas.create_rectangle(app.width - (j*2+55),app.height*(1/10),app.width- 
         #   ((j+1)*2+55), app.height*(1/10)+5,fill = 'green')

    if(app.Trainer2.curr.currhp>0):        
        for j in range(int(50*(app.Trainer2.curr.currhp/app.Trainer2.curr.hp))):
                canvas.create_rectangle(app.width - (j*2+55),app.height*(1/10),app.width- 
                ((j+1)*2+55), app.height*(1/10)+5,fill = 'green')



def overworld_keyPressed(app, event):
    if (event.key == "Left"):    
        app.scrollX -= 10
        app.pos = 1
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin1(app)):
            app.scrollX+=10
    elif (event.key == "Right"): 
        app.scrollX += 10
        app.pos = 2
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin1(app)):
            app.scrollX-=10
    elif(event.key == "Up"):    
        app.scrollY +=10
        app.pos = 3
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin1(app)):
            app.scrollY-=10
    elif(event.key == "Down"):  
        app.scrollY -=10
        app.pos = 0
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin1(app)):
            app.scrollY+=10
    elif(event.key == "Enter" and app.gym[0] - app.scrollX-100<app.width/2<app.gym[0] - app.scrollX+100
        and app.gym[1]+app.scrollY-100<app.height/2<app.gym[1]+app.scrollY + 100):#magic number change later
        app.Trainer2 = Trainer2
        for a in app.Trainer2.poklist: 
                app.sprites6 = [ ]
                url = a.sprite
                app.spritestrip7 = app.loadImage(url)
                for j in range(len(a.slist)):
                    for i in range(len(a.slist[0])):
                        if(a.slist[j][i] == (0,0,0,0)):
                            continue
                        sprite = app.spritestrip7.crop((a.slist[j][i][0], a.slist[j][i][1] ,a.slist[j][i][2], a.slist[j][i][3]))
                        app.sprites6.append(sprite)
                app.spritedict2[a.name] = app.sprites6
        app.mode = 'gym'               
def overworld_timerFired(app):
    L = []
    app.count +=1
    for (cx, cy) in app.dotsgrass:
        cx -= app.scrollX  
        cy += app.scrollY
        L.append((cx,cy))
    for (cx, cy) in L:
        if((app.width-25)/2<cx and cx <(app.width+25)/2 and (app.height-25)/2< cy and cy< (app.height+25)/2 and app.count%50 == 0): #magic number change later
            print('hi')
            app.Trainer2 = Wild
            for a in app.Trainer2.poklist: 
                app.sprites6 = [ ]
                url = a.sprite
                app.spritestrip7 = app.loadImage(url)
                for j in range(len(a.slist)):
                    for i in range(len(a.slist[0])):
                        if(a.slist[j][i] == (0,0,0,0)):
                            continue
                        sprite = app.spritestrip7.crop((a.slist[j][i][0], a.slist[j][i][1] ,a.slist[j][i][2], a.slist[j][i][3]))
                        app.sprites6.append(sprite)
                app.spritedict2[a.name] = app.sprites6
            app.mode = 'battle'
            break
def ifanyin1(app):
    for (cx, cy) in app.dotstrees:
        cx -= app.scrollX
        cy +=app.scrollY
        if(circlesIntersect(cx,cy,10,app.width/2,app.height/2,10)):#magic number
            return True
        elif(app.gym[0]-app.scrollX-gymw/2<app.width/2<app.gym[0]-app.scrollX+gymw/2 and
                app.gym[1]+app.scrollY-gymh/2<app.height/2<app.gym[1]+app.scrollY+gymh/2):
            return True
    return False
def overworld_redrawAll(app, canvas):
    imgw = 400
    imgh= 260
    for i in range(math.ceil(app.width/imgw)):
        for j in range(2):
            canvas.create_image(imgw/2*(i+1), j*imgh, image=ImageTk.PhotoImage(app.spritestrip4))

    
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
    canvas.create_image(app.gym[0]-app.scrollX, app.gym[1]+app.scrollY, image=ImageTk.PhotoImage(app.spritestrip5))

    x = app.width/2
    canvas.create_text(x, 20, text='Use arrows to move left or right')
    canvas.create_text(x, 40, text=f'app.scrollX = {app.scrollX}')  #magicnumbers
    sprite = app.sprite2[app.pos][app.spriteCounter]
    cx, cy, r = app.width/2, app.height/2, 10
    canvas.create_image(cx, cy, image=ImageTk.PhotoImage(sprite))

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
            if(isin(cx,cy,roomsize) == False or depth != 2):
                ls.append([cx,cy,roomsize,depth])
                BSPTree(width//2,height,depth+1,vorh+1)
            if(isin(cx2,cy,roomsize) == False or depth !=2):
                ls.append([cx2,cy,roomsize,depth])
                BSPTree(width,height,depth+1,vorh+1)
        elif(vorh%2 == 1):
            cx = random.randint(0,width)
            cy = random.randint(0,height//2)
            cy2 = random.randint(height//2,height)
            roomsize = random.randint(50,100)
            if(isin(cx,cy,roomsize) == False or depth !=2):
                ls.append([cx,cy,roomsize,depth])
                BSPTree(width,height//2,depth+1,vorh+1)
            if(isin(cx,cy2,roomsize) == False or depth !=2):
                ls.append([cx,cy2,roomsize,depth])
                BSPTree(width,height,depth+1,vorh+1)

            

def gym_keyPressed(app, event):
    if (event.key == "Left"):    
        app.scrollX2 -= 5
        app.pos = 1
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app) == False):
            app.scrollX2+=5
    elif (event.key == "Right"): 
        app.scrollX2 += 5
        app.pos = 2
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app) == False):
            app.scrollX2-=5
    elif(event.key == "Up"):    
        app.scrollY2 +=5
        app.pos = 3
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app)== False):
            app.scrollY2-=5
    elif(event.key == "Down"):  
        app.scrollY2 -=5
        app.pos = 0
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])
        if(ifanyin(app) == False):
            app.scrollY2+=5
def ifanyin(app):
    best = 10000000
    cx2 = None
    for (cx, cy,roomsize,depth) in ls:
        x = ls.index([cx,cy,roomsize,depth])+1
        cx -= app.scrollX2
        cy +=app.scrollY2
        if(depth == 2):
            if(x<len(ls)-1):
                for j in range(x,len(ls)):
                    if(j<len(ls) and ls[j][3] == 2):
                        (cx2,cy3,roomsize2, depth2) = ls[j]
                        cx2 -=app.scrollX2
                        cy3 +=app.scrollY2
                       
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
def gym_timerFired(app):
    if(app.gymx-app.scrollX2-25<app.cx<app.gymx + app.scrollX2+25 and 
    app.gymy+app.scrollY2-25 < app.cy<app.gymy+app.scrollY2 + 25 ):
        app.mode = 'battle'

def gym_redrawAll(app, canvas):
    thickness = 5
    canvas.create_rectangle(0,0,app.width,app.height,fill = 'black')
    alreadin = []
    for (cx,cy,roomsize,depth) in ls:
        if(depth == 2):
            x = ls.index([cx,cy,roomsize,depth])+1
            cx-=app.scrollX2
            cy += app.scrollY2
            
            canvas.create_rectangle(cx - (roomsize/2),cy-(roomsize/2),cx + (roomsize/2), cy + (roomsize/2),fill= 'green')
            
            for j in range(x,len(ls)):
                if(j<len(ls) and ls[j][3] == 2):
                    canvas.create_rectangle(ls[j][0] + ls[j][2]/2-app.scrollX2,cy - thickness,cx + roomsize/2, cy +thickness,fill = 'blue')
                    canvas.create_rectangle(ls[j][0] + ls[j][2]/2-app.scrollX2- thickness,ls[j][1]  +ls[j][2]/2+app.scrollY2,ls[j][0] + ls[j][2]/2 + thickness - app.scrollX2,cy,fill = 'blue')
                    alreadin.append(j)

    x = app.width/2
    canvas.create_text(x, 20, text='Use arrows to move left or right')
    canvas.create_text(x, 40, text=f'app.scrollX = {app.scrollX}')
    sprite = app.sprite2[app.pos][app.spriteCounter]
    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(sprite))
    canvas.create_image(app.gymx-app.scrollX2, app.gymy+app.scrollY2, image=ImageTk.PhotoImage(app.spritestrip6))


runApp(width=500, height=302)



'''
def appStarted(app):
    url = 'Sprites/Tepigfront.png'
    app.spritestrip2 = app.loadImage(url)
    app.temp = [ ]
    app.sprites2 = []
    app.pos = 0
    slist = [[[0,0,60,60],[60,0,135,60],[135,0,210,60],[210,0,285,60],[285,0,360,60],[360,0,435,60],[435,0,510,60]]
 ,        [[0,60,60,120],[75,60,135,120],[135,60,210,120],[210,60,285,120],[285,60,360,120],[360,60,435,120],[435,60,510,120]]  ,
           [[0,120,60,180],[60,120,135,180],[135,120,210,1800],[210,120,285,180],[285,120,360,180],[360,120,435,180],[435,120,510,180]]     ]
    for j in range(len(slist)):
            for i in range(len(slist[0])):
                if(slist[j][i] == (0,0,0,0)):
                    continue
                sprite = app.spritestrip2.crop((slist[j][i][0], slist[j][i][1] ,slist[j][i][2], slist[j][i][3]))
                app.sprites2.append(sprite)
    
    
    app.spriteCounter = 0

def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites2)

def redrawAll(app, canvas):
    sprite = app.sprites2[app.spriteCounter]
    canvas.create_image(250, 200, image=ImageTk.PhotoImage(sprite))
    #canvas.create_image(200, 200, image=ImageTk.PhotoImage(app.spritestrip))
    canvas.create_line(510,0,510,400)
    canvas.create_line(0,100,1000,100)
runApp(width=400, height=400)





#slist = [[[0,0,60,100],[60,0,135,100],[135,0,210,100],[210,0,285,100],[285,0,360,100],[360,0,435,100],[435,0,510,100]]
# ,        [[0,100,60,200],[60,100,135,200],[135,100,210,200],[210,100,285,200],[285,100,360,200],[360,100,435,200],[435,100,510,200]]  ,
#           [[0,200,60,300],[60,200,135,300],[135,200,210,300],[210,200,285,300],[285,200,360,300],[360,200,435,300],[435,200,510,300]]     ]

'''


from Pokemon import*
from cmu_112_graphics import*
from Gameai import*
import math

gymw = 250
gymh = 135
battleimgshift = 50
ls = []
deep = 3
def distance(x1, y1, x2, y2):
    x = ((x2-x1)**2 + (y2-y1)**2)**0.5  # used formula
    return x


def circlesIntersect(x1, y1, r1, x2, y2, r2):
    x = distance(x1,y1,x2,y2)
    result = (x <= r1+r2)
    return result

def appStarted(app):
    app.mode = 'startscreen'
    app.counter = 0
    app.Trainer1 = Trainer1
    app.Trainer2 = Trainer2
    app.Poke1col = 'green'
    app.Poke2col = 'green'
    app.count = 0
    app.currmove = None
    app.currmove2 = None
    app.pokeswitch = None
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

    #generates players pokemon spritres
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

    app.spriteCounter1 = 0
    app.spriteCounter2 = 0
    app.scrollY = 0
    app.scrollX = 0
    app.dotsgrass = []
    #generates grass position
    for j in range(4):
       for i in range(app.width//24):
          app.dotsgrass.append((i*24,-300 + j*21))
    app.dotstrees = [(random.randrange(app.width*(3/4),app.width),
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
    #overworld player sprite
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
    BSPTree((0,app.width),(0,app.height),0,0)
    count = 0
    #intializes position of player and gym leader     
    app.cx, app.cy= ls[0][0],ls[0][1]          
    app.gymx,app.gymy = ls[len(ls)-1][0],ls[len(ls)-1][1]        
    #scroll variables for the gym
    app.scrollX2 = 0
    app.scrollY2 = 0
    app.Turn = 0
    #for the start screen
    app.poketext = app.loadImage('Sprites/Pokemon start screen.png')
    app.pokeback = app.loadImage('Sprites/Startscreen.jpg')
    app.axolotal = app.loadImage('Sprites/axolotl.png')
def battle(app,Trainer1s,Trainer2s):
            moveai = ai(Trainer2s,Trainer1s)
            app.currmove2 = moveai
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
                    return
                if(type(moveai) != str):
                    app.currmove2 = moveai
                    damages2 = damage(Pokemon2,Pokemon1,moveai)
                    Pokemon1.currhp -= damages2
            else:
                if(type(moveai) != str):
                    damages2 = damage(Pokemon2,Pokemon1,moveai)
                    Pokemon1.currhp -= damages2
                if(Pokemon1.currhp<0):
                    return
                if(app.currmove != 'switch'):
                    damages = damage(Pokemon1,Pokemon2,app.currmove)
                    Pokemon2.currhp -=damages

def battle_timerFired(app):
    if( (app.Trainer1.teamalive() and app.Trainer2.teamalive()) and (app.allowmoves)): 
        battle(app,app.Trainer1,app.Trainer2)
        app.allowmoves = False
        app.Turn+=1
        app.count +=1
    #generates sprites
    app.spriteCounter1 = (1 + app.spriteCounter1) % len(app.spritesdict[app.Trainer1.curr.name])
    app.spriteCounter2 = (1 + app.spriteCounter2) % len(app.spritedict2[app.Trainer2.curr.name])
    #switch if dead 
    if(app.Trainer2.curr.currhp<=0):
        for i in range(len(app.Trainer2.pokelist())):
            if(app.Trainer2.pokelist()[i].currhp>0):
                app.Trainer2.curr  = app.Trainer2.pokelist()[i]
                app.spriteCounter2 = 0
                app.currmove2 = f'died switched to {app.Trainer2.curr.name}'
                break
    if(app.Trainer1.curr.currhp<=0):
        for i in range(len(app.Trainer1.pokelist())):
            if(app.Trainer1.pokelist()[i].currhp>0):
                Trainer1.curr  = app.Trainer1.pokelist()[i]
                app.spriteCounter1 = 0
                app.currmove = f'died switched to {app.Trainer1.curr.name}'
                break
    #if one of the players lose this finishes the game
    if(app.Trainer2.teamalive() == False or app.Trainer1.teamalive() == False):
        app.Trainer2.restoreall()
        app.Trainer1.restoreall()
        app.Turn = 0
        if(app.Trainer2.name == 'Bob'):
            app.mode = 'victory'
        else:
            app.mode = 'overworld'
        
    
      
def battle_mousePressed(app, event):
        #checks to see if I clicked on a move or switch out 
        if(event.x>(2/5)*app.width and event.x<(3/5)*app.width and 
            event.y>(2.5/5)*app.height and event.y<(3/5)*app.height ):
            app.allowmoves = True
            app.currmove = app.Trainer1.curr.moves[0]
        elif(event.x>(3/5)*app.width and event.x<(4/5)*app.width and  
            event.y>(2.5/5)*app.height and event.y<(3/5)*app.height ):
            app.allowmoves = True
            app.currmove = app.Trainer1.curr.moves[1]
        elif(event.x>(2/5)*app.width and event.x<(3/5)*app.width and  
            event.y>(3/5)*app.height and event.y<(3.5/5)*app.height ):
            app.allowmoves = True
            app.currmove = app.Trainer1.curr.moves[2]
        elif(event.x>(3/5)*app.width and event.x<(4/5)*app.width and  
            event.y>(3/5)*app.height and event.y<(3.5/5)*app.height ):
            app.allowmoves = True
            app.currmove = app.Trainer1.curr.moves[0]
        elif(event.x>(1/7)*(app.width-app.width*(1/6)) and event.x<(2/7)*(app.width-app.width*(1/6)) and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[0].currhp >0):
            app.pokeswitch = app.Trainer1.pokelist()[0]
            app.allowmoves = True
            app.currmove = 'switch'
        elif(event.x>(2/7)*(app.width-app.width*(1/6)) and event.x<(3/7)*(app.width-app.width*(1/6)) and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[1].currhp >0):
            app.pokeswitch = app.Trainer1.pokelist()[1]
            app.allowmoves = True
            app.currmove = 'switch'
        elif(event.x>(3/7)*(app.width-app.width*(1/6)) and event.x<(4/7)*(app.width-app.width*(1/6)) and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[2].currhp >0):
            app.pokeswitch = app.Trainer1.pokelist()[2]
            app.allowmoves = True
            app.currmove = 'switch'
        elif(event.x>(4/7)*(app.width-app.width*(1/6)) and event.x<(5/7)*(app.width-app.width*(1/6)) and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[3].currhp >0):
            app.pokeswitch = app.Trainer1.pokelist()[3]
            app.allowmoves = True
            app.currmove = 'switch'
        elif(event.x>(4/7)*(app.width-app.width*(1/6)) and event.x<(5/7)*(app.width-app.width*(1/6)) and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[4].currhp >0):
            app.pokeswitch = app.Trainer1.pokelist()[4]
            app.allowmoves = True
            app.currmove = 'switch'
        app.counter += 1
    
def battle_redrawAll(app, canvas):
    #Draws background
    canvas.create_image(app.width/2-battleimgshift,app.height/2,image=ImageTk.PhotoImage(app.sprite8))
    #Draws sprites
    sprite = app.spritesdict[app.Trainer1.curr.name][app.spriteCounter1]
    sprite2 = app.spritedict2[app.Trainer2.curr.name][app.spriteCounter2]
    canvas.create_image(app.width*(95/400), app.height*(300/400), image=ImageTk.PhotoImage(sprite))
    canvas.create_image(app.width*(2.5/4), app.height*(1.7/4), image=ImageTk.PhotoImage(sprite2))
    #Draws move box
    canvas.create_text(app.width*(3/5), app.height*(2.3/5),
                       text= 'Moves', font='Arial 12 bold')
    canvas.create_text(app.width*(2.5/5), app.height*(2.75/5),
                       text= app.Trainer1.curr.moves[0].name, font='Arial 10 bold')

    canvas.create_text(app.width*(3.5/5), app.height*(2.75/5),
                       text= app.Trainer1.curr.moves[1].name, font='Arial 10 bold')

    canvas.create_text(app.width*(2.5/5), app.height*(3.25/5),              
                       text= app.Trainer1.curr.moves[2].name, font='Arial 10 bold')

    canvas.create_text(app.width*(3.5/5), app.height*(3.25/5),
                       text= app.Trainer1.curr.moves[3].name, font='Arial 10 bold')

    canvas.create_line(app.width*(3/5),app.height*(2.5/5),app.width*(3/5),
    app.height*(3.5/5))

    canvas.create_line(app.width*(2/5),app.height*(3/5),app.width*(4/5),
    app.height*(3/5))

    canvas.create_rectangle(app.width*(2/5),app.height*(2.5/5),
    app.width*(4/5),app.height*(3.5/5))


    canvas.create_text(app.width*(1/5), app.height*(2/5),
                       text= 'hp', font='Arial 15 bold')
    canvas.create_text(app.width*(1/5), app.height*(1.7/5),
                       text= app.Trainer1.curr.name, font='Arial 15 bold')
    canvas.create_text(app.width*(3.5/5), app.height*(0.7/5),
                       text= 'hp', font='Arial 12 bold')
     #draws switch boxes at the bottom
    for i in range(len(app.Trainer1.pokelist())):                   
        canvas.create_rectangle((app.width-app.width*(1/6))*((i+1)/7),app.height*(4/5),(app.width-app.width*(1/6))*((i+2)/7),app.height*(4.5/5))
        canvas.create_text(((app.width-app.width*(1/6))*((i+1)/7)+(app.width-app.width*(1/6))*((i+2)/7))/2,app.height*(4.25/5),text= app.Trainer1.pokelist()[i].name,
        font='Arial 7 bold')   

    #draw player health bar
    if(app.Trainer1.curr.currhp>0): 
        for i in range(int(50*(app.Trainer1.curr.currhp/app.Trainer1.curr.hp))):
            canvas.create_rectangle(i*2+30,app.height*(2/5)+25,(i+1)*2+30,
                    app.height*(2/5)+30,fill = 'green')

  
    #draws enemy health bar   
    if(app.Trainer2.curr.currhp>0):     
        for j in range(int(50*(app.Trainer2.curr.currhp/app.Trainer2.curr.hp))):
                canvas.create_rectangle(app.width-app.width/10 - (j*2+55),app.height*(1.6/10),app.width-app.width/10- 
                ((j+1)*2+55), app.height*(1.6/10)+5,fill = 'green')
    #Draws what move is being used
    if(app.Turn>= 1):
        canvas.create_text(app.width*(4.5/5),app.height*(1.5/5),text = f'Turn: {app.Turn}',font='Arial 7 bold')
    
        if(type(app.currmove)!= str and type(app.currmove2) != str):

            canvas.create_text(app.width*(4.5/5),app.height*(2/5),text = f'{app.Trainer1.curr.name} used {app.currmove.name}',font='Arial 7 bold')
            canvas.create_text(app.width*(4.5/5),app.height*(2.5/5),text = f'{app.Trainer2.curr.name} used {app.currmove2.name}',font='Arial 7 bold')

        elif(type(app.currmove)!= str and (type(app.currmove2) == str) and app.currmove2 !=f'died switched to {app.Trainer2.curr.name}'):

            canvas.create_text(app.width*(4.5/5),app.height*(2/5),text = f'{app.Trainer1.curr.name} used {app.currmove.name}',font='Arial 7 bold')
            canvas.create_text(app.width*(4.5/5),app.height*(2.5/5),text = f'{app.Trainer2.name} switched to  {app.Trainer2.curr.name}',font='Arial 7 bold')

        elif(type(app.currmove)!= str and (type(app.currmove2) == str) and app.currmove2 ==f'died switched to {app.Trainer2.curr.name}'):

            canvas.create_text(app.width*(4.5/5),app.height*(2/5),text = f'{app.Trainer1.curr.name} used {app.currmove.name}',font='Arial 7 bold')
            canvas.create_text(app.width*(4.5/5),app.height*(2.5/5),text = app.currmove2,font='Arial 7 bold')

        elif(type(app.currmove)== str and (type(app.currmove2) != str) and app.currmove ==f'died switched to {app.Trainer1.curr.name}'):
            canvas.create_text(app.width*(4.5/5),app.height*(2.5/5),text = f'{app.Trainer2.curr.name} used {app.currmove2.name}',font='Arial 7 bold')
            canvas.create_text(app.width*(4.5/5),app.height*(2/5),text = app.currmove,font='Arial 7 bold')

        elif(type(app.currmove)== str and (type(app.currmove2) != str) and app.currmove !=f'died switched to {app.Trainer1.curr.name}'):

            canvas.create_text(app.width*(4.5/5),app.height*(2.5/5),text = f'{app.Trainer2.curr.name} used {app.currmove2.name}',font='Arial 7 bold')
            canvas.create_text(app.width*(4.5/5),app.height*(2/5),text = f'{app.Trainer1.name} switched to  {app.Trainer1.curr.name}',font='Arial 7 bold')



def overworld_keyPressed(app, event):
    #adjusts the player sprite and scrollX/Y which shifts the enviroment
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
    #Checks if I'm near the gym and if I clicked enter
    #Also Refills the spritedic for the enemy 
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
        app.mode = 'gymscreen'               
def overworld_timerFired(app):
    L = []
    app.count +=1
    for (cx, cy) in app.dotsgrass:
        cx -= app.scrollX  
        cy += app.scrollY
        L.append((cx,cy))
    #If I'm in grass once every 25 calls of timerfired I will get an encounter 
    for (cx, cy) in L:
        if((app.width-25)/2<cx and cx <(app.width+25)/2 and (app.height-25)/2< cy and cy< (app.height+25)/2 and app.count%25 == 0): 
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
#checks if the player is in any trees
def ifanyin1(app):
    for (cx, cy) in app.dotstrees:
        cx -= app.scrollX
        cy +=app.scrollY
        if(circlesIntersect(cx,cy,10,app.width/2,app.height/2,10)):
            return True
        elif(app.gym[0]-app.scrollX-gymw/2<app.width/2<app.gym[0]-app.scrollX+gymw/2 and
                app.gym[1]+app.scrollY-gymh/2<app.height/2<app.gym[1]+app.scrollY+gymh/2):
            return True
    return False
def overworld_redrawAll(app, canvas):
    imgw = 400
    imgh= 260
    #Draws light green background
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
    canvas.create_text(x, 20, text='Use arrows to move') 
    sprite = app.sprite2[app.pos][app.spriteCounter]
    cx, cy = app.width/2, app.height/2
    canvas.create_image(cx, cy, image=ImageTk.PhotoImage(sprite))

def isin(cx,cy,roomsize):
    for i in ls:
        if((i[0]-i[2]/2)<cx+roomsize/2 and (i[0]+i[2]/2)>cx-roomsize/2 and (i[1] -i[2]/2)<cy+roomsize/2 and (i[1]+i[2]/2)>cy-roomsize/2):
            return True
    return False

#Uses binary space partioning to create rooms
#centers of the rooms and size are randomly generated within a certain range and
#added to a list
def BSPTree(width,height,depth,vorh):   
    if(depth == deep+1):
        return 
    else:
        if(vorh%2 == 0):
            cx = random.randint(width[0],width[1])
            cx2 = random.randint(width[1]//2,width[1])
            cy = random.randint(height[0],height[1])
            roomsize = random.randint(50,100)
            if(isin(cx,cy,roomsize) == False):
                ls.append([cx,cy,roomsize,depth])
                BSPTree((0,width[1]//2),height,depth+1,vorh+1)
            if(isin(cx2,cy,roomsize) == False):
                ls.append([cx2,cy,roomsize,depth])
                BSPTree((width[1]//2,width[1]),height,depth+1,vorh+1)
        elif(vorh%2 == 1):            
            cx = random.randint(width[0],width[1])
            cy = random.randint(height[0],height[1]//2)
            cy2 = random.randint(height[1]//2,height[1])
            roomsize = random.randint(50,100)
            if(isin(cx,cy,roomsize) == False):
                ls.append([cx,cy,roomsize,depth])
                BSPTree(width,(height[0],height[1]//2),depth+1,vorh+1)
            if(isin(cx,cy2,roomsize) == False):
                ls.append([cx,cy2,roomsize,depth])
                BSPTree(width,(height[1]//2,height[1]),depth+1,vorh+1)
           

def gym_keyPressed(app, event):
    #adjusts the player sprite and scrollX/Y which shifts the enviroment
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
#Checks to see if the charecter is within the rooms or within the 
#set paths
def ifanyin(app):
    cx2 = None
    for (cx, cy,roomsize,depth) in ls:
        x = ls.index([cx,cy,roomsize,depth])+1
        cx -= app.scrollX2
        cy +=app.scrollY2
        if((cx-roomsize/2<app.cx<cx+roomsize/2 and cy-roomsize/2<app.cy<cy+roomsize/2)):
            return True
        if(x<=len(ls)-1):
                
                        (cx2,cy3,roomsize2, depth2) = ls[x]
                        cx2 -=app.scrollX2
                        cy3 +=app.scrollY2
                       
                        if(cx2>cx):
                            if(cx<app.cx<cx2 and (cy-5<app.cy<cy+5 or cy3-5<app.cy<cy3+5)):
                                return True
                        elif(cx>cx2):
                            if(cx2<app.cx<cx and (cy-5<app.cy<cy+5 or cy3-5<app.cy<cy3+5)):
                                return True
                        if(cy3>cy):
                            if(cy<app.cy<cy3 and (cx2-5<app.cx<cx2+5 or cx-5<app.cx<cx+5)):
                                return True
                        elif(cy>cy3):
                            if(cy3<app.cy<cy and (cx2-5<app.cx<cx2+5 or cx-5<app.cx<cx+5)):
                                return True
    
    return False   
  #Checks if I'm near the gym leader 
def gym_timerFired(app):
    if(app.gymx-app.scrollX2-25<app.cx<app.gymx - app.scrollX2+25 and 
    app.gymy+app.scrollY2-25 < app.cy<app.gymy+app.scrollY2 + 25 ):
        app.mode = 'battle'

def gym_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill = 'black')
    #draws square rooms
    for (cx,cy,roomsize,depth) in ls:
            cx-=app.scrollX2
            cy += app.scrollY2
            
            canvas.create_rectangle(cx - (roomsize/2),cy-(roomsize/2),cx + (roomsize/2), cy + (roomsize/2),fill= 'green')
            #player sprite
    sprite = app.sprite2[app.pos][app.spriteCounter]
    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(sprite))
    #gym laeder
    canvas.create_image(app.gymx-app.scrollX2, app.gymy+app.scrollY2, image=ImageTk.PhotoImage(app.spritestrip6))
#start screen
def startscreen_keyPressed(app,event):
    if(event.key == 'Enter'):
        app.mode = 'overworld'
def startscreen_redrawAll(app,canvas):
     canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.pokeback))
     canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.poketext))
     canvas.create_text(app.width/2, app.height*(3/4),text = 'The Maximum', font = 'Arial 30')
     canvas.create_text(app.width/2, app.height*(3.5/4),text = 'Press enter to continue')
#Instruction screen for gym
def gymscreen_keyPressed(app,event):
    if(event.key == 'Enter'):
        app.mode = 'gym'
def gymscreen_redrawAll(app,canvas):
     canvas.create_text(app.width/2, app.height/2,text = 'Just a quick gym tip:')
     canvas.create_text(app.width/2, app.height*(2.5/4),text = 'This gym has randomly generated tiles with paths connecting ')
     canvas.create_text(app.width/2, app.height*(2.7/4),text = 'however these paths arent highlighted so it is up to you to ')
     canvas.create_text(app.width/2, app.height*(3/4),text = 'find them and use the paths to guide yourself to the gym leader')
     canvas.create_text(app.width/2, app.height*(3.2/4),text = 'PS: Once you figure out the pattern they are pretty to find')
     canvas.create_text(app.width/2, app.height*(3.5/4),text = 'Press Enter to continue')
 #screen when you beat gym leader    
def victory_keyPressed(app,event):
    if(event.key == 'Enter'):
        app.mode = 'overworld'
def victory_redrawAll(app,canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.axolotal))
    canvas.create_text(app.width/2, app.height/2,text = f'Congratulations you beat gym leader {app.Trainer2.name}')
    canvas.create_text(app.width/2, app.height*(3.5/4),text = 'Press Enter to continue')
    

runApp(width=500, height=302)



'''
def appStarted(app):
    url = 'Sprites/Victini back.png'
    app.spritestrip2 = app.loadImage(url)
    app.temp = [ ]
    app.sprites2 = []
    app.pos = 0
    slist =  [[[0,0,55,70],[95,0,145,70],[195,0,245,70],[285,0,335,70],[375,0,435,70],[475,0,525,70]],
          [[0,70,55,140],[95,70,145,140],[195,70,245,140],[285,70,335,140],[375,70,435,140],[475,70,525,140]],
              [[0,140,55,230],[95,140,145,230],[195,140,245,230],[285,140,335,230],[375,140,435,230],[475,140,525,230]],
                  [[0,230,55,310],[95,230,145,310],[195,230,245,310],[285,230,335,310],[0,0,0,0],[0,0,0,0]]]
    for j in range(len(slist)):
            for i in range(len(slist[0])):
                if(slist[j][i] == [0,0,0,0] or slist[j][i] == (0,0,0,0)):
                    continue
                sprite = app.spritestrip2.crop((slist[j][i][0], slist[j][i][1] ,slist[j][i][2], slist[j][i][3]))
                app.sprites2.append(sprite)
    
    
    app.spriteCounter = 0

def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites2)

def redrawAll(app, canvas):
    sprite = app.sprites2[app.spriteCounter]
    canvas.create_image(250, 200, image=ImageTk.PhotoImage(sprite))

    #canvas.create_image(200, 200, image=ImageTk.PhotoImage(app.spritestrip2))
    canvas.create_line(510,0,510,400)
    canvas.create_line(0,100,1000,100)
runApp(width=400, height=400)





#slist = [[[0,0,40,50],[80,0,130,50],[180,0,230,50],[270,0,320,50],[360,0,420,50],[460,0,510,50]],
#           [[0,50,40,100],[80,50,130,100],[180,50,230,100],[270,50,320,100],[360,50,420,100],[460,50,510,100]],
#               [[0,100,40,150],[80,100,130,150],[180,100,230,150],[270,100,320,150],[360,100,420,150],[460,100,510,150]],
#                   [[0,100,40,150],[80,100,130,150],[180,100,230,150],[270,100,320,150],[0,0,0,0],[0,0,0,0]]]


'''
from Pokemon import*
from cmu_112_graphics import*
from Gameai import*
def appStarted(app):
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

def battle(app,Trainer1s,Trainer2s):
            
            moveai = ai(Trainer2s,Trainer1s)
            print(moveai.name)
            Pokemon1 = Trainer1s.curr
            Pokemon2 = Trainer2s.curr   
            if(app.currmove == 'switch'):
                Trainer1s.curr = app.pokeswitch
            if(type(moveai) == string):
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
                if(type(moveai) != string):
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
#def keyPressed(app,event):
#    if(event.key == 'k' and app.allowmove == False):
#        app.allowmove == True
#        app.allowmove2 == False
#    elif(event.key == 'k' and app.allowmove == True and app.allowmove2 == False):
#        app.allowmove2 == True
def timerFired(app):
    if( (app.Trainer1.teamalive and app.Trainer2.teamalive) and (app.allowmoves)): 
        battle(app,app.Trainer1,app.Trainer2)
        app.allowmove = False
        app.allowmoves = False
        
        app.count +=1
    app.spriteCounter1 = (1 + app.spriteCounter1) % len(app.spritesdict[app.Trainer1.curr.name])
    app.spriteCounter2 = (1 + app.spriteCounter2) % len(app.spritedict2[app.Trainer2.curr.name])
    if(Trainer2.curr.currhp<=0):
        for i in range(len(app.Trainer2.pokelist())):
            if(app.Trainer2.pokelist()[i].currhp>0):
                Trainer2.curr  = app.Trainer2.pokelist()[i]
                app.spriteCounter2 = 0
                break
    if(Trainer1.curr.currhp<=0):
        for i in range(len(app.Trainer1.pokelist())):
            if(app.Trainer1.pokelist()[i].currhp>0):
                Trainer1.curr  = app.Trainer1.pokelist()[i]
                app.spriteCounter1 = 0
                break
    
      
def mousePressed(app, event):
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
    
def redrawAll(app, canvas):#make a variable that is initally set false until I attack and then when it is true set write a statement that I used move x lower the hp and for the next player have it begin only when I click enter
    sprite = app.spritesdict[app.Trainer1.curr.name][app.spriteCounter1]
    sprite2 = app.spritedict2[app.Trainer2.curr.name][app.spriteCounter2]
    canvas.create_image(75, 250, image=ImageTk.PhotoImage(sprite))
    canvas.create_image(300, 100, image=ImageTk.PhotoImage(sprite2))
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

runApp(width=400, height=400)
'''

def appStarted(app):
    url = 'Sprites/boy_run_1.png'
    app.spritestrip = app.loadImage(url)
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

def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite2[app.pos])

def redrawAll(app, canvas):
    sprite = app.sprite2[0][app.spriteCounter]
    canvas.create_image(300, 300, image=ImageTk.PhotoImage(sprite))
    #canvas.create_image(200, 200, image=ImageTk.PhotoImage(app.spritestrip))
    canvas.create_line(260,0,260,400)
    canvas.create_line(0,100,1000,100)
runApp(width=400, height=400)




def appStarted(app):
    url = 'Sprites/Grass.png'
    app.spritestrip = app.loadImage(url)
    app.sprites = [ ]
    url2 = 'Sprites/Grass 2.png'
    app.spritestrip2 = app.loadImage(url2)

    app.sprite = app.spritestrip.crop((30,0,55,30))
               
    
    
    app.spriteCounter = 0

def timerFired(app):
   return

def redrawAll(app, canvas):
    canvas.create_image(300, 300, image=ImageTk.PhotoImage(app.spritestrip2))
    canvas.create_image(500, 200, image=ImageTk.PhotoImage(app.spritestrip))
    canvas.create_line(105,0,105,400)
    #canvas.create_line(0,300,1000,300)
runApp(width=400, height=400)


#slist = [[(65,100,155,200),(165,100,255,200),(260,100,345,200),(360,100,440,200),(455,100,535,200),(550,100,635,200),(650,100,730,200),(745,100,825,200),(845,100,935,200)],
#           [(65,200,155,300)]]


'''


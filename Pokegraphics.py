from Pokemon import*
from cmu_112_graphics import*

def appStarted(app):
    app.counter = 0
    app.Trainer1 = Trainer1
    app.Trainer2 = Trainer2
    app.Poke1col = 'green'
    app.Poke2col = 'green'
    app.allowmove = False 
    app.count = 0
    app.currmove = None
    app.pokeswitch = None
    #for sprite drawing
    url = 'Sprites/Garchomp back.png'
    app.spritestrip = app.loadImage(url)
    app.sprites = [ ]
    app.spritesdict = {}
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
    app.spriteCounter = 0

def battle(app,Trainer1s,Trainer2s):
            Pokemon1 = Trainer1s.curr
            Pokemon2 = Trainer2s.curr
            if(app.currmove == 'switch'):
                Trainer1s.curr = app.pokeswitch
            if(Pokemon1.currspeed>Pokemon2.currspeed):
                if(app.currmove != 'switch'):
                    damages = damage(Pokemon1,Pokemon2,app.currmove)
                    Pokemon2.currhp -=damages
                if(Pokemon2.currhp<0):
                    print(f'{Pokemon1.name} wins')
                    return
                x = random.randint(0,3)
                move2 = Pokemon2.moves[x]
                damages2 = damage(Pokemon2,Pokemon1,move2)
                Pokemon1.currhp -= damages2
            else:
                x = random.randint(0,3)
                move2 = Pokemon2.moves[x]
                damages2 = damage(Pokemon2,Pokemon1,move2)
                Pokemon1.currhp -= damages2
                if(Pokemon1.currhp<0):
                    print(f'{Pokemon2.name} wins')
                    return
                if(app.currmove != 'switch'):
                    damages = damage(Pokemon1,Pokemon2,app.currmove)
                    Pokemon2.currhp -=damages
def timerFired(app):
    if( (app.Trainer1.teamalive and app.Trainer2.teamalive) and (app.allowmove)): 
        battle(app,app.Trainer1,app.Trainer2)
        app.allowmove = False
    app.spriteCounter = (1 + app.spriteCounter) % len(app.spritesdict[app.Trainer1.curr.name])
    if(Trainer2.curr.currhp<=0):
        for i in range(len(app.Trainer2.pokelist())):
            if(app.Trainer2.pokelist()[i].currhp>0):
                Trainer2.curr  = app.Trainer2.pokelist()[i]
                break
    if(Trainer1.curr.currhp<=0):
        for i in range(len(app.Trainer1.pokelist())):
            if(app.Trainer1.pokelist()[i].currhp>0):
                Trainer1.curr  = app.Trainer1.pokelist()[i]
                break
    
      
def mousePressed(app, event):
    app.count+=1    #What I need to do: If my Pokemon is dead let me switch for free
    if(event.x>(2.5/5)*app.width and event.x<(3.5/5)*app.width and #and if enemy is dead 
        event.y>(2.5/5)*app.height and event.y<(3/5)*app.height ):
        app.allowmove = True
        app.currmove = app.Trainer1.curr.moves[0]
    elif(event.x>(3.5/5)*app.width and event.x<(4.5/5)*app.width and  
        event.y>(2.5/5)*app.height and event.y<(3/5)*app.height ):
        app.allowmove = True
        app.currmove = app.Trainer1.curr.moves[1]
    elif(event.x>(2.5/5)*app.width and event.x<(3.5/5)*app.width and  
        event.y>(3/5)*app.height and event.y<(3.5/5)*app.height ):
        app.allowmove = True
        app.currmove = app.Trainer1.curr.moves[2]
    elif(event.x>(3.5/5)*app.width and event.x<(4.5/5)*app.width and  
        event.y>(3/5)*app.height and event.y<(3.5/5)*app.height ):
        app.allowmove = True
        app.currmove = app.Trainer1.curr.moves[0]
    elif(event.x>(1/7)*app.width and event.x<(2/7)*app.width and event.y>(4/5)*app.height and event.y<app.height*(4.5/5) and app.Trainer1.pokelist()[0].currhp >0):
        app.pokeswitch = app.Trainer1.pokelist()[0]
        app.allowmove = True
        app.currmove = 'switch'
    app.counter += 1
    app.count +=1
    
def redrawAll(app, canvas):
    sprite = app.spritesdict[app.Trainer1.curr.name][app.spriteCounter]
    canvas.create_image(75, 250, image=ImageTk.PhotoImage(sprite))
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

    canvas.create_rectangle(app.width-50,50,app.width-app.width*(2/5), 
    app.height//3,fill = app.Poke2col)

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
    if(app.Trainer1.curr.currhp>0):
        for i in range(int(50*(app.Trainer1.curr.currhp/app.Trainer1.curr.hp))):
            canvas.create_rectangle(i*2+30,app.height*(2/5)+25,(i+1)*2+30,
            app.height*(2/5)+30,fill = 'green')
    if(app.Trainer2.curr.currhp>0):
        for j in range(int(50*(app.Trainer2.curr.currhp/app.Trainer2.curr.hp))):
            canvas.create_rectangle(app.width - (j*2+55),app.height*(1/10),app.width- 
            ((j+1)*2+55), app.height*(1/10)+5,fill = 'green')

runApp(width=400, height=400)

'''
def appStarted(app):
    url = 'Sprites/Zapdos front.png'
    app.spritestrip = app.loadImage(url)
    app.sprites = [ ]
    
    slist = [[(5,0,95,100),(105,0,195,100),(195,0,285,100),(300,0,380,100),(490,0,560,100),(585,0,665,100),(690,0,760,100),(785,0,860,100)],
           [(5,100,95,200),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0)]]
    for j in range(len(slist)):
            for i in range(len(slist[0])):
                if(slist[j][i] == (0,0,0,0)):
                    continue
                sprite = app.spritestrip.crop((slist[j][i][0], slist[j][i][1] ,slist[j][i][2], slist[j][i][3]))
                app.sprites.append(sprite)
    
    
    app.spriteCounter = 0

def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)

def redrawAll(app, canvas):
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(300, 300, image=ImageTk.PhotoImage(sprite))
    canvas.create_image(500, 200, image=ImageTk.PhotoImage(app.spritestrip))
    canvas.create_line(105,0,105,400)
    #canvas.create_line(0,300,1000,300)
runApp(width=400, height=400)


#slist = [[(65,100,155,200),(165,100,255,200),(260,100,345,200),(360,100,440,200),(455,100,535,200),(550,100,635,200),(650,100,730,200),(745,100,825,200),(845,100,935,200)],
#           [(65,200,155,300)]]



'''

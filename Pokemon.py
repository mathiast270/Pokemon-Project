import time 
import sys
import random
from cmu_112_graphics import*
from moves import*

def delay(t):
    for x in range(t):
        print(x)
        sys.stdout.flush()
        time.sleep(1)

class Pokemon(object):
    def __init__(self,name,type,moves,attack,spattack,hp,defense,spdefense,
    speed,slist,sprite):
        self.name = name
        self.type = type
        self.moves = moves
        self.attack = attack
        self.spattack = spattack
        self.hp = hp        #Bases stats given
        self.defense = defense
        self.spdefense = spdefense
        self.speed = speed
        self.slist = slist
        self.sprite = sprite
        self.currattack = self.attack
        self.currspattack = self.spattack #stats during match which can change
        self.currhp = self.hp
        self.currdefense = self.defense
        self.currspdefense = self.spdefense
        self.currspeed = self.speed
    def pokecopy(self):
        x = Pokemon(self.name,self.type,self.moves,self.attack,self.currspattack,self.currhp,self.defense
        ,self.spdefense,self.speed,self.slist,self.sprite)
        return x
    

class Trainer(object):
    def __init__(self,name,p1,p2,p3,p4,p5,p6):
        self.name = name
        self.p1 =p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.curr = p1
        self.poklist = [p1,p2,p3,p4,p5,p6]
    def switch(self,p):
        if(p.hp<= 0):
            print('select another pokemon')
            return False
        self.curr = p
    def teamalive(self):
        if(self.p1.currhp <=0 and self.p2.currhp <=0 and self.p3.currhp <=0 and self.p4.currhp <=0 and self.p5.currhp <=0 and self.p6.currhp <=0):
            return False
        else:
            return True 
    def pokelist(self):
        L = []
        for i in range(6):
            if(self.poklist[i] == self.curr):
                continue
            else:
                L.append(self.poklist[i])
        return L
    def makecopy(self):
        l = []
        for j in self.poklist:
            l.append(j.pokecopy())
        Newt = Trainer(self.name,l[0],l[1],l[2],l[3],l[4],l[5])
        for i in Newt.poklist:
            if(i.currhp >0):
                Newt.curr = i
        return Newt
    def restoreall(self):
        for i in self.poklist:
            i.currhp = i.hp 


            #attacker   #defender

garslist = [[(0,0,80,100),(105,0,185,100),(215,0,292,100),(320,0,400,100),(425,0,505,100),(530,0,610,100),(635,0,720,100)],
            [(0,100,80,200),(105,100,185,200),(215,100,292,200),(320,100,400,200),(425,100,505,200),(530,100,610,200),(635,100,720,200)],
            [(0,200,80,300),(105,200,185,300),(215,200,292,300),(320,200,400,300),(425,200,505,300),(530,200,610,300),(635,200,720,300)]]
zaplist = [[(5,0,95,100),(105,0,195,100),(195,0,285,100),(300,0,380,100),(490,0,560,100),(585,0,665,100),(690,0,760,100),(785,0,860,100)],
           [(5,100,95,200),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0)]]

zaplistb = [[(5,0,95,100),(105,0,195,100),(235,0,310,100),(340,0,420,100),(440,0,535,100),(565,0,665,100),(675,0,760,100),(785,0,870,100)],
           [(5,100,95,200),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0)]]
Teplistf = [[[0,0,60,60],[60,0,135,60],[135,0,210,60],[210,0,285,60],[285,0,360,60],[360,0,435,60],[435,0,510,60]]
 ,        [[0,60,60,120],[75,60,135,120],[135,60,210,120],[210,60,285,120],[285,60,360,120],[360,60,435,120],[435,60,510,120]]  ,
           [[0,120,60,180],[60,120,135,180],[135,120,210,1800],[210,120,285,180],[285,120,360,180],[360,120,435,180],[435,120,510,180]]     ]
        
Garchomp = Pokemon('Garchomp',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp back.png')
Zapdos = Pokemon('Zapdos',['Electric','Flying'], [Thunderbolt,Heatwave,Hurricane,FocusBlast],
279,349,384,269,279,299,zaplist,'Sprites/Zapdos front.png')
Zapdos2 = Pokemon('Zapdos',['Electric','Flying'], [Thunderbolt,Heatwave,Hurricane,FocusBlast],
279,349,384,269,279,299,zaplistb,'Sprites/Zapdos back.png')
Garchomp2 = Pokemon('Garchomp2',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp back.png')
Garchomp3 = Pokemon('Garchomp3',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp back.png')
Garchomp4 = Pokemon('Garchomp4',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp back.png')
Garchomp5 = Pokemon('Garchomp5',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp back.png')
Garchomp6 = Pokemon('Garchomp6',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp back.png')
Garchomp7 = Pokemon('Garchomp7',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp front.png')
Garchomp8 = Pokemon('Garchomp8',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp front.png')
Garchomp9 = Pokemon('Garchomp9',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp front.png')
Garchomp10 = Pokemon('Garchomp10',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp front.png')
Garchomp11 = Pokemon('Garchomp11',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp front.png')
Garchomp12 = Pokemon('Garchomp12',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,420,289,269,303,garslist,'Sprites/Garchomp front.png')
Deadweight = Pokemon('Deadweight',['Dragon','Ground'],
[Earthquake,DragonClaw,Flamethrower,Dragonpulse],359,259,0,289,269,303,garslist,'Sprites/Garchomp front.png')
Tepig = Pokemon('Tepig',['Fire'],[Flamethrower,HeadSmash,WildCharge,Tackle],194,189,334,189,189,189,Teplistf,'Sprites/Tepigfront.png')
Trainer1 = Trainer('Goku',Garchomp,Zapdos,Garchomp3,Garchomp4,Garchomp5,Garchomp6)
Trainer2 = Trainer('Bob',Garchomp7,Zapdos2,Garchomp9,Garchomp10,Garchomp11,Garchomp12)
Wild = Trainer('WildEncounter',Tepig,Deadweight,Deadweight,Deadweight,Deadweight,Deadweight)
#print(delay(5))
#Use dictionary later
def typeeffectiveness(defender,moveused):
    x = 1
    for i in range(len(defender.type)):
        if(defender.type[i] == 'Fire'):
            if(moveused.type == 'Fire'):
                x*= 0.5
            elif(moveused.type == 'Water'):
                x*=2
            elif(moveused.type == 'Grass'):
                x*=0.5
            elif(moveused.type == 'Ice'):
                x*=0.5
            elif(moveused.type == 'Bug'):
                x*=0.5
            elif(moveused.type == 'Steel'):
                x*=0.5
            elif(moveused.type == 'Ground'):
                x*=2
            elif(moveused.type == 'Rock'):
                x*=0.5
        elif(defender.type[i] == 'Grass'):
            if(moveused.type == 'Fire'):
                x*=2
            elif(moveused.type == 'Water'):
                x*=0.5
            elif(moveused.type == 'Grass'):
                x*=2
            elif(moveused.type == 'Ice'):
                x*=2
            elif(moveused.type == 'Electric'):
                x*=0.5
            elif(moveused.type == 'Ground'):
                x*=0.5
            elif(moveused.type == 'Electric'):
                x*=0.5
            elif(moveused.type == 'Flying'):
                x*=2
            elif(moveused.type == 'Bug'):
                x*=2
            
        elif(defender.type[i] == 'Water'):
            if(moveused.type == 'Electric'):
                x*2
            elif(moveused.type == 'Fire'):
                x*=0.5
            elif(moveused.type == 'Water'):
                x*=0.5
            elif(moveused.type == 'Grass'):
                x*=2
            elif(moveused.type == 'Ice'):
                x*=0.5
            elif(moveused.type == 'Steel'):
                x*=0.5             
        elif(defender.type[i] == 'Dark'):
            if(moveused.type == 'Fighting'):
                x*=2
            elif(moveused.type == 'Psychic'):
                x*=0
            elif(moveused.type == 'Bug'):
                x*=2
            elif(moveused.type == 'Dark'):
                x*=0.5 
            elif(moveused.type == 'Ghost'):
                x*=0.5 
        elif(defender.type[i] == 'Psychic'):
            if(moveused.type == 'Fighting'):
                x*=0.5
            elif(moveused.type == 'Psychic'):
                x*=0.5
            elif(moveused.type == 'Bug'):
                x*=2
            elif(moveused.type == 'Ghost'):
                x*=2
            elif(moveused.type == 'Dark'):
                x*=2
        elif(defender.type[i] == 'Ground'):
            if(moveused.type == 'Water'):
                x*=2
            elif(moveused.type == 'Electric'):
                x*=0
            elif(moveused.type == 'Grass'):
                x*=2
            elif(moveused.type == 'Ice'):
                x*=2
            elif(moveused.type == 'Rock'):
                x*=0.5
        elif(defender.type[i] == 'Electric'):
            if(moveused.type == 'Electric'):
                x*=0.5
            elif(moveused.type == 'Ground'):
                x*=2
            elif(moveused.type == 'Flying'):
                x*=0.5
        elif(defender.type[i] == 'Bug'):
            if(moveused.type == 'Fire'):
                x*=2
            elif(moveused.type == 'Grass'):
                x*=0.5
            elif(moveused.type == 'Fighting'):
                x*=0.5
            elif(moveused.type == 'Ground'):
                x*=0.5
            elif(moveused.type == 'Flying'):
                x*=2
            elif(moveused.type == 'Rock'):
                x*=2

        elif(defender.type[i] == 'Steel'):
            if(moveused.type == 'Fighting'):
                x*=2
            elif(moveused.type == 'Normal'):
                x*=0.5
            elif(moveused.type == 'Fire'):
                x*=2
            elif(moveused.type == 'Grass'):
                x*=0.5
            elif(moveused.type == 'Ice'):
                x*=0.5
            elif(moveused.type == 'Ground'):
                x*=2
            elif(moveused.type == 'Flying'):
                x*=0.5
            elif(moveused.type == 'Psychic'):
                x*=0.5
            elif(moveused.type == 'Bug'):
                x*=0.5
            elif(moveused.type == 'Rock'):
                x*=0.5
            elif(moveused.type == 'Dragon'):
                x*=0.5
            elif(moveused.type == 'Steel'):
                x*=2
        elif(defender.type[i] == 'Ghost'):
            if(moveused.type == 'Normal'):
                x *= 0
            elif(moveused.type == 'Fighting'):
                x *= 0
            elif(moveused.type == 'Bug'):
                x *= 0.5
            elif(moveused.type == 'Ghost'):
                x *= 2
            elif(moveused.type == 'Dark'):
                x *= 2
        elif(defender.type[i] == 'Dragon'):
            if(moveused.type == 'Grass'):
                x *= 0.5
            elif(moveused.type == 'Water'):
                x *= 0.5
            elif(moveused.type == 'Fire'):
                x *= 0.5
            elif(moveused.type == 'Dragon'):
                x *= 2
            elif(moveused.type == 'Ice'):
                x *= 2
            elif(moveused.type == 'Electric'):
                x *= 0.5
        elif(defender.type[i] == 'Flying'):
            if(moveused.type == 'Electric'):
                x *= 2
            elif(moveused.type == 'Rock'):
                x *= 2
            elif(moveused.type == 'Ground'):
                x *= 0
            elif(moveused.type == 'Grass'):
                x *= 0.5
            elif(moveused.type == 'Ice'):
                x *= 2
            elif(moveused.type == 'Fighting'):
                x *= 0.5
            elif(moveused.type == 'Bug'):
                x *= 0.5
        elif(defender.type[i] == 'Fighting'):
            if(moveused.type == 'Flying'):
                x *= 2
            elif(moveused.type == 'Rock'):
                x *= 0.5
            elif(moveused.type == 'Psychic'):
                x *= 2
            elif(moveused.type == 'Bug'):
                x *= 0.5
            elif(moveused.type == 'Dark'):
                x *= 0.5
        elif(defender.type[i] == 'Rock'):
            if(moveused.type == 'Normal'):
                x *= 0.5
            elif(moveused.type == 'Grass'):
                x *= 2
            elif(moveused.type == 'Water'):
                x *= 2
            elif(moveused.type == 'Fire'):
                x *= 0.5
            elif(moveused.type == 'Flying'):
                x *= 0.5
            elif(moveused.type == 'Ground'):
                x *= 2
            elif(moveused.type == 'Fighting'):
                x *= 2
            elif(moveused.type == 'Steel'):
                x *= 2
        elif(defender.type[i] == 'Ice'):
            if(moveused.type == 'Fighting'):
                x *= 2
            elif(moveused.type == 'Fire'):
                x *= 2
            elif(moveused.type == 'Rock'):
                x *= 2
            elif(moveused.type == 'Steel'):
                x *= 2
            elif(moveused.type == 'Ice'):
                x *= 0.5
        elif(defender.type[i] == 'Normal'):
            if(moveused.type == 'Fighting'):
                x *= 2
            elif(moveused.type == 'Ghost'):
                x *= 0
    return x

def damage (Pokemon1a,Pokemon2d,moveused):
    if(moveused == None):
        return 0
    x = 1
    y = typeeffectiveness(Pokemon2d,moveused)
    if(moveused.type == Pokemon1a.type):
        x = 1.5
    if(moveused.sporap == 'sp'):#uses special attack
        return (((((2*100)/5)+2)*moveused.attackpower*
        (Pokemon1a.currspattack/Pokemon2d.currspdefense)/50)+2)*x*y
    elif(moveused.sporap == 'ap'):
        return (((((2*100)/5)+2)*moveused.attackpower*
        (Pokemon1a.currattack/Pokemon2d.currdefense)/50)+2)*x*y

#battle(Garchomp,Garchomp2)
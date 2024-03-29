#Minimax game AI
from Pokemon import*
import copy
import string
statedict = {}
#Resets global dictionary each time it is called
def wrapperaitree(self,enemy,depth):
    dic = {}
    prevmove = ''
    L = []
    for k in statedict: 
       L.append(k)
    i = 0
    while(len(statedict) != 0):
        statedict.pop(L[i])
        i+=1
    return aitree(self,enemy,depth,dic,prevmove)

#Uses Minimax algorithm to go through all the move that the AI can make 
#and stores them in a dictionary
def aitree(self,enemy,depth,dic,prevmove):
    if(depth == 3):
        return 
    else:
        for i in self.curr.moves:
            x = self.makecopy()
            y = enemy.makecopy()
            moveuenemy = pickbestmove(x,y)
            moveuself = i
            battle2(x,y,moveuenemy,moveuself)
            z = prevmove + '-' + moveuself.name
            dic[z] = state(x,y)
            statedict[z] = state(x,y)
            aitree(x,y,depth+1,dic,z)
        for j in self.pokelist():
            a = self.makecopy()
            b = enemy.makecopy()
            if(j.currhp<=0):
                continue
            moveuenemy = pickbestmove(x,y)
            moveuself = 'switch+' + j.name
            battle2(a,b,moveuenemy,moveuself)
            c = prevmove + '-' + moveuself
            dic[c] = state(a,b)
            statedict[c] = state(a,b)
            aitree(a,b,depth+1,dic,c)



        

        
    
    
#calculates the state of the game by adding the hp of all the players pokemon
def state(self,enemy):
    hpself = 0
    hpenemy= 0 
    for i in self.poklist:
        if(i.currhp<0):
            continue
        hpself+= i.currhp
    for j in enemy.poklist:
        if(j.currhp<0):
            continue
        hpenemy+= j.currhp
    return (hpself - hpenemy)/(hpself+hpenemy)
#goes through the options in the state dictionary and finds the most 
#advanageous one
def pickmove(self):
    best = -10000
    bestmove = ''
    for k in statedict:
        if(statedict[k]> best):
            
            best = statedict[k]
            bestmove = k
    moveog = bestmove.split('-')
    for i in self.curr.moves:
        if(moveog[1] == i.name):
            
            return i
    
    return moveog[1]
#picks the enemy move that'll do the most damage(we are assuming that's the 
# action that player will take for simplicity and runtime) 
def pickbestmove(self,enemy):
    best = 0
    bestmove = 0    
    for i in enemy.curr.moves:
        damages = damage(enemy.curr,self.curr,i)
        if(damages>best):
            best = damages
            bestmove = i

    return bestmove
def switch(Trainer1):
     for i in range(len(Trainer1.pokelist())):
            if(Trainer1.pokelist()[i].currhp>0):
                Trainer1.curr  = Trainer1.pokelist()[i]   
                break

    

def battle2(self,enemy,movenemy,moveself):
            if(type(moveself) == str):
                y = moveself.split('+')
                for i in self.pokelist():
                    if(y[1] == i.name):
                        self.curr = i
                damages = damage(enemy.curr,self.curr,movenemy)
                self.curr.currhp -= damages
            else:
                if(self.curr.speed>enemy.curr.speed):
                    dam1 = damage(self.curr,enemy.curr,moveself)
                    enemy.curr.currhp -= dam1
                    if(enemy.curr.currhp<= 0 ):
                        switch(enemy)
                        return
                    dam2 = damage(enemy.curr,self.curr,movenemy)
                    self.curr.currhp -=dam2
                else:
                    dam3 = damage(enemy.curr,self.curr,movenemy)
                    self.curr.currhp -=dam3
                    if(self.curr.currhp<= 0):
                        switch(self)
                        return
                    dam4 = damage(self.curr,enemy.curr,moveself)
                    enemy.curr.currhp -= dam4


def ai(self,enemy):
    selfc = self.makecopy()
    enemyc = enemy.makecopy()
    wrapperaitree(selfc,enemyc,0)
    return pickmove(selfc)

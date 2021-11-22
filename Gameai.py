#separte battle function for the AI
from Pokemon import*
import copy
import string
statedict = {}
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
def aitree(self,enemy,depth,dic,prevmove):
    if(depth == 3):
        return 
    else:
        for i in self.curr.moves:
            x = copy.copy(self)
            y = copy.copy(enemy)
            moveuenemy = pickbestmove(x,y)
            moveuself = i
            battle2(x,y,moveuenemy,moveuself)
            z = prevmove + '-' + moveuself.name
            dic[z] = state(x,y)
            statedict[z] = state(x,y)
            aitree(x,y,depth+1,dic,z)
        for j in self.pokelist():
            a = copy.copy(self)
            b = copy.copy(enemy)
            if(j.currhp<0):
                continue
            moveuenemy = pickbestmove(x,y)
            moveuself = 'switch+' + j.name
            battle2(a,b,moveuenemy,moveuself)
            c = prevmove + '-' + moveuself
            dic[c] = state(a,b)
            statedict[c] = state(a,b)
            aitree(a,b,depth+1,dic,c)



        

        
    #loop throught all elements of tree
    # set those elements = to another tree with None values and updated data
    #recursive call with increased depth and updated player conditions
    return #returns tree each node should have 9 other nodes

def state(self,enemy):
    hpself = 0
    hpenemy= 0 
    for i in self.poklist:
        hpself+= i.currhp
    for j in enemy.poklist:
        hpenemy+= j.currhp
    return (hpself - hpenemy)/(hpself+hpenemy)

def pickmove(self):
    print(self.curr.currhp)
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
            if(type(moveself) == string):
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

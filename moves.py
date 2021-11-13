class move(object):
    def __init__(self,name,type,attackpower,sporap):
        self.type = type
        self.name = name
        self.attackpower = attackpower
        self.sporap = sporap

Earthquake = move('Earthquake','Ground', 100,'ap')
DragonClaw = move('DragonClaw','Dragon',80,'ap')
Flamethrower = move('Flamethrower','Fire',90,'sp')
Dragonpulse = move('Dragonpulse','Dragon',90,'sp') 
Thunderbolt = move('Thunderbolt', 'Electric',95,'sp')
Hurricane = move('Hurricane','Flying',120,'sp')
Heatwave = move('Heatwave','Fire',90,'sp')
FocusBlast = move('FocusBlast', 'Fighting', 120, 'sp')

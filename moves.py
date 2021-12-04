
#defines moves that'll be used by Pokemon
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
Tackle = move('Tackle','Normal',50,'ap')
WildCharge = move('WildCharge','Electric',90,'ap')
HeadSmash = move('HeadSmash','Rock',150,'ap')
Psychic = move('Psychic','Psychic',95,'sp')
Icebeam = move('Icebeam','Ice',95,'sp')
Vcreate = move('Vcreate','Fire',200,'ap')
Glaciate = move('Glaciate','Ice',130,'sp')
BoltStrike = move('BoltStrike','Electric',130,'ap')


from wand import Wand
from spell import Spell
from potion import Potion

class Player:
    def __init__(self,name,year,house):
        self.name=name
        self.index = 0
        self.year=year
        self.house=house
        self.health=year*10
        self.mods = [1,1,1,1]
        self.modpotion=self.mods[0]
        self.modhealth=self.mods[1]
        self.modspell=self.mods[2]
        self.modmagic=self.mods[3]
        self.shield=0
        self.pos=[1,0,0,0]
        self.maxh=year*10
        self.next=[4,4,4,4]
        self.move=1
        self.magic=year*10
        self.maxm = year * 10
        self.potion_number=[]
        '''
    def mod_potion(self,wand):
        self.modpotion = 0.5 + 0.1 * self.year
        if self.house == "Slytherin":
            self.modpotion = self.modpotion + 0.2
        if wand.core == "Chimera":
            self.modpotion = self.modpotion + 0.2
        if wand.lenght == 12 :
            self.modpotion = self.modpotion + 0.2
        if wand.lenght == 11:
            self.modpotion = self.modpotion + 0.1
        if wand.lenght == 9:
            self.modpotion = self.modpotion - 0.1
        if wand.lenght == 8:
            self.modpotion = self.modpotion - 0.2
        if self.house == "Gryffindor":
            self.modpotion = self.modpotion - 0.2
        if wand.core == "Dragon" :
            self.modpotion = self.modpotion - 0.2
        return self.modpotion
    def mod_health(self,wand) :
        self.modhealth = 0.5 + 0.1 * self.year
        if self.house == "Hufflepuff":
            self.modhealth = self.modhealth + 0.2
        if wand.core == "Unicorn":
            self.modhealth = self.modhealth + 0.2
        if wand.lenght == 12:
            self.modhealth = self.modhealth + 0.2
        if wand.lenght == 11:
            self.modhealth = self.modhealth + 0.1
        if wand.lenght == 9:
            self.modhealth = self.modhealth - 0.1
        if wand.lenght == 8:
            self.modhealth = self.modhealth - 0.2
        if self.house == "Slytherin":
            self.modhealth = self.modhealth - 0.2
        if wand.core == "Phoenix":
            self.modhealth = self.modhealth - 0.2
        return self.modhealth
    def mod_spell(self,wand) :
        self.modspell = 0.5 + 0.1 * self.year
        if self.house == "Gryffindor":
            self.modspell = self.modspell + 0.2
        if wand.core == "Phoenix":
            self.modspell = self.modspell + 0.2
        if wand.lenght == 8:
            self.modspell = self.modspell + 0.2
        if wand.lenght == 9:
            self.modspell = self.modspell + 0.1
        if wand.lenght == 11:
            self.modspell = self.modspell - 0.1
        if wand.lenght == 12:
            self.modspell = self.modspell - 0.2
        if self.house == "Ravenclaw":
            self.modspell = self.modspell - 0.2
        if wand.core == "Chimera":
            self.modspell = self.modspell - 0.2
        return self.modspell
    def mod_magic(self,wand) :
        self.modmagic = 0.5 + 0.1 * self.year
        if self.house == "Ravenclaw":
            self.modmagic = self.modmagic + 0.2
        if wand.core == "Dragon":
            self.modmagic = self.modmagic + 0.2
        if wand.lenght == 8:
            self.modmagic = self.modmagic + 0.2
        if wand.lenght == 9:
            self.modmagic = self.modmagic + 0.1
        if wand.lenght == 11:
            self.modmagic = self.modmagic - 0.1
        if wand.lenght == 12:
            self.modmagic = self.modmagic - 0.2
        if wand.core == "Unicorn":
            self.modmagic = self.modmagic - 0.2
        if self.house == "Hufflepuff":
            self.modmagic = self.modmagic - 0.2

        return self.modmagic
    '''

    def imgs(self):
        img=""
        if self.house== "Gryffindor":
            img="1.png"
        elif self.house == "Slytherin":
            img="2.png"
        elif self.house == "Ravenclaw":
            img="3.png"
        elif self.house== "Hufflepuff":
            img="4.png"
            
        return img
    def change(self,wand):
        self.pos[0] = 1
        wand.pos[0] = 1
        wand.pos[2] = wand.pos[0]*100+100
        wand.pos[3] = wand.pos[0]*100+100
        self.next=[4,4,4,4,4]
        self.mod(wand)
        self.modpotion = self.mods[0]
        self.modspell = self.mods[2]
        self.magic = int(max((self.year * 10 + 10) * self.mods[3],20))
        if self.magic % 10 < 5:
            self.magic = self.magic - self.magic % 10
        else:
            self.magic = self.magic - self.magic % 10 + 10
        self.maxm = self.magic
        self.health = int(max((self.year * 10 + 10)* self.mods[1],20))
        self.maxh = self.health

                             # potion,health,spell,magic                       
    modh_dict = {"Slytherin" : ( 0.2,-0.2,   0,   0),
                "Gryffindor" : (-0.2,   0, 0.2,   0),
                "Hufflepuff" : (   0, 0.2,   0,-0.2),
                "Ravenclaw"  : (   0,   0,-0.2, 0.2)
                }

    modwc_dict ={"Chimera"   : ( 0.2,   0,-0.2,   0),
                "Dragon"     : (-0.2,   0,   0, 0.2),
                "Unicorn"    : (   0, 0.2,   0,-0.2),
                "Phoenix"    : (   0,-0.2, 0.2,   0)
                }

    modwl_dict ={12          : ( 0.2, 0.2,-0.2,-0.2),
                11           : ( 0.1, 0.1,-0.1,-0.1),
                9            : (-0.1,-0.1, 0.1, 0.1),
                8            : (-0.2,-0.2, 0.2, 0.2)
                }
    
    def mod(self,wand):
        self.mods[0] = 0.5 + 0.1 * self.year
        self.mods[1] = 0.5 + 0.1 * self.year
        self.mods[2] = 0.5 + 0.1 * self.year
        self.mods[3] = 0.5 + 0.1 * self.year
        for x in self.modh_dict:
            if self.house == x:
                self.mods[0] = self.mods[0] + self.modh_dict[x][0]
                self.mods[1] = self.mods[1] + self.modh_dict[x][1]
                self.mods[2] = self.mods[2] + self.modh_dict[x][2]
                self.mods[3] = self.mods[3] + self.modh_dict[x][3]
        for x in self.modwc_dict:
            if wand.core == x:
                self.mods[0] = self.mods[0] + self.modwc_dict[x][0]
                self.mods[1] = self.mods[1] + self.modwc_dict[x][1]
                self.mods[2] = self.mods[2] + self.modwc_dict[x][2]
                self.mods[3] = self.mods[3] + self.modwc_dict[x][3]
        for x in self.modwl_dict:
            if wand.lenght == x:
                self.mods[0] = self.mods[0] + self.modwl_dict[x][0]
                self.mods[1] = self.mods[1] + self.modwl_dict[x][1]
                self.mods[2] = self.mods[2] + self.modwl_dict[x][2]
                self.mods[3] = self.mods[3] + self.modwl_dict[x][3]
from wand import Wand
from spell import Spell
from potion import Potion

class Player:
    def __init__(self,name,year,house):
        self.name=name
        self.index = 0
        self.lastspell =""
        self.spells_ind = 0 
        self.potions_ind = 0 
        self.year=year
        self.house=house
        self.health=year*10
        self.mods = [1,1,1,1]
        self.modpotion=self.mods[0]
        self.modhealth=self.mods[1]
        self.modspell=self.mods[2]
        self.modmagic=self.mods[3]
        self.shield=0
        self.pos=[1,0,0,0,0] # [0-3,x,y,next_y]
        self.maxh=year*10
        self.next=[4,4,4,4]
        self.move=1
        self.magic=year*10
        self.maxm = year * 10
        self.potion_number=[]
        self.tab_1=[]
        self.tab_2=[]
        self.tab_3=[]

    def create_tabs(self,wand):
        self.tab_1=[self.name,
                  "Dom: " + self.house,
                  "Zycie: " + str(self.health) + "/" + str(self.maxh),
                  "Magia: " + str(self.magic) + "/" + str(self.maxm),
                  "Dlugość różdżki: " + str(wand.lenght) + " cali.",
                  "Rdzeń różdżki: " + wand.core]

    def create_tabs2(self,spell,potion):
        self.tab_2=["Zaklecie: " + str(spell.name),
                    "Koszt: " + str(spell.cost),
                    "Obrazenia: " + str(int(self.modspell * spell.dmg)),
                    "Leczenie: " + str(int(self.modspell * spell.heal)),
                    "Efekt zaklecia: " + spell.efect]

        self.tab_3=["Eliksir: " + str(potion.name),
                    "Ilość: " + str(self.potion_number[self.potions_ind]),
                    "Obrazenia: " + str(int(self.modpotion * potion.dmg)),
                    "Leczenie: " + str(int(self.modpotion * potion.heal)),
                    "Efekt eliksiru: " + potion.efect]


    def imgs(self):
        img=""
        if self.house== "Gryffindor":
            img="images/1.png"
        elif self.house == "Slytherin":
            img="images/2.png"
        elif self.house == "Ravenclaw":
            img="images/3.png"
        elif self.house== "Hufflepuff":
            img="images/4.png"
            
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
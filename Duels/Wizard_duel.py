from player import Player
from spell import Spell
from wand import Wand
from potion import Potion
import pygame, sys, random, time, copy
from pygame.locals import *
pg=pygame
pd=pg.display
pg.init()
FPS = 16 
fpsClock = pygame.time.Clock()
press = 0
index = 0
player_1 = Player("",0,"")
player_2 = Player("",0,"")    
wand_1 = Wand("",0)
wand_2 = Wand("",0)
spells = [  Spell("Brak",0,0,-20,"Brak"),
                Spell("Flipendo",10,0,10,"Brak"),
                Spell("Depulso",20,0,20,"Brak"),
                Spell("Expeliarmus",10,0,30,"Rozbrojenie"),
                Spell("Incendo",15,0,50,"Ogien"),
                Spell("Petrificus Totalus",10,0,40,"Paraliz"),
                Spell("Protego",0,0,30,"Tarcza"),
                Spell("Episkey",0,10,15,"Brak"),
                Spell("Avada Kedavra",max(player_1.maxh,player_2.maxh),0,max(player_1.maxm,player_2.maxm),"Smierc")]
potions = [Potion("Basic potion",2,10,0,"Brak"),
             Potion("Healing potion",2,0,20,"Brak"),
             Potion("Toxic potion",0,0,0,"Trujace opary"),
             Potion("Magic potion",0,0,0,"Przywrocenie magii")]
size = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)   
RED = (220,0,0)
GREEN = (0,200,0)
PURPLE = (147,112,219)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
map = pd.set_mode((size + 400, size))
font = pg.font.SysFont("Comic Sans MS", 18)
sfont = pg.font.SysFont("Comic Sans MS", 12)
lfont = pg.font.SysFont("Comic Sans MS", 70)
mfont = pg.font.SysFont("Comic Sans MS", 30)

def text(text, font, color = BLACK):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

    
def button(msg, x, y, width, height, color, action = None,args = None):

    global press
    width_half = width / 2
    height_half = height / 2
    mouse = pg.mouse.get_pos() 
    click = pg.mouse.get_pressed()
    pg.draw.rect(map, color, (x, y, width, height))


    if (x < mouse[0] < (x + width)) and (y < mouse[1] < (y + height)):
        if (click[0] == 1):
            press = 1
        if press == 1 and click[0] == 0:
            press = 0
            if (action != None):
                if args != None :
                    action (*args)
                else:
                    action()
    
    text_surf, text_rect = text(msg, font)
    text_rect.center = (x + width_half, y + height_half)
    map.blit(text_surf, text_rect)


def exit():

    pg.quit()
    sys.exit(0)


def minus(x,y):
    global index
    index = ((x-1) % len(y))


def plus(x,y):
    global index
    index = ((x+1) % len(y))


def how(x):
    while True:
        image = pg.image.load(x)
        map.blit(image,(0,0))
        button("podstawy",900,100,100,100,YELLOW)
        button("zaklecia",900,200,100,100,RED,how2)
        button("elisiry",900,300,100,100,RED,how3)
        button("menu",900,400,100,100,RED,menu)
        if x == "how.jpg":
            button("dalej",450,550,100,50,BLUE,how,["how2.jpg"])
        else:
            button("powrot",450,0,100,50,BLUE,how,["how.jpg"])
        pd.flip()
        for e in pg.event.get():
            if e.type==pg.QUIT:
                exit()
            if e.type==KEYDOWN:
                if e.key==K_o:
                    pg.mixer.music.pause()
                if e.key==K_i:        
                    pg.mixer.music.unpause()


def how2():
    global index
    index = 0
    while True:
        
        map.fill((255,255,255))
        button("podstawy",900,100,100,100,RED,how,["how.jpg"])
        button("zaklecia",900,200,100,100,YELLOW)
        button("elisiry",900,300,100,100,RED,how3)
        button("menu",900,400,100,100,RED,menu)
        button("poprzednie",200,250,100,100,ORANGE,minus,[index,spells])
        button("nastepne",700,250,100,100,ORANGE,plus,[index,spells])       
        text_surf, text_rect = text("Nazwa: " + str(spells[index].name), font,BLACK)
        text_rect.center = (500,250)
        map.blit(text_surf, text_rect)
        text_surf, text_rect = text("Obrażenia podstawowe: " + str(spells[index].dmg), font,BLACK)
        text_rect.center = (500,270)
        map.blit(text_surf, text_rect)
        text_surf, text_rect = text("Leczenie podstawowe: " + str(spells[index].heal), font,BLACK)
        text_rect.center = (500,290)
        map.blit(text_surf, text_rect)
        text_surf, text_rect = text("Koszt: " + str(spells[index].cost), font,BLACK)
        text_rect.center = (500,310)
        map.blit(text_surf, text_rect)
        text_surf, text_rect = text("Efekt: " + str(spells[index].efect), font,BLACK)
        text_rect.center = (500,330)
        map.blit(text_surf, text_rect)
        for e in pg.event.get():
            if e.type==pg.QUIT:
                exit()
            if e.type==KEYDOWN:
                if e.key==K_o:
                    pg.mixer.music.pause()
                if e.key==K_i:        
                    pg.mixer.music.unpause()
        pd.update()

def how3():
    global index
    index = 0
    while True:
   
        map.fill((255,255,255))
        button("podstawy",900,100,100,100,RED,how,["how.jpg"])
        button("zaklecia",900,200,100,100,RED,how2)
        button("elisiry",900,300,100,100,YELLOW)
        button("menu",900,400,100,100,RED,menu)
        button("poprzednie",200,250,100,100,ORANGE,minus,[index,potions])
        button("nastepne",700,250,100,100,ORANGE,plus,[index,potions])       
        text_surf, text_rect = text("Nazwa: " + str(potions[index].name), font,BLACK)
        text_rect.center = (500,250)
        map.blit(text_surf, text_rect)
        text_surf, text_rect = text("Ilosc podstawowa: " + str(potions[index].number), font,BLACK)
        text_rect.center = (500,270)
        map.blit(text_surf, text_rect)
        text_surf, text_rect = text("Obrażenia podstawowe: " + str(potions[index].dmg), font,BLACK)
        text_rect.center = (500,290)
        map.blit(text_surf, text_rect)
        text_surf, text_rect = text("Leczenie podstawowe: " + str(potions[index].heal), font,BLACK)
        text_rect.center = (500,310)
        map.blit(text_surf, text_rect)
        text_surf, text_rect = text("Efekt: " + str(potions[index].efect), font,BLACK)
        text_rect.center = (500,330)
        map.blit(text_surf, text_rect)
        for e in pg.event.get():
            if e.type==pg.QUIT:
                exit()
            if e.type==KEYDOWN:
                if e.key==K_o:
                    pg.mixer.music.pause()
                if e.key==K_i:        
                    pg.mixer.music.unpause()
        pd.update()

def main():

    #pg.mixer.music.load("ghostin.mp3")
    #pg.mixer.music.play(-1)
    pd.set_caption("Wizard duels")
    menu()
    
    
def menu():
    spells[8].cost = 140
    spells[8].dmg = 144
    obraz=pg.image.load("file.jpg")

    while True:
        for e in pg.event.get():
            
            if e.type == pg.QUIT:
                sys.exit(0)
            if e.type == KEYDOWN:
                
                if e.key == K_o:
                    pg.mixer.music.pause()
                
                if e.key == K_i:        
                    pg.mixer.music.unpause()

        map.blit(obraz,(0,0))

        button("Graj", 400, 300, 200, 100, GREEN, preparation)
        button("Jak grac", 400, 400, 200, 100, YELLOW, how,["how.jpg"])
        button("wyjscie", 400, 500, 200, 100,RED , exit)
        
        pd.update()
        
def burn(x,y):
    
    if x.pos[0] == x.next[0] or x.pos[0] == x.next[1]:
        x.health = x.health- int(20 * y.modspell)

    x.next[0] = 4
    x.next[1] = 4

def toxic(x,y):

    if x.pos[0] == x.next[2] or x.pos[0] == x.next[3]:
        x.health = x.health - int(10 * y.modpotion)
    x.next[2] = 4
    x.next[3] = 4

def write(player):
    player.name = ""
    player.index = 0
    o=1
    while o:
        obraz = pg.image.load("file.jpg")
        map.blit(obraz,(0,0))
        text_surf, text_rect = text("Wpisz nazwe gracza:", lfont,WHITE)
        text_rect.center = (500,50)
        map.blit(text_surf, text_rect)
        text_surf, text_rect = text(str(player.name), lfont,WHITE)
        text_rect.center = (500,150)
        map.blit(text_surf, text_rect)
        temp = [RED]
        if player.index >0:
            temp[0] = ORANGE

        button("Gotowe",400,450,200,100,temp[0],ready,[temp])
        if temp[0] != ORANGE and temp[0] != RED:
            o=0
        pd.update()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:
                    if player.index > 0:
                        player.name = player.name[:player.index - 1] + player.name[player.index:]
                        player.index -= 1
                else:
                    char=str(e.unicode)
                    if char != '' and char != '\r':
                        player.name = player.name[:player.index] + char + player.name[player.index:]
                        player.index += 1
            if e.type == KEYUP:
                if e.key == K_RIGHT:
                    if player.index < len(player.name):
                        player.index += 1
                if e.key == K_LEFT:
                    if player.index > 0:
                        player.index -= 1

def choose(p,player,list1,list2,list3=None): 
    o=1
    while o :
        x= 100 * (9- len(list1))/2 + 50
        obraz = pg.image.load("file.jpg")
        map.blit(obraz,(0,0))
        text_surf, text_rect = text(str(p.name), lfont,WHITE)
        text_rect.center = (500,50)
        map.blit(text_surf, text_rect)
        
        text_surf, text_rect = text(str(list1[-1]), lfont,WHITE)
        text_rect.center = (500,150)
        map.blit(text_surf, text_rect)

        for i in range (len(list2)):
            button(str(list1[i]),x,220,100,100,list2[i],set,[player,list1,list2,i])
            y=340
            if list3 != None:
                for j in range(4): 
                    text_surf, text_rect = text(list3[i][j],font,WHITE)
                    text_rect.center = (x + 40,y)
                    map.blit(text_surf, text_rect)
                    y = y + 20
            x = x + 110

        x = 100
        temp = [RED]
        if list2.count(GREEN) == 1:
            temp[0] = ORANGE

        button("Gotowe",400,450,200,100,temp[0],ready,[temp,list2])

        if temp[0] != ORANGE and temp[0] != RED:
            i = list2.index(GREEN)
            j = set(player,list1,list2,i)
            list2[i] = WHITE
            return j
        pd.update()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            
            if e.type == KEYDOWN:
                
                if e.key == K_o:
                    #pg.mixer.music.pause()
                    print("ok")
                if e.key == K_i:
                    #pg.mixer.music.unpause()
                    print("ok")
        pd.update()

def ready(p,lista2 = None):
    if p[0] != RED:
            p[0] = WHITE


def set(player,list1,list2,ind):
    if  len(list2) > ind:
        for x in range (len(list2)):
            list2[x] = WHITE
        list2[ind] = GREEN
        player = list1[ind]
        return player
        
def action(player1,player2,spell,x,wand1,wand2):

    player1.magic = min(player1.magic-spell.cost+10,player1.maxm)
    
    if spell.name != "Protego" and spell.name != "Episkey" and spell.name != "Avada Kedavra":    
        if player2.pos[0] == x :
            if player2.shield == 0:
                player2.health = player2.health - int(spell.dmg * player1.modspell)
                
                if spell.name == "Expeliarmus" :
                    wand2.pos[0] = random.randint(0,3)
                    wand2.pos[3] = wand2.pos[0]*100+100
                if spell.name == "Petrificus Totalus":
                    player2.move = 0
            
            else:
                player2.shield = 0
        
        
    
    if spell.name == "Avada Kedavra":
        if player2.pos[0] == x :
            player2.health = 0
        player1.magic = 0
        player1.health = 1
    
    if spell.name == "Episkey" :
        player1.health = min(player1.health+ int(spell.heal * player1.modspell),player1.maxh)

    if spell.last == "Protego":
            player1.modspell = player1.modspell - 1

    if player2.shield == 1:
        player2.shield =0
        
    if spell.name == "Protego" :
        player1.shield = 1
        player1.modspell = 1 + player1.modspell
        spell.last = spell.name

    if spell.name == "Incendo":
        player2.next[0] = x
        templist = [0,1,2,3]
        templist.remove(x)
        player2.next[1] = random.choice(templist)


def action2(player1,player2,potion,potionind,x):

    player1.potion_number[potionind] = player1.potion_number[potionind] - 1
    player1.magic = min(player1.magic+10,player1.maxm)
    
    if potion.name == "Healing potion":
        player1.health = min(player1.maxh,player1.health + int(potion.heal * player1.modpotion))

    if potion.name == "Magic potion":
        player1.magic = player1.maxm

    if potion.name == "Toxic potion":
        player2.next[2] = x
        templist = [0,1,2,3]
        templist.remove(x)
        player2.next[3] = random.choice(templist)

    if player2.pos[0] == x :
        if player2.shield == 0:
            player2.health = player2.health - int(potion.dmg * player1.modpotion)
        else:
            player_2.shield = 0

    if player2.shield == 1:
        player2.shield = 0
        

def resoult(player=None):
    while 1:
        if player != None :
            text_surf, text_rect = text(str("Wygral " + player.name), lfont,BLUE)
        else:
            text_surf, text_rect = text(str("Remis"), lfont,BLUE)
        text_rect.center = ((size + 400) / 2), ((size - 300) / 2)
        map.blit(text_surf, text_rect)
        pd.update()
        button("Reset", 500,200, 100, 100, GREEN,game)
        button("Reset postaci",500,300,100,100,ORANGE,preparation)
        button("Menu",500,400,100,100,RED,menu)
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            if e.type == KEYDOWN:
                if e.key == K_o:
                    #pg.mixer.music.pause()
                    print("ok")
                if e.key == K_i:        
                    #pg.mixer.music.unpause()
                    print("ok")


def preparation():
    list_year = [1,2,3,4,5,6,7,"Wybierz rok:"]
    list_year2 = [WHITE] * 7 
    list_house = ["Gryffindor","Slytherin","Ravenclaw","Hufflepuff","Wybierz dom: "]
    list_house2 = [WHITE] * 4
    list_house3 = [["spell +","magic 0","health 0","potion -"],
                    ["spell 0","magic 0","health -","potion +"],
                    ["spell -","magic +","health 0","potion 0"],
                    ["spell 0","magic -","health +","potion 0"]]
    list_lenght = [8,9,10,11,12,"Wybierz dlugosc rozdzczki:"]
    list_lenght2 = [WHITE] * 5
    list_lenght3 = [["spell ++","magic ++","health --","potion --"],
                     ["spell +","magic +","health -","potion -"],
                     ["spell 0","magic 0","health 0","potion 0"],
                     ["spell -","magic -","health +","potion +"],
                     ["spell --","magic --","health ++","potion ++"],]
    list_core = ["Dragon","Unicorn","Testral","Phoenix","Chimera","Wybierz rdzen rozdzczki:"]
    list_core2 = [WHITE] * 5
    list_core3 = [["spell 0","magic +","health 0","potion -"],
                   ["spell 0","magic -","health +","potion 0"],
                   ["spell 0","magic 0","health 0","potion 0"],
                   ["spell +","magic 0","health -","potion 0"],
                   ["spell -","magic 0","health 0","potion +"]]
    write(player_1)
    player_1.year = choose(player_1,player_1.year,list_year,list_year2)
    player_1.house = choose(player_1,player_1.house,list_house,list_house2,list_house3)
    wand_1.lenght = choose(player_1,wand_1.lenght,list_lenght,list_lenght2,list_lenght3)
    wand_1.core = choose(player_1,wand_1.core,list_core,list_core2,list_core3)

    write(player_2)
    player_2.year = choose(player_2,player_2.year,list_year,list_year2)
    player_2.house = choose(player_2,player_2.house,list_house,list_house2,list_house3)
    wand_2.lenght = choose(player_2,wand_2.lenght,list_lenght,list_lenght2,list_lenght3)
    wand_2.core = choose(player_2,wand_2.core,list_core,list_core2,list_core3)


    game()

def game():
    player_1.change(wand_1)
    player_2.change(wand_2)
    spells[8].cost = max(player_1.maxm,player_2.maxm)
    spells[8].dmg = max(player_1.maxh,player_2.maxh)
    turn = 0
    attack = 1
    x_x = 270
    x_y = 200
    wx_x = x_x + 98
    y_x = 630
    y_y = 200
    wy_x = y_x - 60
    ny_y = y_y
    player_1.pos[1] = x_x
    player_1.pos[2] = x_y
    player_1.pos[3] = x_y
    player_2.pos[1] = y_x
    player_2.pos[2] = y_y
    player_2.pos[3] = y_y
    spells_indx = 0
    spells_indy = 0
    potions_indx = 0
    potions_indy = 0
    wand_p1 = pg.image.load("wand.png")
    wand_p2 = pg.image.load("wand1.png")
    for x in range(len(potions)):
        player_1.potion_number.append(potions[x].number + int(player_1.year / 2))
        player_2.potion_number.append(potions[x].number + int(player_2.year / 2))
    image = pg.image.load(player_1.imgs())
    image2 = pg.image.load(player_2.imgs())
    flame_imgs=["flame1.png","flame2.png","flame3.png","flame4.png","flame5.png","flame6.png","flame7.png","flame8.png"]
    animations_count = 0

    while 1:

        #image3 = pg.image.load("file.jpg")
        map.fill(BLACK)
        
        if (turn % 8 < 4) :
            x = player_1
            x_wand = wand_1
            y = player_2
            y_wand = wand_2
        else:
            x = player_2
            x_wand = wand_2
            y = player_1
            y_wand = wand_1

        text_surf, text_rect = text(str("Tura gracza: " + x.name),mfont,WHITE)
        text_rect.center = (500,50)
        map.blit(text_surf, text_rect)
        
        if (x.health <= 0 and y.health > 0):
            resoult(y)
        if (y.health <= 0 and x.health > 0):
            resoult(x)
        if  x.health <=0 and y.health <= 0:
            resoult()

        for i in range(4):
            flame_img = pg.image.load(flame_imgs[animations_count % len(flame_imgs)])
            if i == player_1.next[0] or i == player_1.next[1]:
                map.blit(flame_img,(x_x,i*100 +100))
            elif i == player_1.next[2] or i == player_1.next[3]:
                button("",x_x - 25,i*100+ 100,150,100,GREEN)
            else:
                button("",x_x,i*100+ 100,100,100,WHITE)

            if i == player_2.next[0] or i == player_2.next[1]:        
                button("",y_x -25,i*100+ 100,150,100,RED)
            elif i == player_2.next[2] or i == player_2.next[3]:        
                button("",y_x - 25,i*100+ 100,150,100,GREEN)
            else:
                button("",y_x,i*100+100,100,100,WHITE)
            
            if i == player_1.next[4] :
                button("",y_x,i*100+100,100,100,ORANGE)
            if i == player_2.next[4] :
                button("",x_x,i*100+100,100,100,ORANGE)
        animations_count = animations_count + 1

        if turn % 8 == 1 :
            player_1.pos[2] = player_1.pos[3]
            wand_1.pos[2] = wand_1.pos[3]
            map.blit(image,(x_x,player_1.pos[2]))
            map.blit(wand_p1,(wx_x,wand_1.pos[2]))
        else:
            map.blit(image,(x_x,player_1.pos[2]))
            map.blit(wand_p1,(wx_x,wand_1.pos[2]))
        
        if turn % 8 == 5 :
            player_2.pos[2] = player_2.pos[3]
            wand_2.pos[2] = wand_2.pos[3]
            map.blit(image2,(y_x,player_2.pos[2]))
            map.blit(wand_p2,(wy_x,wand_2.pos[2]))
        else:
            map.blit(image2,(y_x,player_2.pos[2]))
            map.blit(wand_p2,(wy_x,wand_2.pos[2]))
        
        if turn % 4 == 0:
            text_surf, text_rect = text(str("tura gracza: " + x.name),lfont,BLUE)
            text_rect.center = (500,300)
            map.blit(text_surf, text_rect)
        
        phase=["",
               "Faza 1: ruch",
               "Faza 2: wybor akcji",
               "Faza 3: wybor celu akcji"
               ]
        
        text_surf, text_rect = text(str(phase[turn % 4]),mfont,WHITE)
        text_rect.center = (500,80)
        map.blit(text_surf, text_rect)

        for i in range (2):
            if i == 1:
                i = player_1
                j = spells_indx
                k = potions_indx
                l = 130
                m = wand_1
            else:
                i = player_2
                j = spells_indy
                k = potions_indy
                l = 870
                m = wand_2

            text_surf, text_rect = text(i.name + " jest uczniem " + str(i.year) + ".",sfont,WHITE)
            text_rect.center = (l,130)
            map.blit(text_surf, text_rect)

            text_surf, text_rect = text("klasy Hogwartu, jego dom to " + i.house + ".",sfont,WHITE)
            text_rect.center = (l,150)
            map.blit(text_surf, text_rect)

            text_surf, text_rect = text("Posiada rozdzke o dlugosci " + str(m.lenght) + " cali,",sfont,WHITE)
            text_rect.center = (l,170)
            map.blit(text_surf, text_rect)

            text_surf, text_rect = text("ktorej rdzen to " + m.core + ".",sfont,WHITE)
            text_rect.center = (l,190)
            map.blit(text_surf, text_rect)

            text_surf, text_rect = text("Zycie: " + str(i.health) + "/" + str(i.maxh),sfont,WHITE)
            text_rect.center = (l,230)
            map.blit(text_surf, text_rect)

            text_surf, text_rect = text("Magia: " + str(i.magic) + "/" + str(i.maxm),sfont,WHITE)
            text_rect.center = (l,250)
            map.blit(text_surf, text_rect)

            text_surf, text_rect = text(str("Aktualnie wybrane zaklecie: " + str(spells[j].name)),sfont,WHITE)
            text_rect.center = (l,270)
            map.blit(text_surf, text_rect)

            if spells[j].name == "Avada Kedavra":
                text_surf, text_rect = text(str("Koszt/Obrazenia/leczenie zaklecia: "
                                       + str(spells[j].cost ) + "/" + 
                                       str(int(spells[j].dmg)) + "/" +
                                       str(int(i.modspell * spells[j].heal))),sfont,WHITE)
            else:
                text_surf, text_rect = text(str("Koszt/Obrazenia/leczenie zaklecia: "
                                       + str(spells[j].cost ) + "/" + 
                                       str(int(i.modspell * spells[j].dmg)) + "/" +
                                       str(int(i.modspell * spells[j].heal))),sfont,WHITE)
            text_rect.center = (l,290)
            map.blit(text_surf, text_rect)

            text_surf, text_rect = text(("Efekt zaklecia: " + spells[j].efect),sfont,WHITE)
            text_rect.center = (l,310)
            map.blit(text_surf, text_rect)

            text_surf, text_rect = text(str("Aktualnie wybrany eliksir: " + str(potions[k].name)),sfont,WHITE)
            text_rect.center = (l,330)
            map.blit(text_surf, text_rect)

            text_surf, text_rect = text(str("Ilosc/Obrazenia/leczenie eliksiru: "
                                       + str(i.potion_number[k] ) + "/" + 
                                       str(int(i.modpotion * potions[k].dmg)) + "/" +
                                       str(int(i.modpotion * potions[k].heal))),sfont,WHITE)
            text_rect.center = (l,350)
            map.blit(text_surf, text_rect)

            text_surf, text_rect = text(("Efekt eliksiru: " + potions[k].efect),sfont,WHITE)
            text_rect.center = (l,370)
            map.blit(text_surf, text_rect)


        button("Reset", 850, 450, 150, 50, GREEN,game)
        button("Reset postaci",850,500,150,50,ORANGE,preparation)
        button("Menu",850,550,150,50,RED,exit)

        pd.update()
        fpsClock.tick(FPS)
        
        for e in pg.event.get():
            
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            
            if e.type == KEYDOWN:
                if turn % 4 == 0:
                    if e.key == K_RETURN:
                        turn = turn + 1

                if turn % 4 == 1 :
                    if e.key == K_RIGHT or e.key == K_LEFT:
                        turn = turn + 1
                                     
                    if e.key == K_UP:
                        if x.move == 1:
                            if x.pos[0] == x_wand.pos[0]:
                                x_wand.pos[0] = max(x.pos[0] - 1,0)
                                x_wand.pos[3] = x_wand.pos[0] * 100 + 100
                            x.pos[0] = max(x.pos[0] - 1,0)
                            x.pos[3] = max(100,x.pos[2] - 100)
                        else:
                            x.move = 1
                        
                        turn = turn + 1
                            
                    if e.key == K_DOWN:
                        if x.move == 1:
                            if x.pos[0] == x_wand.pos[0]:
                                x_wand.pos[0] = min(x.pos[0] + 1,3)
                                x_wand.pos[3]= x_wand.pos[0] * 100 + 100
                            x.pos[0] = min(x.pos[0]+1,3)
                            x.pos[3] = min(400,x.pos[2] + 100)
                        else:
                            x.move = 1
                        
                        turn = turn + 1
                        '''
                if turn % 8 == 5:
                        
                    if e.key == K_RIGHT or e.key == K_LEFT:
                        turn = turn + 1
                                
                    if e.key == K_UP:
                        if x.move == 1:
                            if x.pos[0] == wand_2.pos[0]:
                                wand_2.pos[0] = max(x.pos[0] - 1,0)
                                wand_2.pos[3] = wand_2.pos[0] * 100 + 100
                            x.pos[0] = max(x.pos[0] - 1,0)
                            ny_y = max(100,x.pos[2] - 100)
                        else:
                            x.move = 1
                        
                        turn = turn + 1
                        
                    if e.key == K_DOWN:
                        if x.move == 1:
                            if x.pos[0] == wand_2.pos[0]:
                                wand_2.pos[0] = min(x.pos[0] + 1,3)
                                wand_2.pos[3] = wand_2.pos[0] * 100 + 100
                            x.pos[0] = min(x.pos[0] + 1,3)
                            ny_y = min(400,x.pos[2] + 100)

                        turn = turn + 1
                        '''
                if turn % 8 == 2:
                    if e.key == K_q:
                        if (x.magic >= spells[spells_indx].cost and player_1.pos[0] == wand_1.pos[0]) or spells[spells_indx].name == "Brak":
                            if turn == 2:
                                turn = turn + 1
                            attack = 1
                            turn = turn+ 1
                    if e.key == K_w:
                       spells_indx = (spells_indx - 1)%(x.year + 2) 
                    if e.key == K_e:
                        spells_indx = (spells_indx + 1)%(x.year + 2)

                    if e.key == K_a:
                        if x.potion_number[potions_indx] > 0:
                            if turn == 2:
                                turn = turn + 1
                            attack = 2
                            turn = turn + 1
                    if e.key == K_s:
                        potions_indx = (potions_indx - 1)% int((x.year+1)/2)
                    if e.key == K_d:
                        potions_indx = (potions_indx + 1)% int((x.year+1)/2)

                if turn % 8 == 6:
                    if e.key == K_q:
                        if (x.magic >= spells[spells_indy].cost and player_2.pos[0] == wand_2.pos[0]) or spells[spells_indy].name == "Brak" :
                            attack = 1
                            turn = turn + 1
                    if e.key == K_w:
                       spells_indy = (spells_indy - 1)% (x.year + 2) 
                    if e.key == K_e:
                        spells_indy = (spells_indy +1 )% (x.year+2)

                    if e.key == K_a:
                        if x.potion_number[potions_indy] > 0:
                            attack = 2
                            turn = turn + 1
                    if e.key == K_s:
                        potions_indy = (potions_indy - 1)% int((x.year+1)/2)
                    if e.key == K_d:
                        potions_indy = (potions_indy + 1)% int((x.year+1)/2)

                if turn % 8 == 3:

                    if e.key == K_1:
                        player_1.next[4]=0
                        attack2 = 1
                        

                    if e.key == K_2:
                        player_1.next[4]=1
                        attack2 = 1

                    if e.key == K_3:
                        player_1.next[4]=2
                        attack2 = 1

                    if e.key == K_4:
                        player_1.next[4]=3
                        attack2 = 1
            
                    if e.key == K_RETURN:
                        if attack2 == 1:
                            burn(x,y)
                            toxic(x,y)
                            if attack == 1:
                                action(x,y,spells[spells_indx],player_1.next[4],wand_1,wand_2)
                            else:
                                action2(x,y,potions[potions_indx],potions_indx,player_1.next[4])
                            turn = turn + 1
                            attack2 = 0
                            player_1.next[4] = 4


                if turn % 8 == 7:
                    
                    if e.key == K_1:
                        player_2.next[4]=0
                        attack2 = 1
                        

                    if e.key == K_2:
                        player_2.next[4]=1
                        attack2 = 1

                    if e.key == K_3:
                        player_2.next[4]=2
                        attack2 = 1

                    if e.key == K_4:
                        player_2.next[4]=3
                        attack2 = 1
            
                    if e.key == K_RETURN:
                        if attack2 == 1:
                            burn(x,y)
                            toxic(x,y)
                            if attack == 1:
                                action(x,y,spells[spells_indy],player_2.next[4],wand_2,wand_1)
                            else:
                                action2(x,y,potions[potions_indy],potions_indy,player_2.next[4])
                            turn = turn + 1
                            attack2 = 0
                            player_2.next[4] = 4
                     

                if e.key == K_o:
                    #pg.mixer.music.pause()
                    print("ok")
                if e.key == K_i:        
                    #pg.mixer.music.unpause()
                    print("ok")

        
main()

from player import Player
from spell import Spell
from wand import Wand
from potion import Potion
from svg import Parser, Rasterizer
import pygame, sys, random, time, copy
from pygame.locals import *
pg=pygame
pd=pg.display
pg.init()
FPS = 16 
fpsClock = pygame.time.Clock()
turn = 0
press = 0
index = 0
attack = 1
attack2 = 0
choosed_action =""
player_1 = Player("Jan",7,"Gryffindor")
player_2 = Player("Niejan",7,"Gryffindor")    
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
             Potion("Toxic potion",0,10,0,"Trujace opary"),
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

def load_svg(filename, scale=None, size=None, clip_from=None, fit_to=None):
    """Returns Pygame Image object from rasterized SVG
    If scale (float) is provided and is not None, image will be scaled.
    If size (w, h tuple) is provided, the image will be clipped to specified size.
    If clip_from (x, y tuple) is provided, the image will be clipped from specified point.
    If fit_to (w, h tuple) is provided, image will be scaled to fit in specified rect.
    """
    svg = Parser.parse_file(filename)
    tx, ty = 0, 0
    if size is None:
        w, h = svg.width, svg.height
    else:
        w, h = size
        if clip_from is not None:
            tx, ty = clip_from
    if fit_to is None:
        if scale is None:
            scale = 1
    else:
        fit_w, fit_h = fit_to
        scale_w = float(fit_w) / svg.width
        scale_h = float(fit_h) / svg.height
        scale = min([scale_h, scale_w])
    rast = Rasterizer()
    req_w = int(w * scale)
    req_h = int(h * scale)
    buff = rast.rasterize(svg, req_w, req_h, scale, tx, ty)
    image = pygame.image.frombuffer(buff, (req_w, req_h), 'RGBA')
    return image

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
            button("dalej",450,550,100,50,BLUE,how,["images/how2.jpg"])
        else:
            button("powrot",450,0,100,50,BLUE,how,["images/how.jpg"])
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
        button("podstawy",900,100,100,100,RED,how,["images/how.jpg"])
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
        button("podstawy",900,100,100,100,RED,how,["images/how.jpg"])
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
    obraz=pg.image.load("images/file.jpg")

    while True:
        for e in pg.event.get():
            
            if e.type == pg.QUIT:
                sys.exit(0)
            if e.type == KEYDOWN:
                
                if e.key == K_o:
                    #pg.mixer.music.pause()
                    print("ok")
                
                if e.key == K_i:        
                    #pg.mixer.music.unpause()
                    print("ok")

        map.blit(obraz,(0,0))

        button("Graj", 400, 300, 200, 100, GREEN, preparation)
        button("Jak grac", 400, 400, 200, 100, YELLOW, how,["images/how.jpg"])
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
        obraz = pg.image.load("images/file.jpg")
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
        obraz = pg.image.load("images/file.jpg")
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

def choose_action(action):
    global choosed_action, turn 
    turn = turn + 1
    choosed_action = action

def phase_1(x,x_wand,i):
    global turn
    if x.move == 1:
        if x.pos[0] == x_wand.pos[0]:
            x_wand.pos[0] = min(max(x.pos[0] + i,0),3)
            x_wand.pos[3] = x_wand.pos[0] * 100 + 100
            x.pos[0] = min(max(x.pos[0] + i,0),3)
            x.pos[3] = x.pos[2] - min(max(100,x.pos[2] + i * 100),400)
    else:
        x.move = 1
    if turn == 1:
        turn = 6
    else:
        turn = turn + 1

def phase_2(x,spels,x_wand):
    global choosed_action,turn,attack
    if choosed_action == "Zaklęcie":
        if (x.magic >= spells[x.spells_ind].cost and x.pos[0] == x_wand.pos[0]) or spells[x.spells_ind].name == "Brak":
            attack = 1
            turn = turn+ 1
    if choosed_action == "Eliksir":
        if x.potion_number[x.potions_ind] > 0:
                            attack = 2
                            turn = turn + 1


def phase_2_1(x,i):
    x.spells_ind = (x.spells_ind + i)%(x.year + 2)
def phase_2_2(x,i):
    x.potions_ind = (x.potions_ind + i)% int((x.year + 1)/2)
def phase_2_3(x,i):
    global choosed_action
    if choosed_action == "Zaklęcie":
        phase_2_1(x,i)
    if choosed_action == "Eliksir":
        phase_2_2(x,i)

def phase_3(x,y,spells,potions,x_wand,y_wand):
    global attack2,turn,choosed_action
    if spells[x.spells_ind].dmg == 0 and choosed_action == "Zaklęcie":
        attack2 = 1
    if potions[x.potions_ind].dmg == 0 and choosed_action == "Eliksir":
        attack2 = 1
    if attack2 == 1:
        burn(x,y)
        toxic(x,y)
        if attack == 1:
            action(x,y,spells[x.spells_ind],x.next[4],x_wand,y_wand)
        else:
            action2(x,y,potions[x.potions_ind],x.potions_ind,x.next[4])
        turn = turn + 1
        attack2 = 0
        x.next[4] = 4
def phase_3_1(x,i):
    global attack2
    x.next[4]=i
    attack2 = 1

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
    global turn, attack,attack2 
    turn = 0 
    attack = 1
    attack2 = 0 
    x_x = 290
    x_y = 220
    wx_x = x_x + 98
    y_x = 630
    y_y = 220
    wy_x = y_x - 60
    player_1.pos[1] = x_x
    player_1.pos[2] = x_y
    player_1.pos[3] = 0
    player_2.pos[1] = y_x
    player_2.pos[2] = y_y
    player_2.pos[3] = 0
    spells_indx = 0
    spells_indy = 0
    potions_indx = 0
    potions_indy = 0
    wand_p1 = pg.image.load("images/wand.png")
    wand_p2 = pg.image.load("images/wand1.png")
    board = pg.image.load("images/board.png")
    for x in range(len(potions)):
        player_1.potion_number.append(potions[x].number + int(player_1.year / 2))
        player_2.potion_number.append(potions[x].number + int(player_2.year / 2))
    image = pg.image.load(player_1.imgs())
    image2 = pg.image.load(player_2.imgs())
    image3 = load_svg("images/scroll-152864.svg",1.55)
    image4 = load_svg("images/scrolls-34607.svg",0.8,(400,600))
    flame_imgs=["images/Flame_A.png",
                "images/Flame_B.png",
                "images/Flame_C.png",
                "images/Flame_D.png",
                "images/Flame_E.png",
                "images/Flame_F.png",
                "images/Flame_G.png",
                "images/Flame_H.png"]
    shield_imgs=[]
    for i in range(1,33):
        shield_imgs.append("images/shield_" + str(i) + ".png")
    animations_count = 0
    animations_count2 = 0

    while 1:

        
        map.fill(BLACK)
        #map.blit(board,(270,100))
        #map.blit(board,(610,100))

        if (turn % 12 < 6) :
            x = player_1
            x_wand = wand_1
            y = player_2
            y_wand = wand_2
        else:
            x = player_2
            x_wand = wand_2
            y = player_1
            y_wand = wand_1

        if (x.health <= 0 and y.health > 0):
            resoult(y)
        if (y.health <= 0 and x.health > 0):
            resoult(x)
        if  x.health <=0 and y.health <= 0:
            resoult()
        
        map.blit(image3,(-260,-160))
        map.blit(image3,(480,-160))
        if turn % 6 > 0  and turn % 6<5:
            map.blit(image4,(0,300))

        text_surf, text_rect = text(str("Tura gracza: " + x.name),mfont,WHITE)
        text_rect.center = (500,50)
        map.blit(text_surf, text_rect)
      
        phase=["",
               "Faza 1: ruch",
               "Faza 2: wybor akcji",
               "Faza 2: wybor akcji",
               "Faza 3: wybor celu akcji",
               ""
               ]
        
        text_surf, text_rect = text(str(phase[turn % 6]),mfont,WHITE)
        text_rect.center = (500,80)
        map.blit(text_surf, text_rect)
        #if turn % 5 > 1 :
         #   button("powrót",200,450,50,50,RED)
        if turn % 6 == 1:
            button("W górę",30,330,200,50,ORANGE,phase_1,[x,x_wand,-1])
            button("Zostań w miejscu",30,380,200,50,ORANGE, phase_1,[x,x_wand,0])
            button("W dół",30,430,200,50,ORANGE,phase_1,[x,x_wand,1])

        if turn % 6 == 2:
            button("Zaklęcie",30,330,200,50,ORANGE,choose_action,["Zaklęcie"])
            button("Eliksir",30,430,200,50,ORANGE,choose_action,["Eliksir"])
        if turn % 6 == 3:
            button("P",20,380,50,50,ORANGE,phase_2_3,[x,-1])
            button("D",220,380,50,50,ORANGE,phase_2_3,[x,1])
            button("Zatwierdź",30,430,200,50,ORANGE,phase_2,[x,spells,x_wand])
        if turn % 6 == 4:
            if (spells[x.spells_ind].dmg != 0 and choosed_action == "Zaklęcie") or (potions[x.potions_ind].dmg != 0 and choosed_action == "Eliksir"):
                button("1",20,380,50,50,ORANGE,phase_3_1,[x,0])
                button("2",90,380,50,50,ORANGE,phase_3_1,[x,1])
                button("3",150,380,50,50,ORANGE,phase_3_1,[x,2])
                button("4",220,380,50,50,ORANGE,phase_3_1,[x,3])
            else:
                attack2 = 1
            button("Zatwierdź",30,430,200,50,ORANGE,phase_3,[x,y,spells,potions,x_wand,y_wand])

        for i in range(4):
            for j in range(2):
                if j == 0:
                    j = y
                    l = x
                else:
                    j = x
                    l = y
                flame_img = pg.image.load(flame_imgs[animations_count % len(flame_imgs)])
                if i == j.next[0] or i == j.next[1]:
                    for k in range (5):
                        map.blit(flame_img,(j.pos[1] + 20 * k - 40,i*100 +100))
                elif i == j.next[2] or i == j.next[3]:
                    button("",j.pos[1] - 25,i*100+ 100,150,100,GREEN)
                else:
                    button("",j.pos[1],i*100 +100,100,100,WHITE)
                
                if i == j.next[4] :
                    button("",l.pos[1],i*100+100,100,100,ORANGE)
        
        
        if x.shield ==1:
            shield_img = pg.image.load(shield_imgs[animations_count2 % len(shield_imgs)])
            map.blit(shield_img,(x.pos[1],x.pos[2] -15))
        if y.shield ==1:
            shield_img = pg.image.load(shield_imgs[animations_count2 % len(shield_imgs)])
            map.blit(shield_img,(y.pos[1],y.pos[2] -15))
        if turn % 6 ==5:
            animations_count2 = animations_count2 + 1
            shift =(y.pos[3] )/31
            #shift_x=(x.pos[1] - y.pos[1])/31
            #shift_y=(x.pos[2] - y.pos[2])/31
            #pg.draw.line(map,RED,[x.pos[1] - shift_x * animations_count2,x.pos[2] - shift_y * animations_count2],
             #            [x.pos[1] - shift_x * animations_count2 +20,x.pos[2] - shift_y * animations_count2 +20],3)
            y.pos[2] = max(min(y.pos[2] -shift,420),120)
            y_wand.pos[2] =max(min(y_wand.pos[2] - shift,400),100)
            if animations_count2 == 31:
                turn = turn +1
                animations_count2 =-1
        animations_count = animations_count + 1
        #if turn % 10 == 1 :
         #   player_1.pos[2] = player_1.pos[3]
          #  wand_1.pos[2] = wand_1.pos[3]

        map.blit(image,(x_x + 10,player_1.pos[2]))
        map.blit(wand_p1,(wx_x,wand_1.pos[2]))
        
        #if turn % 10 == 6 :
         #   player_2.pos[2] = player_2.pos[3]
          #  wand_2.pos[2] = wand_2.pos[3]

        map.blit(image2,(y_x + 10 ,player_2.pos[2]))
        map.blit(wand_p2,(wy_x,wand_2.pos[2]))
        
        for i in range (2):
            if i == 1:
                i = player_1
                l = 130
                m = wand_1
            else:
                i = player_2
                l = 870
                m = wand_2
            i.create_tabs(m)
        
            for n  in range (len(i.tab_1)):
                text_surf, text_rect = text(i.tab_1[n],sfont,WHITE)
                text_rect.center = (l,110 + 20 * n)
                map.blit(text_surf, text_rect)
        if turn % 6 == 3:
            x.create_tabs2(spells[x.spells_ind],potions[x.potions_ind])    
            temp_tab = []
            if choosed_action == "Zaklęcie":
                temp_tab = x.tab_2
            if choosed_action == "Eliksir":
                temp_tab = x.tab_3
            for n in range(len(temp_tab)):
                text_surf, text_rect = text(temp_tab[n],font,WHITE)
                text_rect.center = (130,350 + 20 * n)
                map.blit(text_surf, text_rect)

        if turn % 12 == 0:
            text_surf, text_rect = text(str("tura gracza: " + player_1.name),lfont,BLUE)
            text_rect.center = (500,300)
            map.blit(text_surf, text_rect)
        if turn % 12 ==6:
            text_surf, text_rect = text(str("tura gracza: " + player_2.name),lfont,BLUE)
            text_rect.center = (500,300)
            map.blit(text_surf, text_rect)

        button("Reset", 850, 450, 150, 50, GREEN,game)
        button("Reset postaci",850,500,150,50,ORANGE,preparation)
        button("Menu",850,550,150,50,RED,menu)

        pd.flip()
        fpsClock.tick(FPS)
        
        for e in pg.event.get():
            
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            
            if e.type == KEYDOWN:
                if turn % 6 == 0 :
                    if e.key == K_RETURN:
                        turn =turn +1
                #if turn % 6 ==5:
                 #   if e.key == K_RETURN:
                  #      x.pos[2] = max(min(x.pos[2] -shift,400),120)
                   #     x_wand.pos[2] =max(min(x_wand.pos[2] - shift,400),100)
                    #    animations_count2 = -1
                     #   turn = turn + 1

                if turn % 6 == 1 :
                    if e.key == K_RIGHT or e.key == K_LEFT:
                        phase_1(x,x_wand,0)
                    if e.key == K_UP:
                        phase_1(x,x_wand,-1)
                    if e.key == K_DOWN:
                        phase_1(x,x_wand,1)

                if turn % 6 == 3:
                    if e.key == K_q:
                        phase_2(x,spells,x_wand)                        
                    if e.key == K_w:
                        phase_2_3(x,-1) 
                    if e.key == K_e:
                        phase_2_3(x,1)
   
                if turn % 6 == 4:

                    if e.key == K_1:
                        phase_3_1(x,0)
                    if e.key == K_2:
                        phase_3_1(x,1)
                    if e.key == K_3:
                        phase_3_1(x,2)
                    if e.key == K_4:
                        phase_3_1(x,3)
                    if e.key == K_RETURN:
                        phase_3(x,y,spells,potions,x_wand,y_wand)

                if e.key == K_o:
                    #pg.mixer.music.pause()
                    print("ok")
                if e.key == K_i:        
                    #pg.mixer.music.unpause()
                    print("ok")

        
main()

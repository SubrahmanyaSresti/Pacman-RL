import models
import pygame
pygame.init()

screen= pygame.display.set_mode((800,400))
pimg= pygame.image.load("player.png")
pimg = pygame.transform.scale(pimg, (30,30))
cimg=[pygame.transform.scale(pygame.image.load("c1.png"),(30,30)),pygame.transform.scale(pygame.image.load("c2.png"),(30,30)),pygame.transform.scale(pygame.image.load("c3.png"),(30,30))]
pygame.display.set_caption("Pacman in diguise")

def player(img,x,y):
    screen.blit(img,(x,y))
def catchers(img,x,y):
    for i in range(len(x)):
        screen.blit(img[i],(x[i],y[i]))
        
catchermodel= models.CatcherModel()
playermodel= models.PlayerModel()
catchermodel.loadmodel()
playermodel.loadmodel()
catchermodel.game_mode()
playermodel.game_mode()

def caught(cx,cy,x,y):
    if x in cx and y in cy:
        return True
    else:
        return False
def make_a_move(i,cnumber,cx,cy):
            if(i==3):
                if(cx[cnumber]==20):
                    cx[cnumber]=780
                else : cx[cnumber]-=20
            if(i==1):
                if(cx[cnumber]==780):
                    cx[cnumber]=20
                else : cx[cnumber]+=20
            if(i==2):
                if(cy[cnumber]==380):
                    cy[cnumber]=20
                else : cy[cnumber]+=20
            if(i==0):
                if(cy[cnumber]==20):
                    cy[cnumber]=380
                else : cy[cnumber]-=20
            return cx,cy 
def make_p_move(i,px,py):
            if(i==3):
                if(px==20):
                    px=780
                else : px-=20
            if(i==1):
                if(px==780):
                    px=20
                else : px+=20
            if(i==2):
                if(py==380):
                    py=20
                else : py+=20
            if(i==0):
                if(py==20):
                    py=380
                else : py-=20
            return px,py

def catcher_move(x,y,cx,cy):
    a=[x,y]
    for i in range(len(cx)):
        a.append(cx[i])
        a.append(cy[i])
    m= catchermodel.move([a])
    for i in range(len(m)):
        cx,cy= make_a_move(m[i],i,cx,cy)
    return a,m,cx,cy
def player_move(x,y,cx,cy):
    a=[x,y]
    for i in range(len(cx)):
        a.append(cx[i])
        a.append(cy[i])
    m= playermodel.move([a])
    px,py= make_p_move(m,x,y)
    return a,m,px,py
Running= True
while Running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running= False
    num_of_episodes=1
    for _ in range(num_of_episodes):    
        px= 400
        py= 200     
        player(pimg,px,py)  
        cx=[20,20,780]
        cy=[380,20,20]
        catchers(cimg,cx,cy)
        count=0
        game_not_over= True
        while count<=200 and game_not_over:
            screen.fill((0,0,0))
            pa,pm,px,py= player_move(px,py,cx,cy)
            player(pimg,px,py) 
            ca,cm,cx,cy= catcher_move(px,py,cx,cy)
            catchers(cimg,cx,cy)
            if(caught(cx,cy,px,py)):
                playermodel.addata(pa,pa,True,False,pm)
                catchermodel.addata(ca,ca,True,False,cm)
                playermodel.train()
                catchermodel.train()
                font = pygame.font.Font('freesansbold.ttf', 32)
                text= font.render("CATCHER WON",True,(255,0,0))
                screen.blit(text,(200,200))
                game_not_over=False   
            if(count==200):
                playermodel.addata(pa,pa,False,True,pm)
                catchermodel.addata(ca,ca,False,True,cm)
                playermodel.train()
                catchermodel.train()
                font = pygame.font.Font('freesansbold.ttf', 32)
                text= font.render("RUNNER WON ",True,(0,255,0))
                screen.blit(text,(200,200))
            count+=1
            pygame.display.update()
    playermodel.savemodel()
    catchermodel.savemodel()
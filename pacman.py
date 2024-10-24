import pygame
import models
catchermodel= models.CatcherModel()
catchermodel.game_mode()
pygame.init()

screen= pygame.display.set_mode((800,400))

pimg= pygame.image.load("player.png")
pimg = pygame.transform.scale(pimg, (30,30))
px= 400
py= 200

cimg=[pygame.transform.scale(pygame.image.load("c1.png"),(30,30)),pygame.transform.scale(pygame.image.load("c2.png"),(30,30)),pygame.transform.scale(pygame.image.load("c3.png"),(30,30))]

def player(img,x,y):
    screen.blit(img,(x,y))
def catchers(img,x,y):
    for i in range(len(x)):
        screen.blit(img[i],(x[i],y[i]))
def caught(cx,cy,x,y):
    if x in cx and y in cy:
        return True
    else:
        return False
def make_a_move(i,cnumber):
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

def catcher_move(x,y,cx,cy):
    a=[x,y]
    for i in range(len(cx)):
        a.append(cx[i])
        a.append(cy[i])
    m= catchermodel.move([a])
    for i in range(len(m)):
        make_a_move(m[i],i)
    
        
cx=[20,20,780]
cy=[380,20,20]
pygame.display.set_caption("Pacman in diguise")
running= True
count=0
while running :
    screen.fill((0,0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running= False
        if i.type==pygame.KEYDOWN:
            
            if(i.key==pygame.K_LEFT):
                catcher_move(px,py,cx,cy)
                count+=1
                if(px==20):
                    px=780
                else : px-=20
            if(i.key==pygame.K_RIGHT):
                catcher_move(px,py,cx,cy)
                count+=1
                if(px==780):
                    px=20
                else : px+=20
            if(i.key==pygame.K_DOWN):
                catcher_move(px,py,cx,cy)
                count+=1
                if(py==380):
                    py=20
                else : py+=20
            if(i.key==pygame.K_UP):
                catcher_move(px,py,cx,cy)
                count+=1
                if(py==20):
                    py=380
                else : py-=20
    

    player(pimg,px,py)
    catchers(cimg,cx,cy)
    if caught(cx,cy,px,py):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text= font.render("GAME OVER",True,(255,0,0))
        screen.blit(text,(200,200))
        
    if(count>=200):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text= font.render("YOU WON ! ",True,(0,255,0))
        screen.blit(text,(200,200))
    pygame.display.update()
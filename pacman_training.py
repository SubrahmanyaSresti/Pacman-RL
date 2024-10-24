import lstmmodel
catchermodel= lstmmodel.CatcherModel()
playermodel= lstmmodel.PlayerModel()
catchermodel.loadmodel()
playermodel.loadmodel()
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
    
num_of_episodes=30
for _ in range(num_of_episodes):    
    px= 400
    py= 200       
    cx=[20,20,780]
    cy=[380,20,20]
    count=0
    game_not_over= True
    while count<=200 and game_not_over:
        pa,pm,px,py= player_move(px,py,cx,cy)
        ca,cm,cx,cy= catcher_move(px,py,cx,cy)
        if(caught(cx,cy,px,py)):
            playermodel.addata(pa,pa,True,False,pm)
            catchermodel.addata(ca,ca,True,False,cm)
            print("CATCHER WON!!!!")
            playermodel.train()
            catchermodel.train()
            game_not_over=False    
        if(count==200):
            playermodel.addata(pa,pa,False,True,pm)
            catchermodel.addata(ca,ca,False,True,cm)
            playermodel.train()
            catchermodel.train()
        count+=1
playermodel.savemodel()
catchermodel.savemodel()
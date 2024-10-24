import tensorflow as tf
from keras.layers import Dense, LSTM
from keras.models import Sequential
import numpy as np

class PlayerModel:
    def __init__(self):
        self.modl= Sequential([
            LSTM(32,return_sequences=True,input_shape=(8,)),
            Dense(32,activation="relu"),
            LSTM(32,return_sequences=True),
            Dense(32,activation="relu"),
            Dense(16,activation="relu"),
            Dense(4,activation="tanh")
        ])
        self.modl.compile(optimizer="adam",loss="mean_squared_error",metrics=["accuracy"])
        self.arrx=[]
        self.arry=[]
        self.epsilon= 1.0
    def addata(self,arrx,arry,cwin,pwin,move=None):
        if(cwin):
            self.arrx[-1]=arrx
            [ary]= self.modl.predict(np.array([arrx]))
            ary[move]= -1
            self.arry[-1]=ary
        elif(pwin):
            self.arrx[-1]=arrx
            [ary]= self.modl.predict(np.array([arrx]))
            ary[move]= -1
            self.arry[-1]=ary
        else:
            self.arrx.append(arrx)
            self.arry.append(arry)
    def train(self):
        self.modl.fit(x=np.array(self.arrx),y=np.array(self.arry),epochs=10)
        self.arrx=[]
        self.arry=[]
    def savemodel(self):
        self.modl.save("player_model")
    def loadmodel(self):
        self.modl= tf.keras.models.load_model("player_model")
    def move(self,movearray):
        move=-1
        [ar]= self.modl.predict(np.array(movearray))
        trarray= ar
        if(np.random.uniform(0.0,1.0)<self.epsilon):
            move= np.random.randint(0,4)
        else:   
            move= np.argmax(ar)
        self.epsilon= self.epsilon  - 0.001*self.epsilon
        trarray[move]=0.0001 
        [temp]=movearray
        self.addata(arrx=temp,arry=trarray,cwin=False,pwin=False)
        return move
    def game_mode(self):
        self.epsilon= 0.1
    

class CatcherModel:
    def __init__(self):
        self.modl= Sequential([
            LSTM(128,return_sequences=True,input_shape=(8,)),
            Dense(128,activation="relu"),
            LSTM(64,return_sequences=True),
            Dense(64,activation="relu"),
            LSTM(64,return_sequences=True),
            Dense(32,activation="relu"),
            LSTM(32,return_sequences=True),
            Dense(32,activation="relu"),
            LSTM(32,return_sequences=True),
            Dense(32,activation="relu"),
            Dense(12,activation="tanh")
        ])
        self.modl.compile(optimizer="adam",loss="mean_squared_error",metrics=["accuracy"])
        self.arrx=[]
        self.arry=[]
        self.epsilon= 1.0
    def addata(self,arrx,arry,cwin,pwin,move=None):
        if(cwin):
            self.arrx[-1]=arrx
            [ary]= self.modl.predict(np.array([arrx]))
            ary[move[0]]= 1
            ary[move[1]+4]= 1
            ary[move[2]+8]= 1
            self.arry[-1]=ary
            self.modl.fit(x=np.array(self.arrx),y=np.array(self.arry),epochs=40)
        elif(pwin):
            self.arrx[-1]=arrx
            [ary]= self.modl.predict(np.array([arrx]))
            ary[move[0]]= -1
            ary[move[1]+4]= -1
            ary[move[2]+8]= -1
            self.arry[-1]=ary
        else:
            self.arrx.append(arrx)
            self.arry.append(arry)
    def train(self):
        self.modl.fit(x=np.array(self.arrx),y=np.array(self.arry),epochs=20)
        self.arrx=[]
        self.arry=[]
        self.epsilon= self.epsilon - 0.01*self.epsilon
    def savemodel(self):
        self.modl.save("catcher_model")
    def loadmodel(self):
        self.modl= tf.keras.models.load_model("catcher_model")
        self.modl.compile(optimizer="adam",loss="mean_squared_error",metrics=["accuracy"])
        self.arrx=[]
        self.arry=[]
    def move(self,movearray):
        move=[-1,-1,-1]
        [ar]= self.modl.predict(np.array(movearray))
        trainarr= ar
        if(np.random.uniform(0.0,1.0)<self.epsilon):
            move[0]= np.random.randint(0,4)
            move[1]= np.random.randint(0,4)
            move[2]= np.random.randint(0,4)
        else:   
            move[0]= np.argmax(ar[0:4])
            move[1]= np.argmax(ar[4:8])-4
            move[2]= np.argmax(ar[8:12])-8
        trainarr[move[0]]= -0.001
        trainarr[move[1]+4]= -0.001
        trainarr[move[2]+8]= -0.001
        [temp]=movearray
        self.addata(temp,trainarr,False,False)
        #self.epsilon= self.epsilon - 0.001*self.epsilon
        return move
    def game_mode(self):
        self.epsilon=0.1
        

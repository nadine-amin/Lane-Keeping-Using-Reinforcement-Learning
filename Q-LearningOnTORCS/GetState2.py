import itertools

#Discrete Speed Values
Speed=[0,20,40,80,85,90,95,100,105,110,115,120,125,130,140,160]
#Discrete Distance Values
Distance=[-1,0,5,10,20,30,40,50,60,70,80,90,100,120,140,200]

#Generate Speed Value Combinations 0000 to 1111
SpeedList  = list(itertools.product([0,1], repeat=4))
#Generate Distance Value Combinations 0000 to 1111
DistList   = list(itertools.product([0,1], repeat=4))         


#Discretize The Continuous Speeds
def DiscSpeed(x): 
    if   x <10                 : y=0
    elif x >=10    and x<30    : y=20
    elif x >=30    and x<60    : y=40
    elif x >=60    and x<82.5  : y=80
    elif x >=82.5  and x<87.5  : y=85
    elif x >=87.5  and x<92.5  : y=90
    elif x >=92.5  and x<97.5  : y=95
    elif x >=97.5  and x<102.5 : y=100
    elif x >=102.5 and x<107.5 : y=105
    elif x >=107.5 and x<112.5 : y=110
    elif x >=112.5 and x<117.5 : y=115
    elif x >=117.5 and x<122.5 : y=120
    elif x >=122.5 and x<127.5 : y=125
    elif x >=127.5 and x<135   : y=130
    elif x >=135   and x<150   : y=140
    elif x >=150               : y=160
    return y

#Discretize The Continuous Distances
def DiscDist(y):
    if   y<0                 : x=-1
    elif y<2.5               : x=0
    elif y>=2.5  and y<7.5   : x=5    
    elif y>=7.5  and y<15    : x=10
    elif y>=15   and y<25    : x=20
    elif y>=25   and y<35    : x=30
    elif y>=35   and y<45    : x=40
    elif y>=45   and y<55    : x=50
    elif y>=55   and y<65    : x=60
    elif y>=65   and y<75    : x=70
    elif y>=75   and y<85    : x=80
    elif y>=85   and y<95    : x=90
    elif y>=95   and y<110   : x=100
    elif y>=110  and y<130   : x=120
    elif y>=130  and y<170   : x=140
    elif y>=170              : x=200
  
    return x


def State (speed,track,trackpos):
    #Takes as Inputs The Continuous Speed and Distance Semsor Readings
    #Averages Readings From Distance Sensors
    #Determines The Number of The Sensor With The Maximum Reading
    #Discretizes The Speed and Average Distance
    #Gets The Corresponding Binary Value of The Discretized Speed, Average Distance, anf The Maximum Sensor Number
    #Outputs The Binary State
    
    t7=(track[6]+track[7]+track[8])/float(3)
    t11=(track[10]+track[11]+track[12])/float(3)
    
    maxsensor=max(track[5],t7,track[9],t11,track[13])
    
    if   maxsensor==track[5] : z=[1,0,0]
    elif maxsensor==t7       : z=[1,1,0]
    elif maxsensor==track[9] : z=[0,1,0]
    elif maxsensor==t11      : z=[0,1,1]
    elif maxsensor==track[13]: z=[0,0,1]
    
    if   maxsensor==-1 and trackpos >0 : z=[0,0,0]
    elif maxsensor==-1 and trackpos <0 : z=[1,1,1]

    b=tuple(SpeedList[Speed.index(DiscSpeed(speed))])+tuple(z)+tuple(DistList[Distance.index(DiscDist(maxsensor))])
    return list(b)

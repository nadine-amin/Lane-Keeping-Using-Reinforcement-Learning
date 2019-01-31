import numpy
import re


def ComputeReward(speed,trackpos,angle,dist):
    #Computes The Reward to be Granted to The Agent in a Certain Scenario
    stuck=0
    SOOT=0
    OOT=0
        
    if numpy.abs(trackpos)>=0.8:
        OOT=1   
    elif numpy.abs(trackpos)>=0.5:
        SOOT=1    

    #Checks if Agent is Stuck    
    if (numpy.abs(angle) >= 45 and speed<10) or (speed<5 and dist>20):
        x=count()
        if x==25:
            stuck=1
            count.counter=0

    Rspeed=numpy.power((speed/float(120)),4)*0.3
    Rtrackpos=numpy.power(1/(float(numpy.abs(trackpos))+1),4)*1.1
    Rangle=numpy.power((1/((float(numpy.abs(angle))/40)+1)),4)*0.6
        
    if stuck==1:
        Reward=-2
    elif SOOT==1:
        Reward=(Rspeed+Rtrackpos+Rangle)*0.5
    elif OOT==1:
        if numpy.abs(trackpos) >=1.5:
            Reward=-1.5
        else:
            Reward=numpy.abs(trackpos)*(-1)
    else:
        Reward=Rspeed+Rtrackpos+Rangle
    return Reward


def FindQmaxIndex(state,table):
    #Returns The Index of The Acion With The Highest Q-Value For This State
    State = Stateindex(convert2string(state))
    maximum = table.iloc[State][1]

    ActionIndex=0
    for i in range (15):
        if table.iloc[State][i+1]>maximum: 
            maximum=table.iloc[State][i+1]
            ActionIndex=i

    return ActionIndex


#Converting Partitioned State Into State Index
def Stateindex(state):
    getnumbers = re.findall('\d+', state)

    values=[]
    for i in range (11):
        values.append(int(getnumbers[i]))
    
    output = "".join(map(str, values))
    del values
    
    return int(output, 2)

def convert2string(state):
    #Converts State into Partioned State in The Form:(0000)(000)(0000)
    b=tuple(state)
    x=str(b[0:4])+str(b[4:7])+str(b[7:11])
    return x


def count():
    #A Function That Counts The Number of Times it Gets Called
    count.counter += 1 
    return(count.counter)
count.counter = 0

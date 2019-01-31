import itertools
import pandas as pd
import numpy
import re

learning_rate = 0.1
Discount = 0.99
i = 1

def maketable():
    #Constructs The Qtable With Rows Equal to The Number of States and Columns Equal to The Number of Possible Actions + 1
    Statestring = []
    States= list(itertools.product([0,1], repeat=11))
    for i in range (2048):     #Partitioning States For Readability
        x1 = States[i][0:4]
        x2 = States[i][4:7]
        x3 = States[i][7:11]

        Statestring.append(str(x1)+str(x2)+str(x3))
    data = numpy.c_[Statestring,numpy.zeros((2048,15)) ]
    s = pd.DataFrame(data)
    return s


def update(state, Actionindex, Next_Qmax, NextState, Current_Reward ,qtable):
    #Updates The Q-value Corresponding to Certain State, Action, Reward and New State
    
    Statestring = convert2string(state)
    Current_Q = float(qtable.loc[Stateindex(Statestring)][Actionindex+1])
    NQmax = float(qtable.loc[Stateindex(convert2string(NextState))][Next_Qmax+1])

    qtable.iloc[Stateindex(Statestring),Actionindex+1]=Current_Q+learning_rate*(Current_Reward+Discount*NQmax-Current_Q) 
    

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


#Converts Partitioned State Into State Index
def Stateindex(state):
    getnumbers = re.findall('\d+', state)

    values=[]
    for i in range (11):
        values.append(int(getnumbers[i]))
    
    output = "".join(map(str, values))
    del values
    
    return int(output, 2)

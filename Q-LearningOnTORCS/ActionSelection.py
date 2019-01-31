import random
import re
import itertools

#Converting Partitioned State Into State Index
def Stateindex(state):
    getnumbers = re.findall('\d+', state)

    values=[]
    for i in range (11):
        values.append(int(getnumbers[i]))
    
    output = "".join(map(str, values))
    del values
    
    return int(output, 2)

#Selecting an Action
def Selectaction(state, table, MaxQIndex, laptime):
    eta = 0.1 - (0.0000001*count())
    egreedy = 0.4    
    
    Randomnum = random.uniform(0,1)
    
    if Randomnum < eta:
        #Hueristic Action
        return ['Hueristic', 'Hueristic']
    
    elif Randomnum <= (eta+float(egreedy)):
        #Random Action
        random_action_index = random.randint(0,14)
        random_action = ActionTable(random_action_index)
        return random_action

    elif Randomnum > (eta+egreedy):
        #Q-Table Action: choose the action with the highest q-value for this state
        Qtable_Action = ActionTable(MaxQIndex)
        return Qtable_Action  

#Determining Discrete-Valued Acceleration and Steering Given Action Index
def ActionTable(index):
    if index == 0:
        return [1, 0.5]
    elif index == 1:
        return [0, 0.5]
    elif index == 2:
        return [-1,0.5]
    elif index == 3:
        return [1, 0.1]
    elif index == 4:
        return [0, 0.1]
    elif index == 5:
        return [-1,0.1]
    elif index == 6:
        return [1, 0]
    elif index == 7:
        return [0, 0]
    elif index == 8:
        return [-1,0]
    elif index == 9:
        return [1, -0.1]
    elif index == 10:
        return [0, -0.1]
    elif index == 11:
        return [-1, -0.1]
    elif index == 12:
        return [1, -0.5]
    elif index == 13:
        return [0, -0.5]
    elif index == 14:
        return [-1,-0.5]

#Function That Counts its Calls
def count():
    count.counter += 1 
    return (count.counter)
count.counter = 0

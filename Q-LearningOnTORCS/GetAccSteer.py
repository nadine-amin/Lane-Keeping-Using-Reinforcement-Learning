#Discretizing Steering to 5 Values
def DiscSteer(steer):
    if (steer >= 0.33):
        Dsteer = 0.5
    elif ((steer < 0.33) and (steer > 0.02)):
        Dsteer = 0.1
    elif ((steer <= 0.02) and (steer >= -0.02)):
        Dsteer = 0
    elif ((steer < -0.02) and (steer > -0.33)):
        Dsteer = -0.1
    elif (steer <= -0.33):
        Dsteer = -0.5

    return Dsteer


#Discretizing Acceleration to 3 Values
def DiscAccel(accel):
    if (accel >= 0.33):
        Daccel = 1
    elif ((accel < 0.33) and (accel > -0.33)):
        Daccel = 0
    elif (accel <= -0.33):
        Daccel = -1

    return Daccel


#Determining Action Index Given Continuous-Valued Steering and Acceleration
def AccelSteer(accel, steer):
    #Discretize the steering and acceleration values
    S = DiscSteer(steer)
    A = DiscAccel(accel)

    if (A == 1):
        if (S == 0.5):
            ActionIndex = 0
        elif (S == 0.1):
            ActionIndex = 3
        elif (S == 0):
            ActionIndex = 6
        elif (S == -0.1):
            ActionIndex = 9
        elif (S == -0.5):
            ActionIndex = 12

    elif (A == 0):
        if (S == 0.5):
            ActionIndex = 1
        elif (S == 0.1):
            ActionIndex = 4
        elif (S == 0):
            ActionIndex = 7
        elif (S == -0.1):
            ActionIndex = 10
        elif (S == -0.5):
            ActionIndex = 13

    elif (A == -1):
        if (S == 0.5):
            ActionIndex = 2
        elif (S == 0.1):
            ActionIndex = 5
        elif (S == 0):
            ActionIndex = 8
        elif (S == -0.1):
            ActionIndex = 11
        elif (S == -0.5):
            ActionIndex = 14


    return ActionIndex
    

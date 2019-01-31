import msgParser

class CarControl(object):
    #A Class Holding All The Car Control Parameters
    #Performs Range Check on The Set Parameters

    def __init__(self, accel = 0.0, brake = 0.0, gear = 1, steer = 0.0, clutch = 0.0, focus = 0, meta = 0):
        
        self.parser = msgParser.MsgParser()
        
        self.actions = None
        
        self.accel = accel
        self.brake = brake
        self.gear = gear
        self.steer = steer
        self.clutch = clutch
        self.focus = focus
        self.meta = meta
    
    def toMsg(self):
        #Prepare Message to be Sent to the Server
        self.actions = {}
        
        self.actions['accel'] = [self.accel]
        self.actions['brake'] = [self.brake]
        self.actions['gear'] = [self.gear]
        self.actions['steer'] = [self.steer]
        self.actions['clutch'] = [self.clutch]
        self.actions['focus'] = [self.focus]
        self.actions['meta'] = [self.meta]
        
        return self.parser.stringify(self.actions)

    #Define Setters and Getters
    def setAccel(self, accel):
        self.accel = accel
    
    def getAccel(self):
        return self.accel
    
    def setBrake(self, brake):
        self.brake = brake
    
    def getBrake(self):
        return self.brake
    
    def setGear(self, gear):
        self.gear = gear
    
    def getGear(self):
        return self.gear
    
    def setSteer(self, steer):
        self.steer = steer
    
    def getSteer(self):
        return self.steer
    
    def setClutch(self, clutch):
        self.clutch = clutch
    
    def getClutch(self):
        return self.clutch
    
    def setMeta(self, meta):
        self.meta = meta
    
    def getMeta(self):
        return self.meta
        
        

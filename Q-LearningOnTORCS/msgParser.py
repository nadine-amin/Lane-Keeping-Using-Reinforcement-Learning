class MsgParser(object):
    #A Parser For Received UDP Messages and Building UDP Messages
    
    def __init__(self):
        
    def parse(self, str_sensors):
        #Returns a Dictionary With Tags and Values From The UDP Message
        sensors = {}
        
        b_open = str_sensors.find('(')
        
        while b_open >= 0:
            b_close = str_sensors.find(')', b_open)
            if b_close >= 0:
                substr = str_sensors[b_open + 1: b_close]
                items = substr.split()
                if len(items) < 2:
                    print "Problem parsing substring: ", substr
                else:
                    value = []
                    for i in range(1,len(items)):
                        value.append(items[i])
                    sensors[items[0]] = value
                b_open = str_sensors.find('(', b_close)
            else:
                print "Problem parsing sensor string: ", str_sensors
                return None
        
        return sensors
    
    def stringify(self, dictionary):
        #Builds a UDP Message From a Dictionary
        msg = ''
        
        for key, value in dictionary.items():
            if value != None and value[0] != None:
                msg += '(' + key
                for val in value:
                    msg += ' ' + str(val)
                msg += ')'
        
        return msg

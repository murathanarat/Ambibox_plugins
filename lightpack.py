import socket, time, imaplib, re, sys

class lightpack:
   
    def __init__(self, _host, _port, _ledMap, _apikey = None):
        self.host = _host
        self.port = _port
        self.ledMap = _ledMap
        self.apikey = _apikey        
    
    def __readResult(self): 
        total_data=[]
        data = self.connection.recv(8192)
        total_data.append(data)
        return ''.join(total_data)
        
    def getProfiles(self):
        cmd = 'getprofiles\n'
        self.connection.send(cmd)
        profiles = self.__readResult()
        return profiles.split(':')[1].rstrip(';\n').split(';')        
        
    def getProfile(self):
        cmd = 'getprofile\n'
        self.connection.send(cmd)
        profile = self.__readResult()
        profile = profile.split(':')[1]
        return profile
        
    def getStatus(self):
        cmd = 'getstatus\n'
        self.connection.send(cmd)
        status = self.__readResult()
        status = status.split(':')[1]
        return status

    def getCountLeds(self):
        cmd = 'getcountleds\n'
        self.connection.send(cmd)
        count = self.__readResult()
        count = count.split(':')[1]
        return count
        
    def getAPIStatus(self):
        cmd = 'getstatusapi\n'
        self.connection.send(cmd)
        status = self.__readResult()
        status = status.split(':')[1]
        return status
        
    def connect (self):
        try:    
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((self.host, self.port))            
            self.__readResult()
            if self.apikey is not None:    
                cmd = 'apikey:' + self.apikey + '\n'            
                self.connection.send(cmd)
                self.__readResult()
            return 0
        except:
            print ('Lightpack API server is missing')
            return -1
        
    def setColor(self, n, r, g, b):         
        cmd = 'setcolor:{0}-{1},{2},{3}\n'.format(n-1, r, g, b)
        self.connection.send(cmd)
        self.__readResult()
        
    def setColorToAll(self, r, g, b):    
        cmdstr = ''
        for i in self.ledMap:
            cmdstr = str(cmdstr) + str(i) + '-{0},{1},{2};'.format(r,g,b)        
        cmd = 'setcolor:' + cmdstr + '\n'            
        self.connection.send(cmd)
        self.__readResult()

    def setGamma(self, g):
        cmd = 'setgamma:{0}\n'.format(g)
        self.connection.send(cmd)
        self.__readResult()        
        
    def setSmooth(self, s):
        cmd = 'setsmooth:{0}\n'.format(s)
        self.connection.send(cmd)
        self.__readResult()

    def setBrightness(self, s):
        cmd = 'setbrightness:{0}\n'.format(s)
        self.connection.send(cmd)
        self.__readResult()

    def setProfile(self, p):
       
        cmd = 'setprofile:%s\n' % p
        self.connection.send(cmd)        
        self.__readResult()
        
    def lock(self):
        cmd = 'lock\n'
        self.connection.send(cmd)
        self.__readResult()
        
    def unlock(self):
        cmd = 'unlock\n'
        self.connection.send(cmd)    
        self.__readResult()
    
    def turnOn(self):
        cmd = 'setstatus:on\n'        
        self.connection.send(cmd)
        self.__readResult()
    
    def turnOff(self):
        cmd = 'setstatus:off\n'
        self.connection.send(cmd)
        self.__readResult()        

    def disconnect(self):
        self.unlock()
        self.connection.close()
        

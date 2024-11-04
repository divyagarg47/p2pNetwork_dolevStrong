from datetime import datetime
import time
    
class Message:
    def __init__(self,messagebody,isBroadcast = False,numSign = 0):
        self.messagebody = messagebody
        self.messageid = int(1000*time.time())
        self.isBroadcast = isBroadcast
        self.numSign = numSign
    
    def getMessageBody(self):
        return self.messagebody
    def __str__(self):
        return f"{self.messagebody}:{self.isBroadcast}:{self.messageid}:{self.numSign}"

    # @classmethod
    # def from_string(cls, string):
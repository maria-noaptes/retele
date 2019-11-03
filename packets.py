class CONNECT:
    def __init__(self,id,username,parola):
        self.id=id
        self.username=username
        self.parola=parola
class CONNACK:
    def __init__(self,flag_confirmare):
        self.flag_confirmare=flag_confirmare
class SUBSCRIBE:
    def __init__(self,packetID,subscriptii):
        self.subscriptii=subscriptii
        self.packetID=packetID
class PINGREQ:
    pass
class SUBPACK:
    def __init__(self,packetID,returnCode):
        self.packetID=packetID
        self.returnCode=returnCode
class PUBLISH:
    def __init__(self,topic,payload):
        self.topic=topic
        self.payload=payload
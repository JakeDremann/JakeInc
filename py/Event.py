class Event:

    def __init__(self):

        self.title = None
        self.start = None
        self.end = None 
        self.location = None
    
    def setTitle (self, Title):
        self.title = Title
    
    def setStart (self, Start):
        self.start = Start
    
    def setEnd (self, End):
        self.end = End
    
    def setLocation (self, Location):
        self.location = Location
    
    def getTitle (self):
        return (self.title)
    
    def getStart (self):
        return (self.start)
    
    def getEnd (self):
        return (self.end)
    
    def getLocation (self):
        return (self.location)

    


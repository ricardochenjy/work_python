class organism(object):
    def __init__(self):
        self.live=True
    def peel(self):
        print 'Peel me'
        
class animal(organism):  
    def __init__(self):
        super(animal,self).__init__()
        self.movable=True
    def photosynthesis(self):
        print "can't"
            
class vertebrate(animal):  
    def __init__(self):
        super(vertebrate,self).__init__()
        self.spine=True
        
class mammal(vertebrate):  
    def __init__(self):
        super(mammal,self).__init__()
        self.viv=True

class dogs(mammal):
    def __init__(self):
        super(dogs,self).__init__()
        self.hair=True
        self.name='big white'
   

class parent(object):
    def altered(self):
        print 'parent altered()'
        
class child(parent):
    def altered(self): 
        super(child,self).altered()
        print 'child altered()'

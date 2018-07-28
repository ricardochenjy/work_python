class parent(object):
    def override(self):
        print 'parent override()'
        
class child(parent):
    def override(self):
        print 'child override()'

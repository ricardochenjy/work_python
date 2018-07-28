from math import pi
def C(r):
    return pi*r*2

def difference(a,b):
    return a-b

x1=input('number x1 is :')
x2=input('number x2 is :')
print 'the difference is :',difference(x1,x2)
print '*******************'
r=input('please input the radiu :\n\t\t')
print 'The circumference is :\n\t\t%f'%C(r)



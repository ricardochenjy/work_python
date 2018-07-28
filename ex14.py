'''
cats=20
dogs=10
if cats<dogs:
    print 'More dogs than cats.'
elif  dogs<cats:
    print 'More cats than dogs.'
else:
    print 'Same number of cats and dogs'
'''
print '*******************'

from math import pi
from sys import argv
script,r_Earth,r_Mars=argv

def C(r):
    return pi*r*2

r=input('please input the radiu :\n\t\t')
print 'The circumference is :\n\t\t%f'%C(r)

r_Earth=float(r_Earth)
r_Mars=float(r_Mars)

C_Earth=C(r_Earth)
C_Mars=C(r_Mars)

c_e=abs(C_Earth-C(r))
c_m=abs(C_Mars-C(r))

if c_m<c_e:
    print 'It is Mars more possibly .'
elif  c_e<c_m:
    print 'It is Earth more possibly.'
else:
    print 'It just in the midumn of the two.'


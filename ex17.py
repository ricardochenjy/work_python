from sys import argv
import Cr as cir
script,r_Earth,r_Mars=argv

r=input('please input the radiu :\n\t\t')
print 'The circumference is :\n\t\t%f'%cir.C(r)

r_Earth=float(r_Earth)
r_Mars=float(r_Mars)

C_Earth=cir.C(r_Earth)
C_Mars=cir.C(r_Mars)

c_e=abs(C_Earth-cir.C(r))
c_m=abs(C_Mars-cir.C(r))

if c_m<c_e:
    print 'It is Mars more possibly .'
elif  c_e<c_m:
    print 'It is Earth more possibly.'
else:
    print 'It just in the midumn of the two.'


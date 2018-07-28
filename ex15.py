a=(1,2,3)
b=[1,2,3]
c={1,2,3}
print '**********tuple'
for i in a:
    print i
    print 1+3,'\n'
print '**********list'
for i in b:
    print i
    print 1+3,'\n'
print '**********set'
for i in c:
    print i
    print 1+3,'\n'
print '**************'
for i in range(3):
    print a[i]
print '**************'
for i in range(10,21,1):
    a=i/10.00
    print a,'^',a,'=',pow(a,a),'\n'

a2=[] 
for i in range(5):
    a2.append(i)
print a2


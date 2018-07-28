import numpy 
a=0
n=input('the times you want to print:')

while a<n:
    print 'hello world'
    a=a+1
    if (a>520):
        print 'You have printed 521 times.stop.'
        break


a=0
N=0.0
m=input('the times you want to try to find:')
while a<m:
     num=numpy.random.randn(1)
     if num>1:
        N=N+1
     a=a+1
     if (a>1e5):
         print 'You have tried too many times.stop.'
         ans=N/float(a)
         break
ans=N/float(m)
print 'the possibility of "a>1" is:',ans

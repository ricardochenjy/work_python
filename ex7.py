from sys import argv
script,pi,r=argv
print 'The script is called:\n\t\t',script
print 'The circumference ratio is:\n\t\t',pi
print 'The semidiameter is:\n\t\t',r
#scipy matplotlib  panda
pi=float(pi)  #circumference ratio
r=float(r)  #semidiameter
C=pi*r*2 #circumference
print 'the circumference is = \n\t\t%f.\n'%C #print the result
PI=raw_input('pealse input the pi:\n\t\t')
PI=float(PI)
R=raw_input('pealse input the semidiameter:\n\t\t')
R=float(R)
C2=PI*R*2
print 'the circumference is = \n\t\t%f.'%C2 #print the result

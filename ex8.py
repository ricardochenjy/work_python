from sys import argv
script,filename=argv
text=open(filename,'w')
line1='My name is Chenjingyan'
line2='I am 19.'
line3='I like writing code.'
text.write(line1)
text.write('\n')
text.write(line2)
text.write('\n')
text.write(line3)
text.write('\n')
text.close()



#filename=raw_input('pealse input the filename:\n\t')
#file2=open(filename)
#print 'The content of %s:' %filename
#print file.read()



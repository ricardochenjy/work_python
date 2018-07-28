# -*- coding: UTF-8 -*-
#!/usr/bin/python
from sys import argv
script,filename=argv
text=open(filename,'w+')
line1='My name is 陈景妍'
line2='I am 19.'
line3='I like writing code.'
text.write(line1)
text.write('\n')
text.write(line2)
text.write('\n')
text.write(line3)
text.write('\n')
text.seek(0,0)
print '******************'
print text.read()
text.close()

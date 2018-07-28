import class18 as cl
import class18_2 as cl2
import class18_3 as cl3
import class18_4 as cl4

dad=cl.parent()
son=cl.child()
dad.implicit()
son.implicit()

dad2=cl2.parent()
son2=cl2.child()
dad2.override()
son2.override()

dad3=cl3.parent()
son3=cl3.child()
dad3.altered()
son3.altered()

dad4=cl4.parent()
son4=cl4.child()
dad4.fun()
son4.fun()


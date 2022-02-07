'''
  creating classes incrementally in the REPL
'''

class T:
    pass

t1 = T()
t2 = T()

t1.a = 10
t2.a = "hello"
t1.b = [1,2,3]
t2.c = {'a':5, 'b':6}
print(t1.a*10, t2.a, 't1.b is ', t1.b, 't2.c is', t2.c)

T.b = "class attribute"
T.d = 999

print('T.b=',T.b,'T.d=',T.d)
print('t1.b=',t1.b,'t2.b=',t2.b)
print('t1.d=',t1.d,'t2.d=',t2.d)


class Demo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = []

    def interpolate(self,t):
        return a*t + b*(1-t)

    def remember(self,x):
        self.c += [x]

    def recall(self):
        x = self.c[-1] # get the last element
        self.c = self.c[:-1]  # remove the last element
        return x

d1 = Demo(3,5)
d2 = Demo(3,6)
print(d1.interpolate(0.5))
d2.remember(7)
d2.remember('hello')
print(d2.recall())

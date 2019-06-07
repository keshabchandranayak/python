# -*- coding: utf-8 -*-
#import one
class data:
    """print Name"""
    a=0
    b=0
    def __init__(self, x=10,y=12):
        print("in init")
        self.a=x
        self.b=y
    x="keshab"
    def fun(self,str):
        print("HiHI")
        print(self.a, self.b)
        print(str)
       
data.fun("yyy","ccc")
obj=data()
obj.fun("bbb")
print(data.__doc__)
#print(locals)
#help(one)
#print(obj.__doc__)
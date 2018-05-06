#Problem 1: Complete the complex class denition (available in overload.py from the lecture 7
#repository) to support -,*, and / ( sub , mul , and div ). Recall that a/b = a*conj(b)/(b*conj(b)).
#Show from a few sample cases that your functions work. (10)

import numpy
class Complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i

    def copy(self):
        return Complex(self.r,self.i)

    #add function
    def __add__(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r=ans.r+val.r
            ans.i=ans.i+val.i
        else:
            ans.r=ans.r+val
        return ans

    #minus function
    def __sub__(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r=ans.r-val.r
            ans.i=ans.i-val.i
        else:
            ans.r=ans.r-val
        return ans

    #multiply function
    def __mul__(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r=ans.r*val.r
            ans.i=ans.i-val.i
        else:
            ans.r=ans.r*val
        return ans
    
    #divide function
    def __truediv__(self,val): #__truediv__ for floating points, and __floordiv__ for integers
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r=ans.r/val.r
            ans.i+ans.i/val.i
        else:
            ans.r=ans.r/val
        return ans

    def __repr__(self):
        if (self.i<0):
            return repr(self.r)+' - '+repr(-1*self.i) +'i'
        else:
            return repr(self.r)+' + '+repr(self.i) +'i'


if __name__=='__main__':

    a=Complex(2,5)
    b=Complex(4,-3)
    #addition of a and b
    c=a+b
    print (str(a)+" + "+str(b)+ " = " +str(c))
    d=a-b
    print (str(a)+" - "+str(b)+ " = " +str(d))
    e=a*b
    print (str(a)+" x "+str(b)+ " = " +str(e))
    f=a/b
    print (str(a)+" / "+str(b)+ " = " +str(f))










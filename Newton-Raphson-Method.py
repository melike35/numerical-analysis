#!/usr/bin/env python
# coding: utf-8

# In[8]:




# function
def f(x):
    return (3*x*x*x+x*x-x-5)

# derivative of function
def deriv(x):
    return 9*x*x+2*x*x-1

#x0 value that comes from question 
x0=-1

#initial itr = 0
itr = 0

for i in range  (100):
    itr += 1
    xr = x0 - f(x0)/deriv(x0)
    if abs(f(xr))< 0.0001:
        break
    x0 = xr
print ("Iteration  :  %i " %itr)
print("Root :  %.5f"%x0)


# In[ ]:





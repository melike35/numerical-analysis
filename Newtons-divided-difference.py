#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def DiffTable(x, y, n): 
  
    for i in range(1, n):  
        for j in range(n - i):  
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j])); 
    return y; 
  
def proTerm(i, value, x):  
    pro = 1;  
    for j in range(i):  
        pro = pro * (value - x[j]);  
    return pro; 

def Formula(value, x, y, n):  
  
    sum = y[0][0];  
  
    for i in range(1, n): 
        sum = sum + (proTerm(i, value, x) * y[0][i]);  
      
    return sum;  
  

def showTable(y, n):  
  
    for i in range(n):  
        for j in range(n - i):  
            print(round(y[i][j], 4), "\t",  
                               end = " ");   
        print("");  
  

  
# number of inputs given  
print("______Newton’s Divided Difference Interpolation_____")
print(" ")
print(" ")
n = int(input(print("Enter the number of points you'll calculate  :")));  
x = [] 


print("Enter X values :")
for i in range(0, n): 
    ele = int(input()) 
  
    x.append(ele) 
      
print(x) 

y = [[0 for i in range(10)]  
        for j in range(10)];  
  
print("Enter Y values :")
y[0][0] = int(input()) ;  
y[1][0] = int(input()) ;  
y[2][0] = int(input()) ;  
y[3][0] = int(input()) ;  


y=DiffTable(x, y, n);  
  

showTable(y, n);  

  
print("Value  is", 
        round(Formula(3, x, y, n), 2)) 


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Estimate PI Monte Carlo Simulation
# Center of the circle=(0.0)
# Radius of the circle=1

import numpy as np
import math as m

n=int(input('Enter number of samples:'))
x=np.random.uniform(0,1,n)
y=np.random.uniform(0,1,n)
A=0

for i in range(n):
  if(x[i]**2+y[i]**2<=1):
    A=A+1
p=4*A/n

print("pi= ",p)


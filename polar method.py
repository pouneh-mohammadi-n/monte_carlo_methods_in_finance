#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math as m

def two_IID():
  s=2
  while (s>=1):
    u1=np.random.uniform(0,1)
    u2=np.random.uniform(0,1)
    v1=2*(u1)-1
    v2=2*(u2)-1
    s=v1**2+v2**2
  main=m.sqrt(-2*m.log(s)/s)
  X=v1*main
  Y=v2*main
  return X,Y

for i in range(0,100):
  print (two_IID())


# In[ ]:





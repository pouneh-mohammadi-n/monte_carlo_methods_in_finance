#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def integral(n,a1,a2,b1,b2):
  x=np.random.uniform(a1,a2,n)
  y=np.random.uniform(b1,b2,n)
  I=(a2-a1)*(b2-b1)
  s=I*np.sum(((x**2)+(y**2)))/n
  print(s)


# In[2]:


import numpy as np
def integral1(n,a1,a2,b1,b2,c1,c2):
  x=np.random.uniform(a1,a2,n)
  y=np.random.uniform(b1,b2,n)
  z=np.random.uniform(c1,c2,n)
  I=(a2-a1)*(b2-b1)*(c2-c1)
  s=I*np.sum(((x**2)+(y**2)+(z**2)))/n
  print(s)
  


# In[ ]:





import numpy as np
import scipy.stats as st
import seaborn as sns
import matplotlib.pyplot as plt

def f(x):
  return st.norm.pdf(x, loc=20 ,scale=10) + st.norm.pdf(x, loc=60, scale=20)
def g(x):
  return st.norm.pdf(x, loc=40, scale=30)
x = np.arange(-50,151)
a = max(f(x)/g(x))

def AR(iteration=10000):
  samples=[]
  for i in range(iteration):
    z = np.random.normal(40, 30)
    u = np.random.uniform(0, a*g(z))
    if u<=f(z):
      samples.append(z)
  return np.array(samples)

plt.plot(x, f(x))
plt.plot(x, a*g(x))
plt.title('Acceptance_Rejection Algorithm')
plt.show()

np.linspace(0,1,11)

np.arange(0,1,0.1)


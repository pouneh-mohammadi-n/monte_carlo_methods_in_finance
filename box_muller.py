import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns

# generate random uniform variables
u1 = np.random.uniform(size=10000)
u2 = np.random.uniform(size=10000)

lg=-2*np.log(u1)
X = np.sqrt(lg)*np.cos(2*np.pi*u2)
Y = np.sqrt(lg)*np.sin(2*np.pi*u2)

#theoretical normal distribution
x = np.linspace(-4,4,1000)
y = scipy.stats.norm.pdf(x,0,1)

#plot empirical distribution vs. theoretical 
fig,axes = plt.subplots(2,1)
axes[0].plot(x,y, label = 'emprical')
sns.kdeplot(X, ax = axes[0], label = 'theoretical')
axes[1].plot(x,y, label = 'emprical')
sns.kdeplot(Y, ax = axes[1], label = 'theoretical')
plt.show()

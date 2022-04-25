import numpy as np

x = np.array(list(range(100)))

y = 10.25*x + 14

noise = np.random.randint(-50,50,size=x.shape)

y += noise
y = np.floor(y)

y = [ int(e) for e in y.tolist()] 
print(y)
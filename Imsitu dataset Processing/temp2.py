import numpy as np

X = np.load('./X.npy')
X = X/255.


np.save('./X.npy',X)
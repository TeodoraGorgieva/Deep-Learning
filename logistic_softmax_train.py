import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from process import get_data

def y2indicator(y,K):
    N=len(y)
    ind = np.zeros((N,K))
    for i in xrange(N):
        ind[i, y[i]]=1
    return ind

X,Y=get_data()
X,Y=shuffle(X,Y)
Y=Y.astype(np.int32)
D=x.shape[1]
K=len(set(Y))
import numpy as np

a= np.random.randn(5)
expa = np.exp(a)
answer = expa/expa.sum()
A = np.random.randn(100, 5)
expA = np.exp(A)
answerA = expA/expA.sum(axis=1, keepdims=True)
print(answerA.sum(axis=1))
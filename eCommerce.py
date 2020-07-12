import pandas as pd
import numpy as np
url='https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/ann_logistic_extra/ecommerce_data.csv'
df = pd.read_csv(url, index_col=0)
#print(df.head(5))
data = df.as_matrix()

X= data[:, :-1]
Y= data[:, -1]

X[:,1] = (X[:,1]-X[:,1].mean())/X[:,1].std()
X[:,2] = (X[:,2]-X[:,2].mean())/X[:,2].std()

N, D = X.shape
X2 = np.zeros((N, D + 3))
X2[:, 0:(D - 1)] = X[:, 0:(D - 1)]

for n in range(N):
    t = int(X[n, D - 1])
    X2[n, t + D - 1] = 1
    
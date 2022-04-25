import numpy as np


def solve(x,y):
    
    X = np.array(x).reshape(1,-1)
    y = np.array(y).reshape(-1,1)
    X = np.insert(X,0,np.ones(X.shape),axis=0)
    X = X.T
    c_m = ( np.dot( np.linalg.inv(np.dot(X.T,X)), np.dot(X.T, y) )).tolist()
    print(f"m = {c_m[1][0]}")
    print(f"c = {c_m[0][0]}")
import numpy as np
inputm=np.array([[3 ,2, 1]])
B=np.zeros((np.shape(inputm)))
print (inputm)
for i in range(inputm.shape[1]):
    A=inputm[:,i].T
    Aexp=np.exp(A)
    Asum=np.sum(Aexp)
    B[:,i]=Asum/Aexp

print(B)


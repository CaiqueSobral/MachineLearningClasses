import numpy as np

V1 = np.array([1, 2, 3])

A = np.array([[10, 12], [6, 9], [3, 20]])
B = np.array([[-5, 3], [17, 4], [2, -1]])
B_TRANS = np.transpose(B)
I3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

E = A @ B_TRANS
print(A * B)

import numpy as np

c = np.arange(1, 13)

# r = c.reshape(2, 2, 3)
r = c.reshape(4,3)
print(c)
print(r)
f = r.flatten()
print(f)

# 전치행렬
t = r.T
print(t)

# 단위행렬
e1 = np.eye(4)
print(e1)
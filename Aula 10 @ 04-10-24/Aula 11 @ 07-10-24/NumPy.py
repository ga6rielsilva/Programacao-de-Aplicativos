import numpy as np

a = np.array([1, 2, 3])

print(a.ndim)
print(a.size)
print(a)

print("\n===============================\n")

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.ndim)
print(b.size)
print(b)

print("\n===============================\n")

c = np.arange(10)
print(c)
c = np.arange(10).reshape(2, 5)
print(c)

print("\n===============================\n")

d = np.zeros((3))
print(d)
d = np.zeros((3, 4), dtype=int)
print(d)
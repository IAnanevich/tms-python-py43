import numpy as np

# massive = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
# print(massive)
# print(type(massive))

# print(massive[3])
# print(massive[:2])
# massive[0] = 0
# print(massive)

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a)

# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=float)
# print(matrix)
# print(matrix[1])
# print(matrix[1][1]) = print(matrix[1, 1])
# print(matrix[1, 1])
# print(matrix[1, :])
# print(matrix[:, 2])
# print(matrix[-1:, -2:])

# print(matrix)
# print(matrix.shape)
# print(matrix.dtype)
# print(len(matrix[0]))

# print(2 in matrix)
# print(0 in matrix)

# massive1 = np.array(range(10), float)
# # print(massive1)
# massive = massive1.reshape((5, 2))
# print(massive)
# # print(massive.shape)
# print(massive1)

# a = np.array([1, 2, 3], float)
# b = a
# c = a.copy()
#
# a[0] = 0
# print(a)
# print(b)
# print(c)

# a = np.array([1, 2, 3], float)
# print(a)
# print(a.tolist())
# print(list(a))

# a = np.array([1, 2, 3], float)
# print(a)
# a.fill(100)
# print(a)

# matrix = np.array(range(6), float).reshape((2, 3))
# print(matrix)
# print(matrix.transpose())
# print(matrix.flatten())

# a = np.array([1, 2], float)
# b = np.array([7, 8, 9, 10], float)
# c = np.array([0, 5], float)
# print(np.concatenate((a, b, c)))

# print(np.ones((10, 10)))
# print(np.zeros((10, 10)))
# print(np.zeros(5))

# a = np.array([1, 2, 3], float)
# print(np.zeros_like(a))
# print(np.ones_like(a))

# a = np.identity(3, float)
# print(a)

# a = np.eye(5, k=2, dtype=float)
# print(a)

# math operations

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a + b)
# print(b - a)
# print(a * b)
# print(b / a)
# print(a ** b)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a + b)

# a = np.array([[1, 2, 3], [1, 2, 3]])
# b = np.array([[4, 5, 6], [4, 5, 6]])
# print(b)
# print(b.diagonal())
# print(a + b)
# print(a * b)

# a = np.array([2.1, 2.5, 2.9], float)
# b = np.array([1.1, 1.5, 1.9], float)
# print(np.floor(a))
# print(np.ceil(a))
# print(np.rint(a))
# print(np.rint(b))
# print(np.pi)
# print(np.e)

# a = np.array(range(10, 14), int).reshape((2, 2))
# for (x, y) in a:
#     print(x * y)
# print(a)

# a = np.array([5, 1, 9])
# print(a.sum())
# print(a.prod())
# print(a.min())
# print(a.max())
# print(a.argmin())
# print(a.argmax())
# print(np.sort(a))

# a = np.array([1, 1, 1, 2, 2, 3, 5, 6, 1, 6, 7, 1, 2, 4, 1])
# print(np.unique(a))

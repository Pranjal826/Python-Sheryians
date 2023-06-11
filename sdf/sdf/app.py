# primitive/non-reference/immutable - data can be copied
# int float bool String None
# reference/ non-primitive/ mutable - data can not be copied
# List Tuple -> sequential(indexing)
# Sets Dict -> non-sequential(keys)

# a = 12
# b = a
# a = 15
# print(f"a -> {a}")  # 15
# print(f"b -> {b}")  # 12


# creating list
# l = []
# l = list()
# print(type(l))
# l = [1, "john", True, 12.32,[23,34,54,]]
# print(l)


# Reading list -> indexing/slicing
# l = [21, 34, 56, 78, 90, 98, 67, 56, 54, 32]
# print(l)
# print(l[2])
# print(l[-2])
# print(l[3:6:1])
# print(l[-3:-6:-1])

# updating list
# l = [21, 34, 56, 78, 90, 98, 67, 56, 54, 32]
# print(l)
# l[2] = 69
# print(l)

# deleting list
# l = [21, 34, 56, 78, 90, 98, 67, 56, 54, 32]
# print(l)
# del l
# del l[3]
# del l[0:3:2]
# print(l)

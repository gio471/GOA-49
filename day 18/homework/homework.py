list1 = [2, 51, 11, 13, 51, 100]
# 1. Output every item from list with positive indexing.
# 2. Output every item from list with negative indexing.
# 3. Replace the last element of a list with a new value.
# 4. Replace the fifth element of a list with a new value.

print(list1[0:5])
print(list1[-5:-1])
list1[-1] = 10
print(list1)
list1[5] = 11
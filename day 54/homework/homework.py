numbers = [2, 4, 6, 8, 10]

double_numbers = list(map(lambda x: x * 2,numbers))
print(double_numbers)



names = ["Alice", "Bob", "Charlie"]
result1 = list(map(lambda y : "Hello, " +  y,names ))
print(result1)


fruits = ["apple", "banana", "kiwi"]
lengths = list(map(len,fruits))
print(lengths)




positive = [-5, 3, -2, 7, 0, 10]
result2 = list(filter(lambda x:x >= 0,positive))
print(result2)


words = ["pear", "apple", "peach", "grape"]
words_starting_with_p = list(filter(lambda word:word.startswith("p"),words ))
print(words_starting_with_p)



numbers2 = [10, 55, 42, 78, 65, 20]
result3 = list(filter(lambda x:x > 50,numbers2))
print(result3)
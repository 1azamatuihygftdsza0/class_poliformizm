sonlar = list(range(10))
print(sonlar)
# mevalar  = ["olma", "olcha", "gilos", "kiwi", "mango"]
# a_harfli = []
# for x in mevalar:
#   if "a" in x:
#     a_harfli.append(x)
# print(a_harfli)
# mevalar  = ["olma", "olcha", "gilos", "kiwi", "mango"]
# a_harfli = [x for x in mevalar if "a" in x]
# print(a_harfli)
# a = [1, 2, 3, 4, 5]
# b = []
# for i in a:
#     b.append(i * 2)
# print(b)
# a = [1,2,3,4,5]
# b = list(x*2 for x in a)
# print(b)
# x = list(a for a in range(10) if a>5)
# print(x)
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
#
# print(zip(a, b))
# nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flat = [item for sublist in nested for item in sublist]
# print(flat)
# # [1, 2, 3, 4, 5, 6, 7, 8]
# a = (1,2,3)
# b = ("a","b","c")
# c = ("A","B","C")
# x = zip(b, c)
# print(list(x))
# a = [1, 2, 3, 4]
# b = []
# x = zip(a, b)
# print(list(x))
x = [('a', 'A'), ('b', 'B'), ('c', 'C')]
b, c = zip(*x)
print(b)
print(c)
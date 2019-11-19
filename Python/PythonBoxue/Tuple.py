# Python 中的只读集合 Tuple
empty = ()
numbers = (1, 2, 3)
mix = (1, 2, "Three")
empty1 = tuple()
numbers1 = tuple('123')
mix1 = tuple([1, 2, "three"])
print(numbers1)
print(mix1)
numbers2 = tuple([7, 8, 9])
print(numbers2)
print(numbers2 + numbers2)
print(numbers2 * 2)

print(numbers2[0])
print(numbers2[0:2])
print(numbers2[0:3:2])

print(len(numbers2))
print(min(numbers2))
print(max(numbers2))

print(3 in numbers2)

del(numbers)
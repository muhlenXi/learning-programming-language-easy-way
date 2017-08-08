# 用数学思维理解 Comprehension

numbers = [i for i in range(1,6)]
print(numbers)

numbers1 = [i for i in range(1,6) if i % 2 ==0]
print(numbers1)

strings = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [int(num) for items in strings for num in items]
print(flatten)

xSamples = [2, 5, 8]
ySamples = [2, 6, 8]

points = [(x,y) for x in xSamples for y in ySamples if x != y]
print(points)

numberSet = {x for x in  range(1,6)}
print(numberSet)

numberDict = {i: str(i) for i in  range(1,6)}
print(numberDict)

switch = {(value,key) for key,value in numberDict.items()}
print(switch)
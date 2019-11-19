# 创建 lsit
list1 = []
list1 = list()
numList = [5, 4, 3, 2, 1]
numList1 = [9, 7, 5, 3, 2]
mixList = [1,2,3,"four",5]

nestedList = [numList, mixList]

# 合并 list
print(numList + mixList)

print(numList.extend(mixList))
print(numList)

numList.append(9)
print(numList)

numList.append([10, 11])
print(numList)

numList1.sort()
print(numList1)

numList2 = numList1.copy()
print(numList2[0])
print(numList2[0:3])
print(numList2[0:-1])

numList2.insert(1,11)
print(numList2)
numList2.insert(100,100)
print(numList2)

print(numList2.pop(0))
print(numList2)

print(numList2.remove(11))
print(numList2)

del(numList2[0:5:2])
print(numList2)

print(len(numList2))

print(numList2.index(9))

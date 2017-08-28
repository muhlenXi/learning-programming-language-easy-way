### List

#### 创建

```python
numberList = [] 
numberList = list()
```

#### 合并

```python
numberList2 = [numberList + numberList1]
numberList2 = numberList1.extend(numberList)
numberList.append(9)
```

#### 排序

```python
numberList.sort()
```

#### 访问

```python
numberList[0] # 单索引
numberList[0:3] # range 索引
```

#### 插入元素

```python
numberList.insert(0, "Mars")
```

#### 删除元素

```python
numberList.pop(0) # 删除并返回指定元素
numberList.remove(0)
del(numberList[0:5]) # 参数是list的切片
```

#### 获取元素个数

```python
len(numberList)
```

#### 查询是否存在某个元素

```python
numberList.index(2)
```

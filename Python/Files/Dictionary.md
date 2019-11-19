### dictionary

#### 创建

```python
{}
user = dict({"name": "Mars"})
```

#### 访问

```python
user['name']
```

#### 获取 keys 或 values

```python
user.keys()
user.values()
```

#### 是否包含 key 或 value

```python
"name" in user # 是否包含 key name
"Mars" in user # 是否包含 value Mars
``` 

#### 添加或更新

*当 key 不存在时，即为添加新元素*

```python
user.update({"age": 18})
```

#### 删除元素或字典

```python
del(user['name']) # 删除元素
del(user)	# 删除字典
```

#### 清空内容

```python
clear()
```

#### 
### dict

```python
# 创建
{}
user = dict({"name": "Mars"})

# 访问
user['name']

# 获取 keys 或 values
user.keys()
user.values()

# 是否包含 key 或 value
"name" in user # 是否包含 key name
"Mars" in user # 是否包含 value Mars

# 添加或更新
user.update({"age": 18})

# 删除元素或字典
del(user['name']) # 删除元素
del(user)	# 删除字典

# 清空内容
clear()
```
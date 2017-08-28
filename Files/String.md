### String 

#### 创建

```python
welcome = "Hello, World!" # 方式1
welcome = 'Hello, World!' # 方式2
welcome = '''Hello, Python!
Hello, World!
Hello, Everybody!
'''
```

#### 连接

```python
string2 = string + string1
```

#### 大小写转换

```python
welcome.upper()
welcome.lower()
```

#### 去掉首尾空格

```python
welcome.strip()
```

#### 获取帮助

```python
dir(welcome) # 获取支持的所有方法
help(welcome.count) # 获取方法的具体帮助
```

#### 字符串分割

```python
welcome[0]
hello = welcome[0:5]
```

####  String Template

```python
print("%s World!" % "Hello")
print("%s %s" % ("Hello", "World!"))
print("{0} {1}".format("Hello", "World!"))

welcome = {"action":"Hello", "name":"World"}
print("{action} {name}!".format(**welcome))
```
### String 


UTF-8 编码把一个 Unicode 字符根据值的大小编码成 1 ~ 6 个字节。 
 
在计算机内存中，统一使用 Unicode 编码，当需要保存到硬盘或者需要传输的时候，就转换成 UTF-8 编码。 
 
string 和 bytes 互相转换时，需要指定编码，最常用的编码是 UTF-8。 

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

#### 对于单个字符，字符编码相互转换 
 
```python 
ord("我") # 获取字符的整数表示 
chr(25105)  # 把编码转换为对应的字符 
``` 
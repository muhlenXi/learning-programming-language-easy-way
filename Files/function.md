### 自定义函数

1、无参无返回值

```python
def a_stub_function():
	pass
```

2、参数个数固定，带有默认值

```python
def and(m=1, n=2):
	return a + b
```

3、可变参数列表

```python
def add(*args):
	tmp = 0
	for i in args:
		tmp += i
	
	return tmp

add(1, 2, 3, 4) # 调用
```

4、可变参数带默认值

```python
def add(**args):
	tmp = 0
	for i in args:
		tmp += args[i]
	
	return tmp
	
	
add(n1=1, n2=2, n3=3) # 调用
```

5、混合使用

```python
def add(*args, **k_args):
	tmp = 0
	for i in args:
		tmp += i
		
	for i in k_args:
		tmp += k_args[i]
	
	return tmp
	
	
add(4, 5, n1=1, n2=2, n3=3)
```


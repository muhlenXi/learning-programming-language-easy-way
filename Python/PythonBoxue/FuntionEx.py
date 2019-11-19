def a_stub_fuction():
    pass

# 参数个数固定，带有默认值
def add(m=1,n=2):
    return m + n

# 可变参数列表
def add1(*args):
    tmp = 0
    for i in args:
        tmp += i
    return tmp

def add2(**args):
    tmp = 0
    for i in args:
        tmp += args[i]
    return tmp


print(add(3, 5))
print(add())
print(add1(1, 2, 3))
print(add2(n1=1, n2=2, n3=3))
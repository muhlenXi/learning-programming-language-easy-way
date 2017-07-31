# 在计算机内存中，统一使用 Unicode 编码，当需要保存到硬盘和需要传输的时候，就转换为UTF-8编码。

print('包含中文的str')

# ord() 获取字符的整数表示

print(ord('A'))

print(ord('中'))

# chr() 把编码转换为对应的字符

print(chr(66))

print(chr(25991))

print('\u4e2d\u6587')

x = b'ABC'

'ABC'.encode('ascii')
'中文'.encode('utf-8')

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# len() 计算包含多少个字符

print(len('ABC'))
print(len('中文'))

print(len(b'ABC'))
print(len('中文'.encode('utf-8')))

# 格式化
# %d 整数 %f 浮点数 %s 字符串 %x 十六进制整数

greet = 'Hello, %s' % 'word'
print(greet)

string = 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print(string)

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Age: %s. Gender: %s' % (25, True))

# 用 %% 来表示 % 字符

print('growth rate: %d %%' % 7)


# exercise

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('%.1f %%' % r)

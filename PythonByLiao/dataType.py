print('I\'m OK')
print('I\'m learning\nPython.')
# r'' 表示 '' 内部的字符串默认不转义
print(r'\\\t\\')

print('''line1
line2
line3''')

# not 为非运算
print(not True)
age = 19
if age >= 18:
    print('adult')
else:
    print('teenager')

PI = 3.141592654
print(PI)

print(10 / 3)
print(10 // 3)

print(10 % 3)

print('---- exercise ----')
n = 123
print(n)

f = 456.789
print(f)

s1 = 'Hello,World'
print(s1)

s2 = 'Hello,\'Adam\''
print(s2)

s3 = r'Hello,"Bart"'
print(s3)

s4 = r'''Hello,
Lisa!'''
print(s4)
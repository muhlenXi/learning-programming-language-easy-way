# 理解分支语句和 boolean 表达式

num = 30
if num < 10:
    content = '{0} is less than 10'.format(num)
    print(content)
elif 10 < num < 20:
    print("between 10 and 20")
elif num > 10 and num < 20:
    print('between 10 and 20')
elif num == 10 or num == 20:
    print('equal to 10 or 20')
elif not num == 10:
    print('not equal to 10')
elif num != 10:
    print('not equal to 10')
elif num not in [10,20]:
    print('not equal to 10 or 20')
else:
    print("greater than or equal to 20")


if not "":
    print("empty string")

if not ():
    print('empty tuple')

if not []:
    print('empty list')

if not None:
    print('none')

if __name__ == '__main__':
    print('execute as a single script.')

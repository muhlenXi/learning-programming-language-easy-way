# 在 Python 中使用循环

for num in range(1, 5):
    print(num)

for num in [5, 4, 3, 2, 1]:
    print(num)

user = {'email': '11@boxue.io', 'name': 'Mars'}
for info in user:
    print(info)

for num in range(1, 5):
    if num == 2:
        break
    print(num)
else:
    print('All numbers are interated')

num = 1
while num < 10:
    if num % 2 == 0:
        num += 1
        continue

    print(num)
    num += 1


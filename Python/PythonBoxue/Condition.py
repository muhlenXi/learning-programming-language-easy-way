# 理解分支语句和 boolean 表达式

number = 30
if number < 10:
    print("{0} is less than 10".format(number))
elif number == 10 or number == 20:
    print("{0} is 10 or 20.")
elif number > 10 and number < 20:
    print("{0} is between ten and twenty.".format(number))
else:
    print("{0} is more than t")



if __name__ == '__main__':
    print('execute as a single script.')

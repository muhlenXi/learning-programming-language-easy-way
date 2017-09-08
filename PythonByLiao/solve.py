import math

def quadratic(a, b, c):
    x1 = 0
    x2 = 0
    if b*b - 4*a*c >= 0:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return (x1, x2)

def sum(m=1, n=2):
    return m + n


print(sum())    # 使用了默认值 m，n
print(sum(3))   # 使用了默认值 n
print(sum(3, 3))    # 未使用默认值
print(sum(n=2))     # 使用了默认值 m  在此感谢11的指点
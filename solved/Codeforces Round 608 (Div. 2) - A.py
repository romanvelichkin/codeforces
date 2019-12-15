# codeforces round 608 div 2 - A
# solved in time
# https://codeforces.com/contest/1271/problem/A?locale=en

# a - галстуки
a = int(input())
# b - шарфы
b = int(input())
# c - жилетки
c = int(input())
# d - пиджаки
d = int(input())
# e - стоимость a + d
e = int(input())
# f - стоимость b + c + d
f = int(input())

if e > f:
    result = min(a, d) * e
    d_rest = d - min(a, d)
    result = result + min(b, c, d_rest) * f
else:
    result = min(b, c, d) * f
    d_rest = d - min(b, c, d)
    result = result + min(a, d_rest) * e

print(result)
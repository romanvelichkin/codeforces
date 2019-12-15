# codeforces round 608 div 2 - B

# https://codeforces.com/contest/1271/problem/B?locale=en

n = int(input())
s = input()

# количество хотя бы одной из букв должно быть четным
w_amount = 0
b_amount = 0
result = 0
result_turns = ''

for i in range(n):
    if s[i:i+1] == 'W':
        w_amount += 1
    else:
        b_amount += 1

if w_amount == n or b_amount == n:
    print('0')

elif w_amount % 2 != 0 and b_amount % 2 != 0:
    print('-1')

# work for BWW doesnt work for BWWWW
else:
    for i in range(n):
        print('i = ' + str(i))
        if i > 0:
            if s[i-1:i] != s[i:i+1]:
                result += 1
                result_turns = result_turns + str(i+1) + ' '
                i += 1
    print(result)
    print(result_turns[:len(result_turns)])




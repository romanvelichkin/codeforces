# codeforces round 608 div 2 - F

# https://codeforces.com/contest/1271/problem/F?locale=en

groups = int(input())
result = '-1'

for i in range(groups):
    rooms_first = input().split(' ')
    math_room_first = rooms_first[0]
    prog_room_first = rooms_first[1]
    sport_room_first = rooms_first[2]

    rooms_second = input().split(' ')
    math_room_second = rooms_first[0]
    prog_room_second = rooms_first[1]
    sport_room_second = rooms_first[2]

    student_types = input().split(' ')
    stud_all = student_types[0]
    stud_no_sport = student_types[1]
    stud_no_prog = student_types[2]
    stud_just_math = student_types[3]
    stud_no_math = student_types[4]
    stud_just_prog = student_types[5]
    stud_just_sport = student_types[6]

    stud_amount_math = stud_all + stud_no_sport + stud_no_prog + stud_just_math
    stud_amount_prog = stud_all + stud_no_sport + stud_no_math + stud_just_prog
    stud_amount_sport = stud_all + stud_no_math + stud_no_prog + stud_just_sport

    math_room_total = math_room_first + math_room_second
    prog_room_total = prog_room_first + prog_room_second
    sport_room_total = sport_room_first + sport_room_second

    if math_room_total < stud_amount_math:
        result = '-1'
        print(result)
        continue

    if prog_room_total < stud_amount_prog:
        result = '-1'
        print(result)
        continue

    if sport_room_total < stud_amount_sport:
        result = '-1'
        print(result)
        continue

    group_first_all = min(stud_all, math_room_first, prog_room_first, sport_room_first)
    # надо везде ставить min, чтобы выбирать наименьшее значение и избежать отрицательных величин
    math_room_first = math_room_first - group_first_all
    prog_room_first = prog_room_first - group_first_all
    sport_room_first= sport_room_first - group_first_all
    group_second_all = stud_all - group_first_all

    group_first_no_sport = min(stud_no_sport, math_room_first, prog_room_first)
    math_room_first = math_room_first - group_first_no_sport
    prog_room_first = prog_room_first - group_first_no_sport
    group_second_no_sport = stud_no_sport - group_first_no_sport






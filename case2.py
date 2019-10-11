"""Case2
Developers:
Kuznetsova Ksenia(0%)
Panukova Ekaterina(0%)"""


import local as lc

print(lc.HELLO)
member = int(input())
n: float = 0
m: int = 0
n1: float = 0
name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
income = 0
for month in name_month:
    print(lc.TXT_CATEGORY, month)
    income1 = float(input())
    income += income1

if member == 1:
    m = int(4750)
    if 0 <= income <= 9075:
        n = 0.1 * income
    elif income <= 36900:
        n = 0.1 * 9075 + 0.15 * (income - 9076)
    elif income <= 89350:
        n = 0.1 * 9075 + 0.15 * (36900 - 9076) + 0.25 * (income - 36901)
    elif income <= 186350:
        n = 0.1 * 9075 + 0.15 * (36900 - 9076) + 0.25 * (89350 - 36901) + 0.28 * (income - 89351)
    elif income <= 405100:
        n = 0.1 * 9075 + 0.15 * (36900 - 9076) + 0.25 * (89350 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (
                    income - 186351)
    elif income <= 406750:
        n = 0.1 * 9075 + 0.15 * (36900 - 9076) + 0.25 * (89350 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (
                    405100 - 186351) + 0.35 * (income - 405101)
    elif income >= 406751:
        n = 0.1 * 9075 + 0.15 * (36900 - 9076) + 0.25 * (89350 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (
                    405100 - 186351) + 0.35 * (406750 - 405101) + 0.396 * (income - 406751)

    else:
        print(lc.ERROR)


elif member == 2:
    M = int(7950)
    seven = income - 457600
    if seven < 0:
        seven = 0
    six = income - seven - 405100
    if six < 0:
        six = 0
    five = income - six - seven - 226850
    if five < 0:
        five = 0
    four = income - five - six - seven - 148850
    if four < 0:
        four = 0
    three = income - four - five - six - seven - 73800
    if three < 0:
        three = 0
    two = income - three - four - five - six - seven - 18150
    if two < 0:
        two = 0
    one = income - two - three - four - five - six - seven
    if one < 0:
        one = 0
    N = one * 0.1 + two * 0.15 + three * 0.25 + four * 0.28 + five * 0.33 + six * 0.35 + seven * 0.396


elif member == 3:
    M = int(5500)
    if 0 <= income <= 12950:
        N = 0.1 * income
    elif income <= 49400:
        N = 0.1 * 12950 + 0.15 * (income - 12951)
    elif income <= 127550:
        N = 0.1 * 12950 + 0.15 * (49400 - 12951) + 0.25 * (income - 49401)
    elif income <= 206600:
        N = 0.1 * 12950 + 0.15 * (49400 - 12951) + 0.25 * (127550 - 49401) + 0.28 * (206600 - 127551) + 0.33 * (
                    income - 127551)
    elif income <= 405100:
        N = 0.1 * 12950 + 0.15 * (49400 - 12951) + 0.25 * (127550 - 49401) + 0.28 * (206600 - 127551) + 0.33 * (
                    405100 - 206601) + 0.35 * (income - 405101)
    elif income >= 432201:
        N = 0.1 * 9075 + 0.15 * (36900 - 9076) + 0.25 * (89350 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (
                    405100 - 186351) + 0.35 * (432201 - 405101) + 0.396 * (income - 432201)
    else:
        print(lc.ERROR)

else:
    print(lc.ERROR)

if member == 1:
    person = lc.PERSON_1
elif member == 2:
    person = lc.PERSON_2
else:
    person = lc.PERSON_3
if m > n:
    m = n
n1 = (n - m)
print(lc.RESULT_1, round(income))
print(lc.RESULT_2, round(n))
print(lc.RESULT_3, round(m))
print(lc.RESULT_4, round(n1))

"""Case2
Developers:
Kuznetsova Ksenia(0%)
Panukova Ekaterina(0%)"""

#import local as lc
member = input('Здравствуйте, мы рады видеть Вас в банке "KatSun".' \
         '\nК какой категории Вы относитесь?(Укажите цифру)\n1-Один субъект\n2-Супружеская пара\n3-Родитель-одиночка\n')

if member == '1':
    income = int(input('Укажите Ваш ежемесячный доход: ', ))
    if income <= 9075:
        print(0.1*income)
    elif income <= 36900:
        print(0.1*9075 + 0.15*(income - 9076))
    elif income <= 89350:
        print(0.1*9075 + 0.15*(36900 - 9076) + 0.25*(income - 36901))
    elif income <= 186350:
        print(0.1*9075 + 0.15*(36900 - 9076) + 0.25*(89350 - 36901) + 0.28*(income - 89351))
    elif income <= 405100:
        print(0.1*9075 + 0.15*(36900 - 9076) + 0.25*(89350 - 36901) + 0.28*(186351 - 89351) + 0.33*(income - 186351))
    elif income <= 406750:
        print(0.1*9075 + 0.15*(36900 - 9076) + 0.25*(89350 - 36901) + 0.28*(186351 - 89351) + 0.33*(405100 - 186351) + 0.35*(income - 405101))
    elif income >= 406751:
        print(0.1*9075 + 0.15*(36900 - 9076) + 0.25*(89350 - 36901) + 0.28*(186351 - 89351) + 0.33*(405100 - 186351) + 0.35*(406750 - 405101) + 0.396*(income - 406751))
elif member == '2':
    income = int(input('Укажите Ваш ежемесячный доход: ', ))
    seven = income - 457600
    if seven < 0:
        seven = 0
    six = income - seven - 405100
    if six < 0:
        six = 0
    five = income - six - seven - 226850
    if five < 0:
        five = 0
    foure = income - five - six - seven - 148850
    if foure < 0:
        foure = 0
    three = income - foure - five - six - seven - 73800
    if three < 0:
        three = 0
    two = income - three - foure - five - six - seven - 18150
    if two < 0:
        two = 0
    one = income - two - three - foure - five - six - seven
    if one < 0:
        one = 0
    N = one * 0.1 + two * 0.15 + three * 0.25 + foure * 0.28 + five * 0.33 + six * 0.35 + seven * 0.396
else:
    income = int(input('Укажите Ваш ежемесячный доход: ', ))
    if income <= 12950:
        print(0.1*income)
    elif income <= 49400:
        print(0.1*12950 + 0.15*(income - 12951))
    elif income <= 127550:
        print(0.1*12950 + 0.15*(49400 - 12951) + 0.25*(income - 49401))
    elif income <= 206600:
        print(0.1*12950 + 0.15*(49400 - 12951) + 0.25*(127550 - 49401) + 0.28*(206600 - 127551) + 0.33*(income - 127551))
    elif income <= 405100:
        print(0.1*12950 + 0.15*(49400 - 12951) + 0.25*(127550 - 49401) + 0.28*(206600 - 127551) + 0.33*(405100 - 206601) + 0.35*(income - 405101))
    elif income >= 432201:
        print(0.1*9075 + 0.15*(36900 - 9076) + 0.25*(89350 - 36901) + 0.28*(186351 - 89351) + 0.33*(405100 - 186351) + 0.35*(432201 - 405101) + 0.396*(income - 432201))
#else:
    print('В нашем банке обслуживаются только три категории, попробуйте повторить попытку позже.')
    result = 45 * income
if member == 1:
    person = '"один субъект"'
elif member == 2:
    person = '"супружеская пара"'
else:
    person = '"родитель-одиночка"'
print('',)

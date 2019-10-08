"""Case2
Developers:
Kuznetsova Ksenia(0%)
Panukova Ekaterina(0%)"""

import local as lc
print(lc.'Здравствуйте, мы рады видеть Вас в банке "KatSun".' \
         '\nК какой категории Вы относитесь?(Укажите цифру)\n1-Один субъект\n2-Супружеская пара\n3-Родитель-одиночка')
member = int(input())
income = int(input())
while member >=1 and member<=3:
    if member == 1:
    elif member == 2:
    else :
else:
print('В нашем банке обслуживаются только три категории, попробуйте повторить попытку позже.')
result = N * income
if member == 1:
    person = '"один субъект"'
elif member == 2:
    person = '"супружеская пара"'
else:
    person = '"родитель-одиночка"'
print('',)
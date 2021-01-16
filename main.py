# Здесь я могу написать комментарий в одну строку
'''
Я документация для первой программы!
Я очень нужная и полезная!
'''
price_rub = 1000 # int
eur_cost = 90
price_eur = price_rub / eur_cost
greetings = f'I am the first program!'
type_of_variable = type(price_eur)
print(f'This is price in rub: {price_rub}')
print(f'This is price in euro: {price_eur}')
print(f'this is price in euro {int(price_rub / eur_cost)} and {round(price_rub % eur_cost , 2)} something')
# print(type_of_variable) # проверь на ошибки
# test_bool = False
# print(f'Orig {test_bool}, {int(test_bool)}')

if price_eur > 15:
    print('Price to high')
elif price_eur <= 10 and price_eur >= 0:
    print('Buy it!')
else:
    print('Next month')

while price_eur > 10:
    price_eur -= 0.5
    print(f'We update cost: {price_eur}')

# flag_x = True
item = None
while item != 'freedom':
    item = input('What do you want? :')
    # if item == 'freedom':
    #     print('You are free!')
    #     flag_x = False
    #     break


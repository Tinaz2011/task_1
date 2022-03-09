a = int(input('Какая у Вас выручка? '))
b = int(input('Какие у Вас издержки? '))
res = (a - b)
if res > 0:
    print('Ваш проект приносит прибыль' , res)
elif res < 0:
    print('Ваш проект убыточен', res)
stuff = int(input('Сколько у Вас сотрудников?' ))
rent = res / a
print('Рентабельность Вашего проекта', rent)
stuff_res = res / stuff
print('Прибыль на сотрудника составляет', stuff_res)
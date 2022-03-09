a = int(input('Какая у вас выручка? '))
b = int(input('Какие у Вас издержки? '))
res = (a - b)
if res > 0:
    print('Ваш проект приносит прибыль' , res)
elif res < 0:
    print('Ваш проект убыточен', res)
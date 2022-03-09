number = int(input('input integer'))
res = 0
number_max = 0
while number > 0:
    last = number % 10
    if last > number_max:
        number_max = last
    number = number // 10
print('The biggest number is: ', last)
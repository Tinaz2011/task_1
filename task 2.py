sec = int(input('How many sechonds'))
hour = (sec//3600)
min = ((sec-hour*3600)//60)
sec2 = (sec-hour*3600-min*60)
time_num = {hour}, {min}, {sec}
print(hour, ':', min, ':', sec2)
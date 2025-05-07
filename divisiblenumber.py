#Checking if number is divisible by another number
numerator=int(input('Enter numerator: '))
denominator=int(input('Enter denominator: '))
if numerator%denominator==0:
    print('\n',numerator,'is divisble by',denominator)
else:
    print('Numbers are not divisble')

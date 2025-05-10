#Average Speed
cyclist1=int(input('Enter value 1: '))
cyclist2=int(input('Enter value 2: '))
cyclist3=int(input('Enter value 3: '))
sum=cyclist1+cyclist2+cyclist3
averagespeedof3cyclists=(sum)/3
print('Average Speed:\n',averagespeedof3cyclists)
if cyclist1<=averagespeedof3cyclists and cyclist2<=averagespeedof3cyclists and cyclist3<=averagespeedof3cyclists:
    print('No cylists are going slower')
elif averagespeedof3cyclists>cyclist1 and averagespeedof3cyclists>cyclist2:
    print("%d and %d are lesser than average speed (%d)" %(cyclist1,cyclist2,averagespeedof3cyclists))
elif averagespeedof3cyclists>cyclist1 and averagespeedof3cyclists>cyclist3:
    print('Cyclist 1 and Cyclist 3 are less than the average speed')
elif averagespeedof3cyclists>cyclist2 and averagespeedof3cyclists>cyclist3:
    print('Cyclists 2 and 3 are less than the average speed')
elif averagespeedof3cyclists>cyclist1:
    print('Cyclist 1 is less than the average speed')
elif averagespeedof3cyclists>cyclist2:
    print('Cyclist 2 is less than the average speed')
elif averagespeedof3cyclists>cyclist3:
    print('Cyclist 3 is less than the average speed')
else:
    print('Invalid Input')

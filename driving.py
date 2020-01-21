country=input('where are you from?')
age=int(input('how old are you?'))
if country=='Taiwan':
    if age>=18:
        print('Yes,you can')
    else:
        print('No')
elif country=='America':
    if age>=16:
        print('Yes,you can')
    else:
        print('No')
else:
    print('you can only enter Taiwan or America')


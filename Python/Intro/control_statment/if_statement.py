"""IF STATEMENT"""
x = int(input('Please enter an integer: '))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
else:
    print('More')
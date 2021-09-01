x=int(input('Enter number '))
y=int(input('Enter number '))
operator = input('Enter operator ')
operator= operator.strip().lower()
if operator == 'add':
    print(f'{x} + {y} = {x+y}')
elif operator == 'minus':
    print(f'{x} - {y} == {x-y}')
elif operator == 'mul':
    print(f'{x} * {y} == {x*y}')
elif operator == 'divide':
    print(f'{x}/{y} == {x/y}')
elif operator == 'mod':
    print(f'{x}%{y} == {x%y}')
elif operator == 'power':
    print(f'{x}^{y} == {x ** y}')
else:
    print('I don\'t know what to do')

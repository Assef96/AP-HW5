def myFunc(a, b, *args, **kwargs):
    print(f'a is: {a}')
    print(f'b is: {b}')
    print()
    print('*args are:')
    for arg in args:
        print(arg)
    print()
    for key, value in kwargs.items(): 
        print (f'{key} is: {value}') 
  
myFunc(7, 5, 'foo', 'bar', 'foobar', age =28, eyeColor ='brown')
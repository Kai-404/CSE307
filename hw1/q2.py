a = input()
if " "in a:
    print('None')
else:
    try:
        s = str(type(eval(a)))
        if 'int' in s:
            print('int')
        elif 'float' in s:
            print('float')
        else:
            print('None')
    except (NameError,SyntaxError):
        print('None')
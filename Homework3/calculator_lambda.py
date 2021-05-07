
division = lambda a, b : a / b
substraction = lambda a, b : a - b
multiplication = lambda a, b : a * b
addition = lambda a, b : a + b

def quit_app():
    print('Quit')
    quit()

if __name__ == '__main__':

    actions = {
        '+' : addition,
        '-' : substraction,
        '/' : division,
        '*' : multiplication,
        'q' : quit_app
    }

    prompt = ('Enter a action to be performed (+, -, *, /) or press q to close the calculator:')
    val = input(prompt)
    

    while True:
        try:
            if val == 'q': quit_app()
            a = int(input("Please enter the first number :  "))
            b = int(input("Please enter the second number:  "))

            res = actions[val](a, b)
            print(f'{a} {val} {b}  = {res}')
           
        except (ValueError, KeyError) as e:
            print(f'invalid value or action ({e})')

        except Exception as e:
            print(f'unknown error!{e}')

        finally:
            print('--- finally block ---')
            break

    
    print ('-----------------------------')


#Calculator functions - globally
def division(a, b):

    if b == 0: return 'Inf'

    return a / b
    
def substraction(a, b):
    return a - b
    

def multiplication(a, b):
    return a * b

def addition(a, b):
    return a + b

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

    while True:
        val = input(prompt)

        if val in actions:
            
            if val == 'q': quit_app()
            a = int(input("Please enter the first number :  "))
            b = int(input("Please enter the second number:  "))

            res = actions[val](a, b)
            print(f'{a} {val} {b}  = {res}')
        
        else:
            print(f'Unknown action, please try again: {val} ')

   

    
    print ('-----------------------------')

   
   
   
   # num1 = input("Enter one number and hit enter")
   # num2 = input("Enter other number and hit enter")

   # print((num1, "/", num2, "=", division(num1, num2))

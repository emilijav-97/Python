#1. Finding factorial using function

def recur_factorial(n):
    if n == 1: return n
    return n*recur_factorial(n-1)


if __name__ == '__main__':

#2.Finding factorial using simply lambda

    fact = lambda n: 1 if n == 0 else n*fact(n-1)
    print(fact(5))

    prompt = int(input('Enter a number:'))

    while True:
        
        if prompt < 0:
            print("No factorial possible for negative numbers")  
            break
        elif prompt == 0:
            print("The factorial of 0 is 1")  
            break
        else:
            print(f'The factorial of {prompt} is {recur_factorial(prompt)}')  
            break

def numberGenerator(n):
     number = 0
     while number < n:
         yield bin(number)
         number += 1

         
if __name__ == '__main__':

    prompt = ('Enter how many numbers would you like converted: ')
    val = int(input(prompt))

    myGenerator = numberGenerator(val)

#1. Using next() to Iterate through a Generator

    g = numberGenerator(val)
    counter = 0
    while counter < val:
        print(f'Next -> {next(g)}')
        counter += 1
    
#2. Using list to store the generated values

    print(list(numberGenerator(val)))
    
   








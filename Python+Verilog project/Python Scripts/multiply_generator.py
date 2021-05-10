def numberGenerator(n):
     number = 0
     while number < n:
        yield bin(number)
        number += 1

if __name__ == '__main__':
    
    name = 'rom_{0}x{1}.dat'

    while True:

        try:
            prompt = ('Enter how many numbers would you like converted: ')
            val = int(input(prompt))

            file = name.format(f'{2**(2*val)}', f'{2*val}') #not sure how to format the memory
            fileobject = open(file, 'w')


            myGenerator = numberGenerator(val)
            g = numberGenerator(val)
            counter = 0
            while counter < val:
                print(f'Next -> {next(g)}')
                counter += 1
            l = (list(numberGenerator(val)))
            print(f"{l}")
            fileobject.write(f'{l}\n')
            
            fileobject.close()
            

            
        
        except ValueError:
            print(f'Integer only')
            continue
        else:
            break

    
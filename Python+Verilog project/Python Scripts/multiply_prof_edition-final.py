
if __name__ == '__main__':
    name = 'rom_{0}x{1}.dat'

    prompt = ('--- Multiplication --- :')
    print(prompt)

    while True:
        try:
            n = int(input("Please enter the size of one operand :  "))
            print(f'Entered size is : {n}')

            file = name.format(f'{2**(2*n)}', f'{2*n}')
            fileobject = open(file, 'w')

            
            for a in range(2**n):
                for b in range(2**n):
                    p = a * b
                    
                    aa = format(a, f'0{n}b')
                    bb = format(b, f'0{n}b')
                    res = format(p, f'0{n * 2}b')

                    print(f'{res}')
                    fileobject.write(f'{res}\n')
            
            fileobject.close()
            
        except (ValueError, KeyError) as e:
            print(f'invalid value or action ({e})')

        except Exception as e:
            print(f'unknown error!{e}')

        finally:
            print('--- finally block ---')
            break

    

    print('-----------------------------')

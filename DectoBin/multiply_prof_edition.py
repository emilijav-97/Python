
if __name__ == '__main__':

    prompt = ('--- Multiplication --- :')
    print(prompt)

    while True:
        try:
            n = (input("Please enter the size of one operand :  "))
            print(f'Entered size is : {n}')

            n = int(n)
            for a in range(2**n):
                for b in range(2**n):
                    p = a * b
                    res = format(p, f'0{n * 2}b')
                    aa = format(a, f'0{n}b')
                    bb = format(b, f'0{n}b')
                    print(f'{a} x {b} = {p}\t{aa} x {bb} = {res}')
            
        except (ValueError, KeyError) as e:
            print(f'invalid value or action ({e})')

        except Exception as e:
            print(f'unknown error!{e}')

        finally:
            print('--- finally block ---')
            break


    print('-----------------------------')

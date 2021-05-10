def decimalToBinary(n):
    return "{0:b}".format(int(n))


if __name__ == '__main__':

    prompt = ('Enter two ranges: :')
    print(prompt)
    while True:
        try:
            a = (input("Please enter the lower range :  "))  # tested from 0
            # to 4, to get the table from the example
            b = (input("Please enter the upper range :  "))

            print(f'Numbers are : {a}, {b}')
            a = int(a)
            b = int(b)
            z = []
            for i in range(a, b):
                for j in range(a, b):
                    x = i * j
                    z.append(decimalToBinary(x))

            #print(f'{z}')
            for x in range(len(z)):
                # print(z[x])
                
                print(decimalToBinary(x))
                #z.append(decimalToBinary(x))
                print(f"{z}")

        except (ValueError, KeyError) as e:
            print(f'invalid value or action ({e})')

        except Exception as e:
            print(f'unknown error!{e}')

        finally:
            print('--- finally block ---')
            break
    
    with open('output30.txt', 'w') as file:
        file.write('\n'.join(str(u) for u in z))

    print('-----------------------------')

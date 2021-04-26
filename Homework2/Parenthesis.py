def check(var, start = 0, curr = 0):
    if start == len(var): return curr == 0
    if curr < 0: return False

    for x in var:
        if var[start] == "(" : 
            return  check(x, start + 1, curr + 1)

        elif var[start] == ")": 
            return  check(x, start + 1, curr - 1)

def check_bal(my_string):
    brackets = ['()', '{}', '[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
    return not my_string
   

if __name__ == '__main__':

    prompt = ('Enter a combination of parenthesis: ')
    var = (input(prompt))

    while True:
        if check_bal(var):
            print(f'{var} are typed right Parenthesis')
            break
        else:
            print(f'{var} are typed wrong Parenthesis')
            break
    print(check_bal(var))
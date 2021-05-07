def decorator_func(l):
    def inner(func):
        def wrapper(*args, **kwargs):

            print("Summation of values : {}".format(l))
            print("Summation of values : {}".format(sum(l)))

            res = []
            [res.append(x) for x in l if x not in res]
            sum1 = 0
            for element in res:
                sum1 += element

            print("List without duplicates : {} ".format(res))    
            print("Sum without duplicates : {} " .format(sum1))

            func(*args, **kwargs)

        return wrapper
    return inner
 
if __name__ == '__main__':

    def my_fun(*args):
        for x in args:
            print(x)

    decorator_func(l = [1,2,3,4,5,5])(my_fun)("I am decorator")
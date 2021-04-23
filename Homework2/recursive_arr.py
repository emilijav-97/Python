def sum_arr(arr,size):
    if (size == 0): return 0
    return arr[size-1] + sum_arr(arr,size-1)

if __name__ == '__main__':   

    n=int(input("Enter the number of elements for list:"))
    a=[]
    
    for i in range (0 ,n):
        element=int(input("Enter element:"))
        a.append(element)

    print(f'The list is: {a}')
    b=sum_arr(a,n)
    print(f'Sum of items in list: {b}')
   
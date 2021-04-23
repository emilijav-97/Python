
def arraycom(z, m):
    dictionary = {}

    for i in range(len(z)):
        comp = m - z[i]
        if comp in dictionary:
            print(f"The following number {m} is represented by: (", z[i],"+",comp,")")
        dictionary[comp] = z[i]

if __name__ == '__main__':
    
    z = [1, 4, 6, 8, 9, 23, 12, 20, 12, 10 ,2]
    m = 12    
    
    arraycom(z, m)
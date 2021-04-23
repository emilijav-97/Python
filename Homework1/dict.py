#update using basic dict methods
if __name__ == "__main__":

    dict_a = {1:10, 2:20}
    dict_b = {3:30, 4:40}
    dict_c = {5:50, 6:60}

    dict_a.update(dict_b)
    dict_a.update(dict_c)
    res = dict_a
    print(res)

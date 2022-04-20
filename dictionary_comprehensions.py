def run():
    # dic = {}
    # for i in range (0,100):
    #     dic[i] = i**3
    # print(dic)

    # my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(my_dict)

    # #RETO:

    dict_sqrt = { i: round(i**(1/2),4) for i in range (500)}
    print(dict_sqrt)


if __name__ == '__main__':
    run()

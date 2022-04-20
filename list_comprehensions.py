def run():
    list_nums = []
    for i in range (0,101):
        list_nums.append(i**2)
    
    print(list_nums)

    squares = [ i for i in range (1,1000)
    if i % 36 == 0 ] 
    print (squares)


if __name__ == '__main__':
    run()
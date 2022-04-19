def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Diego", "lastname": "Quiroga"}
    super_list = [
      {"firstname": "Diego", "lastname": "Quiroga"},
      {"firstname": "Miguel", "lastname": "Torres"},
      {"firstname": "Pepe", "lastname": "Rodelo"},
      {"firstname": "Susana", "lastname": "Martinez"},
      {"firstname": "José", "lastname": "Garcia"}  
    ]
    
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_num": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }
    for key, value in super_dict.items():
        print(f'Clave {key}, valor {value}')

    for dic_in in super_list:
        for key, value in dic_in.items():
         print(f'Clave {key}, valor {value}')
    print(super_list[1]["firstname"])



if __name__ == '__main__':
    run()
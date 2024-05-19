#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                print("wrong type")
                result_list.append(0)
                continue
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            result_list.append(result)
        except IndexError:
            print("out of range")
            result_list.append(0)
    return result_list

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    dvsn = []
    for i in range(list_length):
        rslt = 0
        try:
            rslt = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            dvsn.append(rslt)
    return dvsn

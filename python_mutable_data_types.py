# modifying a list parameter, which is mutable, inside a function
def change_list (a, ls = []):
    ls.append(a)
    return ls
    
ls_1 = change_list(1)
ls_2 = change_list(2)
print("ls_1: ",ls_1)
print("ls_2: ",ls_2)
"""
output:
ls_1:  [1, 2]
ls_2:  [1, 2]
"""    

# try for a dictionary
def func(k, v, dict={}):
    dict[k] = v
    return dict

dict1 = func('mom', 48)
dict2 = func('dad', 56)
dict2['son'] = 21
print(dict1)
# prints {'mom': 48, 'dad': 56, 'son': 21}
# dict (parameter), dict1, and dict2 refer to the same object
"""
In Python, when multiple variables refer to the same mutable object, they act as aliases for that single underlying memory structure. 
This means that modifying the object through one variable will instantly change the value seen by all other variables referencing it. 
This behavior occurs because Python variables do not hold actual values; they hold references (memory addresses) to objects.
"""

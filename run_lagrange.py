from Lagrange import *
import random


def read_num():
    """read the number of variables, return negative number if input is invalid
    """
    num = 0
    n_str = raw_input("How many variables? ")
    try:
        num = int(n_str)
        if num<=1:
            print("Please enter a integer GREATER THAN 1!")
        return num
    except(ValueError):
      print("Please enter an INTEGER!")
      return -1


def read_func(num, input_str):
    """read the constraint of target function with the given variable numbers
    return a tuple. Return (None, None) if input is invalid"""
    string = raw_input("please enter your %s function: "%input_str)
    func = build_func(string)
    try:
        random_input = [random.randint(1,10) for _ in range(num)]
        func(random_input)
        return (string, func)
    except(NameError):
        print("Please enter a Python-recognizable function, with variables named x[0], x[1], ...")
        return (None, None)
    except(IndexError):
        print("Please enter a function with %d variables"%num)
        return (None, None)

         
def calculate():
    """get informaiton from user through terminal, finish the calculation,
    plot the result if there are two variables"""
    num = read_num()
    while num<=1:
        num = read_num() 
    (c_str, cons) = read_func(num, "constraint")
    while c_str==None:
        (c_str, cons) = read_func(num, "constraint")
    (f_str, func) = read_func(num, "target")
    while f_str==None:
        (f_str, func) = read_func(num, "target")
    res = lagrange_multi(func, cons, num)
    if num==2:
        points=[]
        points.append(round(res[0], 5)) 
        points.append(round(res[1], 5))
        plot_res(func, cons, points, f_str, c_str)
    else:
        print ("Sorry, cannot plot result for more than 2 variables")
        result = ""
        for i in range (num):
            result += "x[%d]="%i  + str(round(res[i], 3)) + " "        
        print("The result is %s"%result)        
    pass


while True:
    calculate()












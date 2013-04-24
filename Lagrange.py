from numpy import *
from scipy.misc import derivative
from scipy.optimize import fsolve
import pylab 


def build_func(string):
    """build a function from string. The string should be 
    recoganizable for eval with variable names x[0], x[1], x[2]...
    """
    def res_fun(val):
        x = []
        for number in val:
            x.append(number)
        return eval(string)
    return res_fun
        

def partial_derivative(fun, index, points):
    """calculate the partial derivative. 'fun' is the function, 
    'index' is the index of the input that the derivative is with regard to, 
    'points' is the point
    """
    def temp_func(x):
        inputs = [item for item in points]
        inputs[index] = x
        return fun(inputs)
    #the step is chosen to be 1e-5, a step that is too small will slow down the program
    return derivative(temp_func, points[index], 1e-5)            


def lagrange_multi(fun, cons, n):
    """use the lagrange multiplier to calculate the point where 
    fun can reach its maximum/minimum with constraint cons"""
    def temp_func(x):
        inputs = x[:-1]
        result = []
        for i in range(n):
            result.append(partial_derivative(fun, i, inputs) - x[n]*partial_derivative(cons, i, inputs))
        result.append(cons(inputs))
        return result
    return fsolve(temp_func,x0=tuple([1 for _ in range(n+1)]))


def plot_res(fun, cons, points, stringfunc, stringc):
    """plot a function (fun) that is constraint to cons = 0 at the position 
       points. if the number of variables in the langrange multiplier function 
       is 2, it will call this plotting function"""
    x = linspace(points[0]-2.5, points[0]+2.5, 100)
    y = linspace(points[1]-2.5, points[1]+2.5, 100)
    x, y = meshgrid(x,y)
    zcons = cons([x, y])
    zfun = fun([x, y]) - fun(points)
    pylab.ion()
    pylab.clf()
    pylab.axis([points[0]-2.5, points[0]+2.5, points[1]-2.5, points[1]+2.5]) 
    pylab.plot(points[0], points[1], 'bo')
    pylab.contour(x, y, zcons, 0, colors="r")
    pylab.contour(x, y, zfun, 0, colors="g")
    pylab.title("Lagrange Multiplier with 2 Variables")
    pylab.xlabel("x[0] (x)")
    pylab.ylabel("x[1] (y)")
    pylab.text(points[0]-2.2, points[1]-2, "target function level: %s = %f"%(stringfunc, round(fun(points), 3)))
    pylab.text(points[0]-2.2, points[1]-2.25, "constraint function: %s = 0"%stringc)
    pylab.text(points[0]-0.2, points[1]-0.2, "(%f,%f)"%(points[0], points[1]))
 










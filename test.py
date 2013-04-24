""" Test Script for the Lagrange Multiplier
It includes the flowing constraints problems

1, Constraint: 2x + 3y = 6
   Target Function: F(x,y) = log(x) + log(y)
   Solution: x = 1.5, y = 1

2, Constraint: 2x + y =  9
   Target Function: F(x,y) = x^(1/3)* y^(2/3)
   Solution: x = 1.5, y = 6

3, Constraint: 2x + 6y + z = 8
   Target Function: F(x,y,z) = log(x) + log(y) + log(z)
   Solution: x = 4/3, y = 4/9, z = 8/3
"""




from nose.tools import eq_
from Lagrange import *
from math import *




func1 = build_func("x[0] + x[1]")
func2 = build_func("x[0]**2 + sin(x[1]) + log10(x[2] + x[0])")

func3 = build_func("sin(x[0])*cos(x[1])")
func4 = build_func("x[0]*x[1] + log(x[0])")

func5 = build_func("log(x[0]) + log(x[1])")
func6 = build_func("x[0]**(1.0/3) * x[1]**(2.0/3)")
func7 = build_func("log(x[0]) + log(x[1]) + log(x[2])")
func8 = build_func("2*x[0] + 3*x[1] - 6")
func9 = build_func("2*x[0] + x[1] -9")
func10 = build_func("2*x[0] + 6*x[1] + x[2] -8")




def test_build_func():
    eq_(func1([1,3]), 4)
    eq_(func2([10, 0, 90]), 102)


def test_partial_derivative():
    res1 = round(partial_derivative(func3, 0, [0,0]), 3)
    eq_(res1, 1.0)
    res2 = round(partial_derivative(func4, 1, [5,100]), 3)
    eq_(res2, 5.0)
    res3 = round(partial_derivative(func4, 0, [10, 5]), 3) 
    eq_(res3, 5.1)

       
def test_lagrange_multi():
    res1 = lagrange_multi(func5, func8, 2)
    res2 = lagrange_multi(func6, func9, 2)
    res3 = lagrange_multi(func7, func10, 3)
    eq_(round(res1[0], 3), 1.5)
    eq_(round(res1[1], 3), 1.0)
    eq_(round(res2[0], 3), 1.5)
    eq_(round(res2[1], 3), 6.0)
    eq_(round(res3[0], 3), round(4.0/3, 3))
    eq_(round(res3[1], 3), round(4.0/9, 3))
    eq_(round(res3[2], 3), round(8.0/3, 3))


def main():
    print "\n\nRunning unit tests...\n"
    import nose
    if nose.run(argv=["--with-coverage", "test.py"]):
        print "\nPassed all unit tests"


if __name__ == "__main__":
    # calls main() if we have run this with 'python hw0.py'
    main()




from scipy.optimize import linprog
import numpy as np

# Example: A farmer has recently acquired a 110 hectares piece of land. He has decided to grow Wheat \
#  and barley on that land. Due to the quality of the sun and the region’s excellent climate, the \
#  entire production of Wheat and Barley can be sold. He wants to know how to plant each variety \
#  in the 110 hectares, given the costs, net profits and labor requirements according to the data \
#  shown below:

# Variety   Cost (Price/Hec)	Net Profit (Price/Hec)	    Man-days/Hec
# Wheat	    100	                50	                        10
# Barley	200	                120                         30
#The farmer has a budget of US$10,000 and availability of 1,200 man-days during the planning horizon. Find the optimal solution and the optimal value.

# equations to solve
# x + 2y <= 100
# x + 3y <= 120
# x + y <= 110

# constraints
# x < 0
# y < 0

# cost function (SciPy doesn’t allow you to define maximization \ 
# problems directly. we must convert them to minimization problems.)
# max(z) = 50x + 120y : min(z) = -5x -12y

cost_fn_coef = [-5, -12]

lhs_ineq = [[1, 2], [1, 3], [1, 1]]

rhs_ineq = [100, 120, 110]

# x and y bound from 0 to positive infinity
bnd = [(0, np.inf), (0, np.inf)]

opt = linprog(c=cost_fn_coef, A_ub=lhs_ineq, \
    b_ub=rhs_ineq, bounds=bnd, \
    method="revised simplex")

print(opt)

 # == equality constraints residuals.
 #    con: array([], dtype=float64)
 # == objective function value at the optimum (if found).
 #    fun: -540.0
 # == status of the solution
 #message: 'Optimization terminated successfully.'
 # == number of iterations needed to finish the calculation.
 #    nit: 2
 # == differences between the values of the left and right sides of the constraints.
 #  slack: array([ 0.,  0., 30.])
 # == integer between 0 and 4 that shows the status of the solution, such as 0 for when the optimal solution has been found.
 # status: 0
 # boolean, whether the optimal solution has been found.
 #success: True
 # == array holding the optimal values of the decision variables.
 #      x: array([60., 20.])

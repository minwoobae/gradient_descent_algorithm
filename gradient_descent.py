###########################################################################################################################
# Title: Gradient Descent Algorithm
# Date: 02/13/2019, Wednesday
# Author: Minwoo Bae (minwoo.bae@uconn.edu)
# Institute: The Department of Computer Science and Engineering, UCONN
###########################################################################################################################
import numpy as np
from numpy.linalg import inv, norm
from numpy import transpose as T
from numpy import dot, exp, add, sum, random, abs
from numpy import array as vec

# The Closed form solution to computer coefficients vector w for the linear model:
def closed_form(features, response):

    vars = features
    resp = response
    coeffs = inv(vars.T.dot(vars)).dot(vars.T).dot(resp)

    return coeffs

# Compute a loss function E(w):
def loss_function(features, response, coefficients):

    RSS = 0
    vars = features
    resp = response
    coeffs = coefficients

    RSS = ((resp - vars.dot(coeffs)).T).dot(resp - vars.dot(coeffs))

    return RSS


# Compute the gradient of E(w) at w_k
def get_gradient(features, response, coefficients):

    vars = features
    resp = response
    coeffs = coefficients

    gradient = -2*vars.T.dot((resp - vars.dot(coeffs)))

    return gradient

# Compute the argmin w by using gradient descent algorithm:
def get_argmin_w(features, response, init_coeffs, step_size):

    k = 0
    vars = features
    resp = response
    w_temp = init_coeffs
    a_k = step_size

    error = 0.1
    epsilon = 1e-10 #0.0000000000001

    while epsilon < error:
        w_k = w_temp
        gradient = get_gradient(vars, resp, w_k)
        d_k = -gradient
        w_temp = w_k + a_k*d_k
        error = abs(loss_function(vars, resp, w_temp) - loss_function(vars, resp, w_k))

        print(w_temp)
        print(error)

    return w_temp


#Given data matrices:
X = np.array([[1, 1, 1], [1, 2, 3]]).T
y = np.array([2, 3, 5]).T

#Initial guess for w_0:
w_0 = np.array([0.3,1.4]).T

#Set a step size:
step = 10**(-5)

#Compute a gradient descent algorithm:
argmin_w = get_argmin_w(X, y, w_0, step)
print('Optimal solution w^* by the Gradient descent algorithm:')
print(argmin_w)

#Compute an optimal solution by the closed form:
c_argmin_w = closed_form(X, y)
print('Optimal solution w^* by the closed form:')
print(c_argmin_w)

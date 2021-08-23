# ODE_Approximators
Program that uses various approximation methods for ODE's.

This program calculates Euler's method, improved Euler's method, Taylor Method, and RK4. It allows users to input their function and set initial conditions. Below are some pre-worked out functions that the program works on as example's, rather than requiring users to come up with examples to test the program. Program does not give errors between exact values and approximated values. 

(1) Euler's method example. From the textbook by Tennebaum and Pollard on Ordinary Differential equations, page 639, problem 4.  
Function will prompt for inputs:
function = x+y**2
initial independent = 0
initial dependent = 1
independent = x
dependent = y
height = .05
#of approximations = 5
Outputs:
X     Euler's Approximation
.05       1.05
.10       1.107625
.15       1.173967
.20       1.250377
.25       1.338549


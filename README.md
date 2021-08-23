# ODE_Approximators
Program that uses various approximation methods for ODE's.

This program calculates Euler's method, improved Euler's method, Taylor Method, and RK4. It allows users to input their function and set initial conditions. Below are some pre-worked out functions that the program works on as example's, rather than requiring users to come up with examples to test the program. Program does not give errors between exact values and approximated values. 

(1) Euler's method example. From the textbook by Tennebaum and Pollard on Ordinary Differential equations, page 639, problem 4.<br> 
<b>Function will prompt for inputs:<\b><br>
function = x+y**2<br>
initial independent = 0<br>
initial dependent = 1<br>
independent = x<br>
dependent = y<br>
height = .05<br>
#of approximations = 5<br>
  <b>Outputs:</b><br>
X  &nbsp;&nbsp;   Euler's Approximation<br>
.05  &nbsp;&nbsp;     1.05<br>
.10  &nbsp;&nbsp;     1.107625<br>
.15  &nbsp;&nbsp;     1.173967<br>
.20  &nbsp;&nbsp;     1.250377<br><br>
.25  &nbsp;&nbsp;     1.338549<br>


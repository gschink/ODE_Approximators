import pandas as pd
import numpy as np
from math import *

selector = int(input("Choose from the list of methods\n"
                     "(1) Euler's Method\n"
                     "(2) Improved Euler's Method\n"
                     "(3) Taylor Method\n"
                     "(4) RK4\n"
                     "Enter your choice:"))

#Eulers method calculator, entry of basic information to return the approximation as a data frame.
if selector == 1:
    #This class collects user input and stores it in a centralized location. It cuts down on the number of parameters
    #each function takes later
    class info_bundle:
        y_prime = input('Enter the function to approximate:')
        x_0 = float(input('What is initial value for independent?:'))
        y_0 = float(input('What is your initial value for dependent?:'))
        x = input('Enter the independent variable:')
        y = input('Enter the dependent variable:')
        step_size = float(input('Enter the height you want to use:'))
        number_of_approximations = int(input('How many approximations should we do?:'))

    #This class has information that will change often during the run of Euler's method. It's collected here to cut
    #down on parameters and also give those values a global scope relative to this block.
    class y_holder:
        old_val = 0
        y_val = info_bundle.y_0
        last_step = info_bundle.x_0

    #Creates a list of the steps for use in the data frame.
    def step_creator(info_bundle):
        step_size = info_bundle.step_size
        number_of_approximations = info_bundle.number_of_approximations
        x_set = []

        for num in range(number_of_approximations):
            if len(x_set) == 0:
               x_set.append(info_bundle.x_0 + step_size)
            else:
                x_set.append(x_set[-1] + step_size)

        return x_set

    #Takes the input user string stored in info_bundle, makes changes to y_holder as it is called. It reads the string
    #and inputs values into the correct string position for independent or dependent variable.
    def function_parser(info_bundle, y_holder):
        step = y_holder.last_step
        function_holder = []
        print(step)
        for i in range(len(info_bundle.y_prime)):
            if info_bundle.y_prime[i] == info_bundle.x:
                function_holder.append(str(step))
            elif info_bundle.y_prime[i] == info_bundle.y:
                function_holder.append(str(y_holder.y_val))
            else:
                function_holder.append(info_bundle.y_prime[i])
        t =''.join(function_holder)
        function_holder = []

        y_holder.last_step = y_holder.last_step + info_bundle.step_size

        return t

    #Runs Euler's method by calling the function evaluator and making changes to the y_holder class. Relies on information
    #provided in info_bundle
    def eulers_method(info_bundle, y_holder):
        step = info_bundle.step_size
        runs = info_bundle.number_of_approximations
        combined = []

        for i in range(runs):
            func = function_parser(info_bundle, y_holder)
            print(func)
            y_holder.old_val = y_holder.y_val
            z = step*eval(func)
            end = y_holder.old_val + z
            y_holder.y_val = end
            combined.append(end)

        return combined

    #Simple lines to make and print a df
    data = {'X':step_creator(info_bundle), "Euelr's Method Approximation": eulers_method(info_bundle, y_holder)}
    df = pd.DataFrame(data)
    print(df)

elif selector == 2:
    print('Space Holder')
elif selector == 3:
    print('Space Holder')
elif selector == 4:
    print('Space Holder')
else:
    print('Invalid Selection')

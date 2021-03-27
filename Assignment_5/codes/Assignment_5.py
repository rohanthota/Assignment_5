# -*- coding: utf-8 -*-
"""Assignment 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YYfwvLGx1OGQmnLkDY9OBqStpAx3hyyn
"""

import numpy as np
import random as rd
# import uniform distribution
from matplotlib import pyplot as plt
import math

size_siml = 100000
req_no_x = 0
for i in range(size_siml):
  func_x = rd.uniform(0.0,1.0)
  x = -(math.log(func_x))
  if x > 1:
    req_no_x += 1

prob_x_gr_1 = (req_no_x/size_siml)
print(f"The result obtained from simulation is : {prob_x_gr_1}")
print(f"The result obtained theoretically is : 0.367879")
diff_var_diff = prob_x_gr_1 - 0.367879
print(f"The difference between the simulations' and the theoretical values are : {diff_var_diff}")

x_cood_arr=np.linspace(0,14)
plt.plot(x_cood_arr,np.exp(-x_cood_arr), color='green',label='Probability distribution fn.')
plt.plot(x_cood_arr,1-(np.exp(-x_cood_arr)), color='orange',label='Cumulative distribution fn.')
plt.xlabel("---x---")
plt.ylabel("---f(x) and F(x)---")
plt.grid(True)
plt.legend(loc='best')
plt.title('Plotting probability distribution and cumulative distribution functions.')
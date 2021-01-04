# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:59:30 2021

@author: karina999
"""


import numpy as np

N = 4

grid = np.zeros((N, N), int)
choices = np.random.choice(grid.size, 6, replace=False)
grid.ravel()[choices] = 1

print(grid)
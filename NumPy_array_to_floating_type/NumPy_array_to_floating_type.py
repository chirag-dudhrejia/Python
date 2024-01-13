# -*- coding: utf-8 -*-
"""
NumPy program to convert an array to a floating type.
"""

import numpy as np

arr = np.random.randint(100, size=10)
print(arr)

arr = np.asfarray(arr)
print(arr)
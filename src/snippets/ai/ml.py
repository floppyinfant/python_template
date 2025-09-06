"""
Machine Learning

@see Notebooks/Python_template.ipynb
with links to documentation

@see Data Science Cheat Sheets: https://www.datacamp.com/cheat-sheet
@see ebooks
https://www.datacamp.com/de/blog/the-15-best-data-machine-learning-books-to-read-in-2022
[search Github for Data Science ebooks]
"""

import numpy as np
import pandas as pd
import scipy as sp
import sklearn as sk
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
import bokeh
from numba import jit, njit


# np.info(np.ndarray.dtype)
a = np.array([(0,0,0), (0,0,0)], dtype=np.float64)
print("a: ndim ==", a.ndim, ", shape ==", a.shape, "\n", a)

df = pd.DataFrame(np.random.randn(10, 5))
print(df)

iris = datasets.load_iris


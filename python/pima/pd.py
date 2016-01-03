import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

pd.options.display.mpl_style = 'default'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('pima-indians-diabetes.data', names=names)
data.boxplot()
data.hist()
data.groupby('class').hist()
scatter_matrix(data, alpha=0.2, figsize=(6,6), diagonal= 'kde')

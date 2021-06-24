from sklearn.neighbors import LocalOutlierFactor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('nci1.csv')
number_of_rows = len(data.index)
color_map = []
color_set = ['red','blue','yellow','green','orange','purple']


clf = LocalOutlierFactor(n_neighbors=2)
outliers = clf.fit_predict(data.drop(['type'], axis= 1))
print(outliers)
outlier_factor = clf.negative_outlier_factor_
print(outlier_factor)
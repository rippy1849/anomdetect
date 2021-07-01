from sklearn.svm import OneClassSVM
import pandas as pd

data = pd.read_csv('nci1.csv')
number_of_rows = len(data.index)
color_map = []
color_set = ['red','blue','yellow','green','orange','purple']

clf = OneClassSVM(gamma='auto').fit(data.drop(['type'], axis= 1))
clf_prediction = clf.predict(data.drop(['type'], axis= 1))
print(clf_prediction)

clf_outlier_score = clf.score_samples(data.drop(['type'], axis= 1))
print(clf_outlier_score)
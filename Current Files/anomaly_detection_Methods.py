from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.neighbors import LocalOutlierFactor
import pandas as pd

# Receives: 
# Returns: Pandas Data Frame containing outlier scores and anomaly values
# Task: 
def getIsolationForest(data, data_drop):
    clf = IsolationForest(random_state=0).fit(data_drop)
    data['scores']=clf.decision_function(data_drop)
    data['anomaly_Value']=clf.predict(data_drop)
    anomalyData = {'Scores': data['scores'], 'Anomaly Value': data['anomaly_Value']}
    df = pd.DataFrame(anomalyData, columns = ['Scores', 'Anomaly Value'])
    return df

# Receives: 
# Returns: Pandas Data Frame containing outlier scores and anomaly values
# Task: 
def getOneClassSVMOutlier(data, data_drop):
    clf = OneClassSVM(gamma='auto').fit(data_drop)
    data['scores']=clf.score_samples(data_drop)
    data['anomaly_Value']=clf.predict(data_drop)
    anomalyData = {'Scores': data['scores'], 'Anomaly Value': data['anomaly_Value']}
    df = pd.DataFrame(anomalyData, columns = ['Scores', 'Anomaly Value'])
    return df

# Receives: 
# Returns: Pandas Data Frame containing outlier scores and anomaly values
# Task: 
def getLocalOutlier(data, data_drop):
    clf = LocalOutlierFactor(n_neighbors=2)
    data['scores'] = clf.fit_predict(data_drop)
    data['anomaly_Value'] = clf.negative_outlier_factor_
    anomalyData = {'Scores': data['scores'], 'Anomaly Value': data['anomaly_Value']}
    df = pd.DataFrame(anomalyData, columns = ['Scores', 'Anomaly Value'])
    return df

def main():
    data = pd.read_csv('nci1.csv')
    dataWithDrop = data.drop(['type'], axis= 1)
    
    isolationForest = getIsolationForest(data, dataWithDrop)
    print("Isolation Forest: ")
    print(isolationForest)
    
    oneClassSVM = getOneClassSVMOutlier(data, dataWithDrop)
    print("One Class SVM: ")
    print(oneClassSVM)
    
    localOutlier = getLocalOutlier(data, dataWithDrop) 
    print("Local Outlier: ")
    print(localOutlier)
    
main()
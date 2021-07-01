from pyclustertend import hopkins
import pandas as pd

def getHopkinsStatistic(data, numDataPoints):
    hopkinsStatistic = hopkins(data, numDataPoints)
    return hopkinsStatistic

def main():
    # Read in data
    data = pd.read_csv('nci1.csv')
    data = data.drop(['type'], axis= 1)
    # Determine number of data points in dataset
    numDataPoints = len(data.index)
    # Get hopkins statistic 
    hopkinsStatistic = getHopkinsStatistic(data, numDataPoints)
    print("Hopkins Statistic:", hopkinsStatistic)

main()
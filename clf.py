import csv
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import svm
from sklearn.externals import joblib

def main():
    country_id, year, week = input("Enter countryId year and week:").split()

    region = 0
    if country_id == '1':
    	region = 1
    elif country_id == '2' or country_id == '4':
    	region = 2
    elif country_id == '3':
        region = 3
    elif country_id == '5' or country == '6':
        region = 4

    testdata = np.matrix([country_id, region, year, week])
    C = joblib.load('clf.pkl')
    result = C.predict(testdata)
    result = result[np.newaxis].T
    print(result[0,0])

if __name__ == '__main__':
    main()

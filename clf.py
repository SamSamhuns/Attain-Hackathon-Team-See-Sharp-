import csv
import phaser
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import svm
from sklearn.externals import joblib

def main():
    flag = input("Enter 1 for searching countries and other value for searching regions:")
    C = joblib.load('clf.pkl')


    if flag == 0:
        country = input("Enter country name:")
        year, week = input("Enter year and week:").split()
        country_id = phaser.get_ID_by_name(country)
        region = phaser.get_region(country_id)
        testdata = np.matrix([country_id, region, year, week])
        result = C.predict(testdata)
        result = result[np.newaxis].T
        print(result[0,0])
    else:
        region = input("Enter region name:")
        year, week = input("Enter yeaer and week:").split()
        region_id = phaser.get_ID_by_region(region)
        r = []
        for country in phaser.get_countries(region_id):
            r.append([country, region_id, year, weeek])
        testdata = np.matrix(r)
        result = C.predict(testdata)
        result = result[np.newaxis].T
        print(result)
        

if __name__ == '__main__':
    main()

import csv
import numpy as np
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import svm
#from sklearn import preprocessing

def train(data):
    try:
        csvdata = np.loadtxt(data, delimiter = ',')
        x = np.delete(csvdata, 4, axis = 1)
        y = csvdata[: , 4]
    except:
        print('Error reading data')
    X_train, X_val, y_train, y_val = train_test_split(x, y, test_size = 0.33, random_state = 1)
    #X = preprocessing.scale(X_train)
    clf = svm.SVC(kernel = 'rbf', random_state = 2, C = 50, probability = False)
    clf = clf.fit(X_train, y_train)
    #XV = preprocessing.scale(X_val)
    y_pred = clf.predict(X_val)
    print(accuracy_score(y_val, y_pred))
    #print(confusion_matrix(y_val, y_pred))
    return clf
    
def main():
    C = train('data.csv')
    country_id, year, week = input("Enter countryId year and week:").split()

    region = 0
    if country_id == '1':
    	region = 1
    elif country_id == '2' or country_id == '4':
    	region = 2
    elif country_id == '3':
        region = 3
    else:
        region = 4
        
    testdata = np.matrix([country_id, region, year, week])
    #TD = preprocessing.scale(testdata)
    #TD = preprocessing.scale(testdata)

    result = C.predict(testdata)
    result = result[np.newaxis].T
    print(result[0,0])
    #np.savetxt('pred_3.csv', result, delimiter = ',')

if __name__ == '__main__':
    main()

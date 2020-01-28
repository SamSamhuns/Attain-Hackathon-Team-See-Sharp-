import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
import joblib


def train(data):
    try:
        csvdata = np.loadtxt(data, delimiter=',')
        x = np.delete(csvdata, [4, 5], axis=1)
        y = csvdata[:, 5]
    except:
        print('Error reading data')
    X_train, X_val, y_train, y_val = train_test_split(
        x, y, test_size=0.33, random_state=1)

    clf = svm.SVC(kernel='rbf', random_state=2, C=50, probability=False)
    clf = clf.fit(X_train, y_train)

    y_pred = clf.predict(X_val)
    return clf


def main():
    C = train('data.csv')

    joblib.dump(C, 'clf.pkl')


if __name__ == '__main__':
    main()

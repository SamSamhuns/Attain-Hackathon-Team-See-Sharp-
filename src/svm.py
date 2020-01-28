import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
import joblib


def train(data):
    try:
        csvdata = np.loadtxt(data, delimiter=',')
        x = np.delete(csvdata, [4, 5], axis=1)
        y = csvdata[:, 5]
    except Exception as e:
        print(f'{e}: Error reading data')
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.33, random_state=1)

    clf = svm.SVC(kernel='rbf', random_state=2, C=50, probability=False)
    clf = clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print("Accuracy on test data: ", accuracy(y_pred, y_test))
    return clf

def accuracy(y_pred, y_test):
    if len(y_pred) != len(y_test):
        raise IndexError("Lengths of y_pred and y_test do not match")
    return (sum([1 if pred==test else 0 for pred,test in zip(y_pred, y_test)])/len(y_pred)) * 100

def main():
    C = train('data.csv')

    joblib.dump(C, 'clf.pkl')


if __name__ == '__main__':
    main()

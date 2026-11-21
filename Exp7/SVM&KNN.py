import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#SVM
svm_classifier = SVC(
    kernel="linear",
    C=1
)
svm_classifier.fit(X_train,y_train)
svm_predictions = svm_classifier.predict(X_test)

#KNN
knn_classifier = KNeighborsClassifier(
    n_neighbors = 3
)
knn_classifier.fit(X_train,y_train)
knn_predictions = knn_classifier.predict(X_test)

def evaluate_classifier(y_test,predictions,classifier_name):
    accuracy = accuracy_score(y_test,predictions)
    confusion = confusion_matrix(y_test,predictions)
    classification_rep = classification_report(y_test,predictions,target_names=iris.target_names)

    print("Performance metrics for ",classifier_name)
    print("Accuracy:",accuracy)
    print("Confusion matrix:",confusion)
    print("Classification report:",classification_rep)

evaluate_classifier(y_test,svm_predictions,"SVM")
evaluate_classifier(y_test,knn_predictions,"KNN")
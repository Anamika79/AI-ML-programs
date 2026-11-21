from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB

iris = load_iris()

X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size = 0.30,
    random_state = 42
)

gnb = GaussianNB()
gnb.fit(X_train,y_train)
y_pred = gnb.predict(X_test)

cr = classification_report(
    y_test,
    y_pred,
    target_names = iris.target_names
)

print(cr)
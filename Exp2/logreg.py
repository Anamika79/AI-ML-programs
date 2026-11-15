import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score,recall_score,f1_score,accuracy_score

df = pd.read_csv("diabetes.csv")

print("First 5 rows of the dataset")
print(df.head())

# Convert the dataset into X (input features) and y (target)
X = df.drop(columns="Outcome")
y = df["Outcome"] 

# Split X and y into training and testing data
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size = 0.30,
    random_state = 42
)

# Create and train Logistic Regression model
model = LogisticRegression(max_iter=140)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

# Display actual and predicted outcomes
print("\nActual Outcome vs Predicted Outcome")

comparison = pd.DataFrame({
    "Actual outcome" : y_test.values,
    "Predicted outcomes" : y_pred
})

print(comparison.head(10))

pr = precision_score(y_test,y_pred)
re = recall_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred)
ac = accuracy_score(y_test,y_pred)

print("\nModel Evaluation")
print("Precision : ",pr)
print("Recall : ",re)
print("F1 score : ",f1)
print("Accuracy : ",ac)

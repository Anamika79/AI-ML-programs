import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

df = pd.read_csv("USA_Housing.csv")

print("First five rows : ")
print(df.head())

print("Column names : ")
print(df.columns)

X = df[["Avg. Area Income"]]
y = df["Price"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size = 0.30,
    random_state = 42
)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("\nActual Price vs Predicted Price")

comparison = pd.DataFrame({
    "Actual price" : y_test.values,
    "Predicted price" : y_pred
})

print(comparison.head(10))

rmse = mean_squared_error(y_test,y_pred) ** 0.5
r2 = r2_score(y_test,y_pred)

print("Model Evaluation\n")
print("RMSE : ",rmse)
print("R2 score: ",r2)
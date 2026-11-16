import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

df = pd.read_csv("USA_Housing.csv")

print(df.columns)

df.drop(columns = "Address",inplace=True)
X = df.drop(columns = "Price")
y = df["Price"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size = 0.30,
    random_state = 42
)

#Create polynomial features with degree=3
poly = PolynomialFeatures(degree=3)

#Transform training and testing data
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly,y_train)

y_pred = model.predict(X_test_poly)

print("Actual price vs Predicted price")
comparison = pd.DataFrame({
    "Actual prices" : y_test.values,
    "Predicted prices" : y_pred
})

print(comparison.head(10))

rmse = mean_squared_error(y_test,y_pred) ** 0.5
r2 = r2_score(y_test,y_pred)

print("RMSE : ",rmse)
print("R2 score : ",r2)


import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from LinearRegressionSkeleton import LinearRegression
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

X = df['petal width (cm)'].values
y = df['sepal length (cm)'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_regression = LinearRegression(epochs=1000, lr=1e-3)
linear_regression.fit(X_train, y_train)

y_pred = linear_regression.predict(X_test)

# Mean Absolute Error
mae = np.mean(np.abs(y_pred - y_test))
print("Mean Absolute Error:", mae)

# Mean Squared Error
mse = np.mean((y_pred - y_test)**2)
print("Mean Squared Error:", mse)

# Plot the results
plt.scatter(X_test, y_test)
plt.plot([min(X_test), max(X_test)], [min(y_pred), max(y_pred)], color='red')
plt.show()
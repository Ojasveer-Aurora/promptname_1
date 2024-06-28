import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    'Years of Experience': [1.2, 1.4, 1.6, 2.1, 2.3, 3, 3.1, 3.3, 3.3, 3.8, 4, 4.1, 4.1, 4.2, 4.6, 5, 5.2, 5.4, 6, 6.1, 6.9, 7.2, 8, 8.3, 8.8, 9.1, 9.6, 9.7, 10.4, 10.6],
    'Salary': [39344, 46206, 37732, 43526, 39892, 56643, 60151, 54446, 64446, 57190, 63219, 55795, 56958, 57082, 61112, 67939, 66030, 83089, 81364, 93941, 91739, 98274, 101303, 113813, 109432, 105583, 116970, 112636, 122392, 121873]
}

df = pd.DataFrame(data)

x = df[['Years of Experience']]
y = df['Salary']

Xtrain, Xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=30)

model = LinearRegression()
model.fit(Xtrain, ytrain)

y_pred = model.predict(Xtest)

plt.figure(figsize=(10, 6))
plt.plot(Xtest, y_pred, color='red', linewidth=2, label='The Predicted Salary')
plt.ylabel('Salary(in $[dolars])')
plt.title('Salary VS Years of Experience')
plt.scatter(x, y, color='blue', label='The Actual Salary')
plt.grid(True)
plt.xlabel('Years of Experience')
plt.legend()
plt.show()

print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_[0]}")
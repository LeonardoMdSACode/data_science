from sklearn import tree
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the boston housing dataset
boston = load_boston()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.3, random_state=0)

# Create a decision tree regressor
clf = tree.DecisionTreeRegressor()

# Train the regressor on the training data
clf.fit(X_train, y_train)

# Predict the target values of the testing data
y_pred = clf.predict(X_test)

# Evaluate the performance of the regressor
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# use trained regressor to predict the target values of the testing data and evaluate its performance using the mean squared error
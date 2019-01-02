# Step 0: Import Libraries
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
# Load Data
# Step 1: Data import
from sklearn.datasets import load_boston
boston = load_boston()
print([i for i in boston.keys()])
boston_DF = pd.DataFrame(boston.data)
print(boston_DF.head(5))
boston_DF.columns = boston.feature_names
print(boston_DF.head(5))
print(boston.DESCR)
print(boston.target.shape)
print(boston.target)

boston_DF["PRICE"] = boston.target
print(boston_DF)
print(boston_DF.describe())

print('''
Split train-test dataset. Unlike titanic dataset, this time we only given a single dataset. No train and test dataset. That’s fine, we can split it by our self. Basically, before splitting the data to train-test dataset, we would need to split the dataset into two: target value and predictor values. Let’s call the target value Y and predictor values X. Thus, 
Y = Boston Housing Price
X = All other features''')


X = boston_DF.drop('PRICE', axis = 1)
Y = boston_DF['PRICE']
print(Y.size)
print(X.size)

# As there is no null values in the dataset, there is no need for cleaning the data. 
# We can move to next step directly and import the required library for Linear regression

from sklearn.linear_model import LinearRegression
import seaborn as sns; 
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)
sns.pairplot(boston_DF,  x_vars=['CRIM', 'ZN', 'INDUS', 'CHAS'], y_vars='PRICE', size=7, aspect=0.7, kind='reg')
sns.pairplot(boston_DF,  x_vars=[ 'NOX', 'RM', 'AGE', 'DIS', 'RAD'], y_vars='PRICE', size=7, aspect=0.7, kind='reg')
sns.pairplot(boston_DF,  x_vars=['TAX', 'PTRATIO', 'B', 'LSTAT'], y_vars='PRICE', size=7, aspect=0.7, kind='reg')
sns.pairplot(boston_DF,size=7, aspect=0.7, kind='reg')
plt.show()

# correlation
pd.set_option('precision',2)
print(boston_DF.corr())
# Now, we can finally split the dataset into train and test with the snippet below.
# Since, "LSTAT" and "RM" both are comparatively strongly co-related to price, we take only those two for our prediction
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X[['RM','LSTAT']], Y, test_size = 0.2, random_state = 5)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

# Now, train the model
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train, Y_train)

# Predict Output
Y_pred = lm.predict(X_test)

# Test Model
plt.scatter(Y_test, Y_pred)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")
plt.show()

# We now have a model. Let's try to find out the mean squared error.

mse = sklearn.metrics.mean_squared_error(Y_test, Y_pred)
print(mse)

# Since, Mean Square Error is very high, that means that the model isn’t a really great linear model.
# coefficient of determination == R Square 
print("R square: {0}".format(sklearn.metrics.r2_score(Y_test, Y_pred)))

# Since, the R-Square score is too far from 1, the problem doesn't seem to be fit for the Linear regression




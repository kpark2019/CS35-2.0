#
#
# titanic.py
#
#

import numpy as np
from sklearn import datasets
from sklearn import cross_validation
import pandas as pd

# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
df = pd.read_csv('titanic.csv', header=0)
df.head()
df.info()

# let's drop columns with too few values or that won't be meaningful
# Here's an example of dropping the 'body' column:
df = df.drop('body', axis=1)  # axis = 1 means column
df = df.drop('cabin', axis=1)
df = df.drop('boat', axis=1)
df = df.drop('name', axis=1)
df = df.drop('home.dest', axis=1)
df = df.drop('ticket', axis=1)

# let's drop all of the rows with missing data:
df = df.dropna()

# let's see our dataframe again...
# I ended up with 1001 rows (anything over 500-600 seems reasonable)
df.head()
df.info()



# You'll need conversion to numeric datatypes for all input columns
#   Here's one example
#
def tr_mf(s):
    """ from string to number
    """
    d = { 'male':0, 'female':1 }
    return d[s]

df['sex'] = df['sex'].map(tr_mf)  # apply the function to the column

# let's see our dataframe again...
df.head()
df.info()


# you will need others!
def tr_embarks(s):
    d = {'S':0, 'C':1, 'Q':2}
    return d[s]
df['embarked'] = df['embarked'].map(tr_embarks)

df.head()
df.info()


print("+++ end of pandas +++\n")

# import sys
# sys.exit(0)

print("+++ start of numpy/scikit-learn +++")

# We'll stick with numpy - here's the conversion to a numpy array

# extract the underlying data with the values attribute:
X_data = df.drop('survived', axis=1).values        # everything except the 'survival' column
y_data = df[ 'survived' ].values      # also addressable by column name(s)

#
# you can take away the top 42 passengers (with unknown survival/perish data) here:
# Drops the unknown rows to test known data
X_data = X_data[44:,:]   #2d array
y_data= y_data[44:]    #1d column

# scrambles the data
indices = np.random.permutation(len(X_data))
X_data = X_data[indices]
y_data = y_data[indices]

# feature engineering...
#X_data[:,3] *= 100   # maybe the fourth column is worth much more!
X_data[:,1] *= 100
X_data[:,2] *= 100
X_data[:,5] *= 100

# tests the first 15, then using the rest as trtaining
X_test = X_data[0:44,0:15]     #testing
X_train = X_data[44:,0:15]     #training

y_test = y_data[0:44]       #testing (unknown)
y_train = y_data[44:]       #testing (known)





#
# the rest of this model-building, cross-validation, and prediction will come here:
#     build from the experience and code in the other two examples...

from sklearn.neighbors import KNeighborsClassifier

testing_list = []
best_score = 0
index = 0

#using 1,16 for training part of the training data cross validating
for i in range(1,16):
    score = 0
    knn = KNeighborsClassifier(n_neighbors=i) # i as k

    #Cross validate, 6 out of the 30 used  to test
    for j in range (1,16):
        cv_data_train, cv_data_test, cv_target_train, cv_target_test = \
        cross_validation.train_test_split(X_train, y_train, test_size=0.2)

    #fitting the model using cv data
        knn.fit(cv_data_train, cv_target_train)
        score += knn.score(cv_data_test,cv_target_test)
        print("The score is ", score)
    average_score = score/10

    print("KNN cv training-data score is:", knn.score(cv_data_train,cv_target_train))
    print("KNN cv testing-data score is:", knn.score(cv_data_test,cv_target_test))
    print('The average score is', average_score)

    if average_score > best_score:
        best_score = average_score
        index = i

print('The best number of neighbors is', index)
print("The best score is ", best_score)


knn = KNeighborsClassifier(n_neighbors=index)
cv_data_train, cv_data_test, cv_target_train, cv_target_test = \
cross_validation.train_test_split(X_train, y_train, test_size=0.2)
knn.fit(cv_data_train, cv_target_train)

#Train the model with all data then predict
#full data
knn.fit(X_train, y_train)
print("\nCreated and trained a knn classifier")

# examples
print("digit_X_test's predicted outputs are")
print(knn.predict(X_test))

# iris datatypes
print("and the actual labels are")
print(y_test)

for i in range(len(df.index)):
    if df["survived"].iloc[i] == -1:
        df["survived"].iloc[i] = knn.predict(X_test[i])[0]
print(df)
"""
Comments and results:

Briefly mention how this went:
  + what value of k did you decide on for your kNN?
  The k value was 15
  + how high were you able to get the average cross-validation (testing) score?
  Our score was .71


Then, include the predicted labels of the 12 digits with full data but no label:
Past those labels (just labels) here:[1 0 1 0 0 0 1 1 0 0 1 0 1 1 1 1 0 0 0 0 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1
 0 0 1 1 1 0 1]
You'll have 12 lines:




And, include the predicted labels of the 10 digits that are "partially erased" and have no label:
Mention briefly how you handled this situation!?

Past those labels (just labels) here:[1 0 0 0 0 1 1 0 1 1 0 1 0 1 1 1 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 1 1 1 0 0 1
 1 0 1 1 0 0 0]
The partially erased ones and the ones that had a lot missing from the chart were dropped.
Also the other data that was irrelevant were dropped also. 
You'll have 10 lines:



"""

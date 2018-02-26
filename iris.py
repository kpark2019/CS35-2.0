#
#
# iris.py
#
#

import numpy as np
from sklearn import *
import pandas as pd
from collections import Counter

print("+++ Start of pandas +++\n")
# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
df = pd.read_csv('iris.csv', header=0)    # read the file
df.head()                                 # first five lines
df.info()                                 # column details

# There are many more features to pandas...  Too many to cover here

# One important feature is the conversion from string to numeric datatypes!
# As input features, numpy and scikit-learn need numeric datatypes
# You can define a transformation function, to help out...
def transform(s):
    """ from string to number
          setosa -> 0
          versicolor -> 1
          virginica -> 2
    """
    d = { 'unknown':-1, 'setosa':0, 'versicolor':1, 'virginica':2 }
    return d[s]

def transformBack(numbers):
    d = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    words = []
    for i in range(len(numbers)):
        words.append(d[numbers[i]])
    return words
    
# 
# this applies the function transform to a whole column
#
df['irisname'] = df['irisname'].map(transform)  # apply the function to the column

print("+++ End of pandas +++\n")

print("+++ Start of numpy/scikit-learn +++")
# Data needs to be in numpy arrays - these next two lines convert to numpy arrays
X_data_full = df.iloc[:,0:4].values        # iloc == "integer locations" of rows/cols
y_data_full = df[ 'irisname' ].values      # individually addressable columns (by name)

#print(y_data_full)
#
# we can drop the initial (unknown) rows -- if we want to test with known data
# X_data_full = X_data_full[9:,:]   # 2d array
# y_data_full = y_data_full[9:]     # 1d column


#
# we can scramble the remaining data if we want - only if we know the test set's labels
# 
# indices = np.random.permutation(len(X_data_full))  # this scrambles the data each time
# X_data_full = X_data_full[indices]
# y_data_full = y_data_full[indices]



#
# The first nine are our test set - the rest are our training
#
X_test = X_data_full[0:9,0:4]              # the final testing data
#print(X_test)
#print(X_data_full)
X_train = X_data_full[9:,0:4]              # the training data

y_test = y_data_full[0:9]                  # the final testing outputs/labels (unknown)
y_train = y_data_full[9:]                  # the training outputs/labels (known)



#
# feature engineering...
#


# here is where you can re-scale/change column values...
# X_data[:,0] *= 100   # maybe the first column is worth 100x more!
# X_data[:,3] *= 100   # maybe the fourth column is worth 100x more!




#
# create a kNN model and tune its parameters (just k!)
#   here's where you'll loop to run 5-fold (or 10-fold cross validation)
#   and loop to see which value of n_neighbors works best (best cv testing-data score)
#
from sklearn.neighbors import KNeighborsClassifier
# bestlist = []
# best = [0, 0]
# for x in range(50): # test this 50 times to ensure we are getting the true best number of neighbours
#     print("Trial", x)
#     for i in range(1, 100, 2): # testing odd numbers betwen k = 100, and k = 1 to find the best number
#         #print("\n\nNumber of Neighbours:", i)
#         knn = KNeighborsClassifier(n_neighbors=i)   # 15 is the "k" in kNN
#
#         #
#         # cross-validate (use part of the training data for training - and part for testing)
#         #   first, create cross-validation data (here 3/4 train and 1/4 test)
#
#         # loop ten times to accumulate data and then average
#         traindata = 0
#         testdata = 0
#         for j in range(10):
#             cv_data_train, cv_data_test, cv_target_train, cv_target_test = \
#                 cross_validation.train_test_split(X_train, y_train, test_size=0.25) # random_state=0
#
#             # fit the model using the cross-validation data
#             #   typically cross-validation is used to get a sense of how well it works
#             #   and tune any parameters, such as the k in kNN (3? 5? 7? 41?, etc.)
#             knn.fit(cv_data_train, cv_target_train)
#             traindata += knn.score(cv_data_train,cv_target_train)
#             testdata += knn.score(cv_data_test,cv_target_test)
#         #print("KNN cv AVERAGE training-data score:", traindata / 10)
#         #print("KNN cv AVERAGE testing-data score:", testdata / 10)
#
#         if best[0] <= testdata / 10:
#             best[0] = testdata / 10
#             best[1] = i
#         else:
#             pass
#
#
#         #
#         # now, train the model with ALL of the training data...  and predict the labels of the test set
#         #
#
#         # this next line is where the full training data is used for the model
#         knn.fit(X_train, y_train)
#         #print("\nCreated and trained a knn classifier")  #, knn
#
#         # here are some examples, printed out:
#         #print("iris_X_test's predicted outputs are")
#         #print(knn.predict(X_test))
#
#         # and here are the actual labels (iris types)
#         #print("and the actual labels are")
#         #print(y_test)
#
#     #print(best)
#     bestlist.append(best[1])
#
# finalBestCounter = Counter(bestlist)
# print(finalBestCounter)


knn = KNeighborsClassifier(n_neighbors=15)   # 15 is the "k" in kNN
cv_data_train, cv_data_test, cv_target_train, cv_target_test = \
                cross_validation.train_test_split(X_train, y_train, test_size=0.25) # random_state=0
# fit the model using the cross-validation data
#   typically cross-validation is used to get a sense of how well it works
#   and tune any parameters, such as the k in kNN (3? 5? 7? 41?, etc.)
knn.fit(cv_data_train, cv_target_train)
traindata = knn.score(cv_data_train,cv_target_train)
testdata = knn.score(cv_data_test,cv_target_test)


# now, train the model with ALL of the training data...  and predict the labels of the test set
#
# this next line is where the full training data is used for the model
knn.fit(X_train, y_train)
print("\nCreated and trained a knn classifier")  #, knn

# test the nine
print("iris_X_test's predicted outputs are")
finalData = knn.predict(X_test)
print(finalData)

# print this out to make sure that they are all unknowns
print("and the actual labels are")
print(y_test)

words = transformBack(finalData)
print(words)

# 
# here is where you'll more elegantly format the output - for side-by-side comparison
#     then paste your results for the unknown irises below
#

#[1 2 1 1 0 0 2 1 0]
#[1 2 1 1 0 0 2 1 0]



#
# for testing values typed in
#
def test_by_hand(knn):
    """ allows the user to enter values and predict the
        label using the knn model passed in
    """
    print()
    Arr = np.array([[0,0,0,0]]) # correct-shape array
    T = Arr[0]
    T[0] = float(input("sepal length? "))
    T[1] = float(input("sepal width? "))
    T[2] = float(input("petal length? "))
    T[3] = float(input("petal width? "))
    prediction = knn.predict(Arr)[0]
    print("The prediction is", prediction)
    print()


# import sys   # easy to add break points...
# sys.exit(0)


"""
Comments and results:

Briefly mention how this went:
  + what value of k did you decide on for your kNN?

    We decided on the value 15, because we ran a for loop with a counter for each "best" k value
    and ended up with a wide majority in favor of 15 (24 times / 50 tests)

  + how smoothly did this kNN workflow go...
    
    It ended up going pretty well, we also ran this test multiple times and ended up with the
    same output


Then, include the predicted labels of the first 9 irises (with "unknown" type)
Paste those labels (or both data and labels here)
You'll have 9 lines:

1. versicolor
2. virginica
3. versicolor
4. versicolor
5. setosa
6. setosa
7. virginica
8. versicolor
9. setosa

"""

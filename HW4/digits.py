#
#
# digits.py
#
#

import numpy as np
from sklearn import cross_validation
import pandas as pd
from collections import Counter

# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
df = pd.read_csv('digits.csv', header=0)
df.head()
df.info()

# Convert feature columns as needed...
# You may to define a function, to help out:
def transform(s):
    """ from number to string
    """
    return 'digit ' + str(s)
    
df['label'] = df['64'].map(transform)  # apply the function to the column
print("+++ End of pandas +++\n")

# import sys
# sys.exit(0)

print("+++ Start of numpy/scikit-learn +++")

# We'll stick with numpy - here's the conversion to a numpy array
X_data = df.iloc[:,0:64].values        # iloc == "integer locations" of rows/cols
y_data = df[ 'label' ].values      # also addressable by column name(s)

#print("X_data", X_data)

#
# you can divide up your dataset as you see fit here...
#

X_test1 = X_data[0:10,0:36]              # the testing data (half of a digit)
X_test2 = X_data[10:22,0:64]             # the testing data (full digit)
X_train1 = X_data[22:,0:36]              # the training data
X_train2 = X_data[22:, 0:64]

y_test1 = y_data[0:10]                  # the final testing outputs/labels (unknown)
y_test2 = y_data[10:22]
y_train1 = y_data[22:]                  # the training outputs/labels (known)

#
# This is what I used to check for the best value of k
#
X_test = X_data[23:45,0:64]              # the final testing data
X_train = X_data[45:,0:64]              # the training data

y_test = y_data[23:45]                  # the final testing outputs/labels (unknown)
y_train = y_data[45:]                  # the training outputs/labels (known)

#
# Use this to find your best 'k' value
# Took forever... 5 minutes per trial :(
#
#
from sklearn.neighbors import KNeighborsClassifier
# bestlist = []
# best = [0, 0]
# for x in range(20): # test this 50 times to ensure we are getting the true best number of neighbours
#     print("Starting Trial", x)
#     for i in range(1, 100, 2): # testing odd numbers betwen k = 100, and k = 1 to find the best number
#         #print("\n\nNumber of Neighbours:", i)
#         knn = KNeighborsClassifier(n_neighbors=i)   # 15 is the "k" in kNN
#
#         #
#         # cross-validate (use part of the training data for training - and part for testing)
#         #   first, create cross-validation data (here 3/4 train and 1/4 test)
#         #
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

#
# This is the real code that I will be running
#

knn = KNeighborsClassifier(n_neighbors=15)   # __ is the "k" in kNN
cv_data_train, cv_data_test, cv_target_train, cv_target_test = \
                cross_validation.train_test_split(X_train, y_train, test_size=0.25) # random_state=0
knn.fit(cv_data_train, cv_target_train)
traindata = knn.score(cv_data_train,cv_target_train)
testdata = knn.score(cv_data_test,cv_target_test)

# now, train the model with ALL of the training data...  and predict the labels of the test set
#
# this next line is where the full training data is used for the model
knn.fit(X_train1, y_train1)
print("\nCreated and trained a knn classifier")  #, knn

# test the 22
print("Half-Digit predicted outputs are")
finalData = knn.predict(X_test1)
print(finalData)

# print this out to make sure that they are all unknowns
print("These should all be -1:")
print(y_test1)

knn.fit(X_train2, y_train1)
print("\nCreated and trained a knn classifier")  #, knn

# test the 22
print("Full-Digit predicted outputs are")
finalData = knn.predict(X_test2)
print(finalData)

# print this out to make sure that they are all unknowns
print("These should all be -1:")
print(y_test2)

#
# feature display - use %matplotlib to make this work smoothly
#
from matplotlib import pyplot as plt

def show_digit( Pixels ):
    """ input Pixels should be an np.array of 64 integers (from 0 to 15) 
        there's no return value, but this should show an image of that 
        digit in an 8x8 pixel square
    """
    print(Pixels.shape)
    Patch = Pixels.reshape((8,8))
    plt.figure(1, figsize=(4,4))
    plt.imshow(Patch, cmap=plt.cm.gray_r, interpolation='nearest')  # cm.gray_r   # cm.hot
    plt.show()
    
# # try it!
# row = 0
# Pixels = X_data[row:row+1,:]
# show_digit(Pixels)
# print("That image has the label:", y_data[row])


"""
Comments and results:

Briefly mention how this went:
  + what value of k did you decide on for your kNN?
    After going through the same procedure as the iris dataset 
    (which meant having 20 trials testing all odd numbers from 1-99, with a repetition of ten
    for each average) we actually ended up coming to the value 1. Out of the 20 trials we ran,
    12/20 => 1, 7/20 => 3, 1/20 => 5 were the best k values.
    
  + how smoothly were you able to adapt from the iris dataset to here?
    It was almost exactly the same, except that we had to limit the number 
    of trials due to the length of each trial (around 5 minutes). We also had to switch
    the indices, but that was to be expected.
    
  + how high were you able to get the average cross-validation (testing) score?
    Our highest score was 0.98...... but it was pretty good for the knn process.



Then, include the predicted labels of the 12 digits with full data but no label:
Past those labels (just labels) here:
You'll have 12 lines:

11. 9
12. 9
13. 5
14. 5
15. 6
16. 5
17. 0
18. 5
19. 8
20. 9
21. 8
22. 4

And, include the predicted labels of the 10 digits that are "partially erased" and have no label:

Past those labels (just labels) here:
You'll have 10 lines:

1. 0
2. 0
3. 0
4. 1
5. 7
6. 2
7. 3
8. 6
9. 0
10. 1

Mention briefly how you handled this situation?
    Instead of using the full 64 columns in a row, I only used half of them to compare to each other.
    This seemed logical, considering that comparing a bunch of 0's to actual values seemed illogical:
    there was no way we could even hope to get a decent match. So we went with the next best thing: comparing
    what we did have.
    
    In order to do this, we did the following:
        1) Split by Rows 1-10 (we looked at them manually to find out which ones were missing half)
        2) Run knn process with same k value (we didn't end up having time to run the trials a second time)
        3) Fill in the blanks by comparing to other sets with the same value (We didn't actually get to this step)
"""
#
# digits5: modeling the digits data with DTs and RFs
#


import numpy as np            
import pandas as pd

from sklearn import tree      # for decision trees
from sklearn import ensemble  # for random forests
from collections import Counter

try: # different imports for different versions of scikit-learn
    from sklearn.model_selection import cross_val_score   # simpler cv this week
except ImportError:
    try:
        from sklearn.cross_validation import cross_val_score
    except:
        print("No cross_val_score!")

#
# The "answers" to the 20 unknown digits, labeled -1:
#
answers = [9,9,5,5,6,5,0,9,8,9,8,4,0,1,2,3,4,5,6,7]


print("+++ Start of pandas' datahandling +++\n")
# df here is a "dataframe":
df = pd.read_csv('digits5.csv', header=0)    # read the file w/header row #0
df.head()                                 # first five lines
df.info()                                 # column details
print("\n+++ End of pandas +++\n")


print("+++ Start of numpy/scikit-learn +++\n")
# Data needs to be in numpy arrays - these next two lines convert to numpy arrays
X_all = df.iloc[:,0:64].values        # iloc == "integer locations" of rows/cols
y_all = df[ '64' ].values      # individually addressable columns (by name)

#print(y_all)


# X_data_full = X_all[0:,:]  #
# y_data_full = y_all[0:]    #


#
# now, model from iris5.py to try DTs and RFs on the digits dataset!
#

##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################

print("     +++++ Decision Trees +++++\n\n")

X_labeled = X_all[20:,:]  # make the 10 into 0 to keep all of the data
y_labeled = y_all[20:]    # same for this line

#
# we can scramble the data - but only the labeled data!
#
indices = np.random.permutation(len(X_labeled))  # this scrambles the data each time
X_data_full = X_labeled[indices]
y_data_full = y_labeled[indices]

X_train = X_data_full
y_train = y_data_full

#
# some labels to make the graphical trees more readable...
#
print("Some labels for the graphical tree:")

feature_names = []
for i in range(0, 64):
    feature_names.append("Pixel " + str(i))

#print(feature_names)

target_names = []
for j in range(0, 10):
    target_names.append(str(j))

#
# show the creation of three tree files (at three max_depths)
#
for max_depth in [1,2,3,4]:
    # the DT classifier
    dtree = tree.DecisionTreeClassifier(max_depth=max_depth)

    # train it (build the tree)
    dtree = dtree.fit(X_train, y_train)

    # write out the dtree to tree.dot (or another filename of your choosing...)
    filename = 'tree' + str(max_depth) + '.dot'
    tree.export_graphviz(dtree, out_file=filename,   # the filename constructed above...!
                            feature_names=feature_names,  filled=True,
                            rotate=False, # LR vs UD
                            class_names=target_names,
                            leaves_parallel=True )  # lots of options!
    #
    # Visualize the resulting graphs (the trees) at www.webgraphviz.com
    #
    print("Wrote the file", filename)
    #


#
# cross-validation and scoring to determine parameter: max_depth
#
best_score = 0
best_depth = 0
for max_depth in range(40,55):
    # create our classifier
    dtree = tree.DecisionTreeClassifier(max_depth=max_depth)
    #
    # cross-validate to tune our model (this week, all-at-once)
    #
    scores = cross_val_score(dtree, X_train, y_train, cv=5)
    average_cv_score = scores.mean()
    if average_cv_score >= best_score:
        best_depth = max_depth
        best_score = average_cv_score
    print("For depth=", max_depth, "average CV score = ", average_cv_score)
    #print("      Scores:", average_cv_score)

print("Depth:", best_depth)
print("Score:", best_score)

# import sys
# print("bye!")
# sys.exit(0)

MAX_DEPTH = best_depth   # choose a MAX_DEPTH based on cross-validation...
print("\nChoosing MAX_DEPTH =", MAX_DEPTH, "\n")

#
# now, train the model with ALL of the training data...  and predict the unknown labels
#

X_unknown = X_all[0:20,0:64]              # the final testing data
X_train = X_all[20:,0:64]              # the training data

y_unknown = y_all[0:20]                  # the final testing outputs/labels (unknown)
y_train = y_all[20:]                  # the training outputs/labels (known)

# our decision-tree classifier...
dtree = tree.DecisionTreeClassifier(max_depth=MAX_DEPTH)
dtree = dtree.fit(X_train, y_train)

#
# and... Predict the unknown data labels
#
print("Decision-tree predictions:\n")
predicted_labels = dtree.predict(X_unknown)
answer_labels = answers

#
# formatted printing! (docs.python.org/3/library/string.html#formatstrings)
#
s = "{0:<11} | {1:<11}".format("Predicted","Answer")
#  arg0: left-aligned, 11 spaces, string, arg1: ditto
print(s)
s = "{0:<11} | {1:<11}".format("-------","-------")
print(s)
# the table...
for p, a in zip( predicted_labels, answer_labels ):
    s = "{0:<11} | {1:<11}".format(p,a)
    print(s)

#
# feature importances!
#
print()
print("dtree.feature_importances_ are\n      ", dtree.feature_importances_)
print("Order:", feature_names[0:64])











print("\n\n")
print("     +++++ Random Forests +++++\n\n")

#
# The data is already in good shape -- let's start from the original dataframe:
#
# Data needs to be in numpy arrays - these next two lines convert to numpy arrays
X_all = df.iloc[:,0:64].values        # iloc == "integer locations" of rows/cols
y_all = df[ '64' ].values      # individually addressable columns (by name)

X_labeled = X_all[20:,:]
y_labeled = y_all[20:]

#
# we can scramble the data - but only the labeled data!
#
indices = np.random.permutation(len(X_labeled))  # this scrambles the data each time
X_data_full = X_labeled[indices]
y_data_full = y_labeled[indices]

# X_train = X_data_full
# y_train = y_data_full


#
# cross-validation to determine the Random Forest's parameters (max_depth and n_estimators)
#

#
#   + loop over a number of values of max_depth (m)
#   + loop over different numbers of trees/n_estimators (n)
#   -> to find a pair of values that results in a good average CV score
#
# use the decision-tree code above as a template for this...
#

# here is a _single_ example call to build a RF:
#m = 2
#n = 10
count = 0
# stores a count of all 'm' values to see what the optimal one was
mnVal = []
totalMN = 0
for m in range(30, 35, 1):
    print("m:", m)
    totalN = 0
    nVal = 0
    for n in range(70, 75, 1):
        print("[m:", m, ",n:", str(n) + "]")
        rforest = ensemble.RandomForestClassifier(max_depth=m, n_estimators=n)

        # an example call to run 5x cross-validation on the labeled data
        scores = cross_val_score(rforest, X_train, y_train, cv=5)
        #print("CV scores:", scores)
        #print("CV scores' average:", scores.mean())
        if totalN <= scores.mean():
            totalN = scores.mean()
            nVal = n

    if totalMN < totalN:
        mnVal = [m, nVal]
        totalMN = totalN

    print("Top score:", totalMN)

print("Best Values:", mnVal)
print("Score:", totalMN)

#
# now, train the model with ALL of the training data...  and predict the labels of the test set
#

X_test = X_all[0:20,0:64]              # the final testing data
X_train = X_all[20:,0:64]              # the training data

y_test = y_all[0:20]                  # the final testing outputs/labels (unknown)
y_train = y_all[20:]                  # the training outputs/labels (known)

# these next lines is where the full training data is used for the model
MAX_DEPTH = mnVal[0]
NUM_TREES = mnVal[1]
print()
print("Using MAX_DEPTH=", MAX_DEPTH, "and NUM_TREES=", NUM_TREES)
rforest = ensemble.RandomForestClassifier(max_depth=MAX_DEPTH, n_estimators=NUM_TREES)
rforest = rforest.fit(X_train, y_train)

# here are some examples, printed out:
print("Random-forest predictions:\n")
predicted_labels = rforest.predict(X_test)
answer_labels = answers  # note that we're "cheating" here!

#
# formatted printing again (see above for reference link)
#
s = "{0:<11} | {1:<11}".format("Predicted","Answer")
#  arg0: left-aligned, 11 spaces, string, arg1: ditto
print(s)
s = "{0:<11} | {1:<11}".format("-------","-------")
print(s)
# the table...
for p, a in zip( predicted_labels, answer_labels ):
    s = "{0:<11} | {1:<11}".format(p,a)
    print(s)

#
# feature importances
#

s = "{0:<11} | {1:<11}".format("Pixel #","Importance")
#  arg0: left-aligned, 11 spaces, string, arg1: ditto
print(s)
s = "{0:<11} | {1:<11}".format("-------","-------")
print(s)
# the table...
for p, a in zip( feature_names, rforest.feature_importances_):
    s = "{0:<11} | {1:<11}".format(p,a)
    print(s)

# print("\nrforest.feature_importances_ are\n      ", rforest.feature_importances_)
# print("Order:", feature_names[0:64])

# The individual trees are in  rforest.estimators_  [a list of decision trees!]


""" Our Decision Tree and Random Forest did alright when predicting the digit.
The Random Forest predictions were however more accurate than the Decision Tree,
which makes sense since a Random Forest is a collection of multiple Decision
Trees, thus making it more precise. Both of them however got over 80% correct
for all tests (over the course of multiple trials).

I believe that the Random Forest definitely did significantly better than the kNN algorithm,
achieving a high score of 95% (only one incorrect). The Decision Tree, however, was about
the same if not slightly better than kNN neighbours.
"""

""" Values:

Pixel #     | Importance 
-------     | -------    
Pixel 0     | 0.0        
Pixel 1     | 0.0017563218140821501
Pixel 2     | 0.021072390055148396
Pixel 3     | 0.009659049362463933
Pixel 4     | 0.008492307729381792
Pixel 5     | 0.020315751701400524
Pixel 6     | 0.0063415330537895075
Pixel 7     | 0.0009395078943938022
Pixel 8     | 4.062466866933737e-05
Pixel 9     | 0.009794796763422917
Pixel 10    | 0.027387560796127072
Pixel 11    | 0.007647568210816518
Pixel 12    | 0.017832110373890285
Pixel 13    | 0.025718854534979397
Pixel 14    | 0.004766273642259458
Pixel 15    | 0.0009158497847195577
Pixel 16    | 9.683349018168212e-05
Pixel 17    | 0.007960969756722752
Pixel 18    | 0.019907346394325842
Pixel 19    | 0.027543665217386496
Pixel 20    | 0.03234886951226492
Pixel 21    | 0.0543512989543749
Pixel 22    | 0.010194343798078152
Pixel 23    | 0.000708276862494938
Pixel 24    | 4.645763501580282e-05
Pixel 25    | 0.012655948794659318
Pixel 26    | 0.0432986665313349
Pixel 27    | 0.022909195023480267
Pixel 28    | 0.032017618551811844
Pixel 29    | 0.0245375960128575
Pixel 30    | 0.02811408331257183
Pixel 31    | 6.352888875370083e-05
Pixel 32    | 0.0        
Pixel 33    | 0.030613640315466588
Pixel 34    | 0.026265141791984577
Pixel 35    | 0.019651990246916634
Pixel 36    | 0.04020870456573499
Pixel 37    | 0.015416057245704058
Pixel 38    | 0.025788298117786365
Pixel 39    | 0.0        
Pixel 40    | 3.458809779976239e-05
Pixel 41    | 0.013011460806622091
Pixel 42    | 0.032823244395607236
Pixel 43    | 0.04156639105491413
Pixel 44    | 0.021135862012729784
Pixel 45    | 0.02435817870331633
Pixel 46    | 0.020232047025602315
Pixel 47    | 0.00010036290575728595
Pixel 48    | 1.616966523244555e-05
Pixel 49    | 0.0019332905243836553
Pixel 50    | 0.01712192752948963
Pixel 51    | 0.020468398191312985
Pixel 52    | 0.01614326272627751
Pixel 53    | 0.023960294240286995
Pixel 54    | 0.025848696262191766
Pixel 55    | 0.0010313871878166816
Pixel 56    | 0.0        
Pixel 57    | 0.0014473384127482733
Pixel 58    | 0.02139556655130322
Pixel 59    | 0.009318061942370606
Pixel 60    | 0.022419655981766852
Pixel 61    | 0.028336819802464438
Pixel 62    | 0.016721096647793844
Pixel 63    | 0.003196867926759436
"""
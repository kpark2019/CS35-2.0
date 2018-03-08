#
# titanic5: modeling the Titanic data with DTs and RFs
#

import numpy as np
import pandas as pd

from sklearn import tree      # for decision trees
from sklearn import ensemble  # for random forests

try: # different imports for different versions of scikit-learn
    from sklearn.model_selection import cross_val_score   # simpler cv this week
except ImportError:
    try:
        from sklearn.cross_validation import cross_val_score
    except:
        print("No cross_val_score!")


#
# The "answers" to the 30 unlabeled passengers:
#
answers = [0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,
            1,0,1,1,1,1,0,0,0,1,1,0,1,0]

#

print("+++ Start of pandas' datahandling +++\n")
# df here is a "dataframe":
df = pd.read_csv('titanic5.csv', header=0)    # read the file w/header row #0
#
# drop columns here
#
df = df.drop(['ticket','name','cabin','fare','home.dest','embarked'], axis=1)  # axis = 1 means column

df.head()                                 # first five lines
df.info()                                 # column details

# One important one is the conversion from string to numeric datatypes!
# You need to define a function, to help out...
def tr_mf(s):
    """ from string to number
    """
    d = { 'male':0, 'female':1 }
    return d[s]

df['sex'] = df['sex'].map(tr_mf)  # apply the function to the column
#
# Saves rows age unknown before dropping
all_data = df.values
# end of conversion to numeric data...
# drop rows with missing data!
df = df.dropna()
#
print("\n+++ End of pandas +++\n")

#

print("+++ Start of numpy/scikit-learn +++\n")
# convert to numpy arrays
X_data_full = df.drop('survived', axis=1).values
y_data_full = df[ 'survived' ].values


# First 20 test rest train

X_test = X_data_full[0:20,:]              # final testing data
X_train = X_data_full[20:,:]              # training data
y_test = y_data_full[0:20]                # final testing outputs/labels (unknown)
y_train = y_data_full[20:]                 # training outputs/labels (known)
feature_names = df.drop('survived', axis=1).columns.values
target_names = ['0','1']

# 10-fold cross-validate
# create cross-validation data
# Iterates through n_neighbors model parametee in order
# determines which one performs best by 10-fold cross-validate

def findBestScore():
    """ Iterates through n_neighbors model parameter,
        between 1 and 20 to determine which one performs best by returning
        maximum testing_avgScore and corresponding k value.
    """
    resultList = []
    BestScore = 0
    # iterate different max_depths 1 to 19
    for max_depth in range(1,20):
        dtree = tree.DecisionTreeClassifier(max_depth=max_depth)
        trainng_score = []
        testing_score = []

        # run 10 different cross-validation
        for index in range(10):

            # split into cross-validation sets.
            cv_data_train, cv_data_test, cv_target_train, cv_target_test = \
                cross_validation.train_test_split(X_train, y_train, test_size=0.1)

            # fit the model using cross-validation data
            dtree = dtree.fit(cv_data_train, cv_target_train)
            dtree.feature_importances_
            trainng_score += [dtree.score(cv_data_train,cv_target_train)]
            testing_score += [dtree.score(cv_data_test,cv_target_test)]

        # Compute average score for traning and testing data
        trainng_avgScore = 1.0 * sum(trainng_score)/len(trainng_score)
        testing_avgScore = 1.0 * sum(testing_score)/len(testing_score)

        # find best score
        if testing_avgScore > BestScore:
            BestScore = testing_avgScore
            best_depth = max_depth
        resultList += [[best_depth, trainng_avgScore, testing_avgScore]]
    print ('The best average score and the corresponding max_depth is: ')
    return BestScore, best_depth


#  Model Decision Tree Graph
def decisionTreeGraph(max_depth):
    """ generate dot file for MDT graph """
    dtree = tree.DecisionTreeClassifier(max_depth=max_depth)

    # full training data is used for the model
    dtree = dtree.fit(X_data_full, y_data_full)
    print("\nCreated and trained a decision tree classifier")

    # write out the dtree to tree.dot
    tree.export_graphviz(dtree, out_file='tree' + str(max_depth) + '.dot',
                            feature_names=feature_names,  filled=True, rotate=False,
                            class_names=target_names, leaves_parallel=True)
    print ('write out tree.dot')


def findRFBestDepth():
    """ findRFBestDepth iterates through the model parameter, max_depth
        between 1 and 20 to determine which one performs best by returning
        the maximum testing_avgScore and the corresponding max_depth value
        when n_estimators is 100.

    """
    resultList = []
    BestScore = 0
    # iterate through different max_depths from 1 to 19
    for max_depth in range(1,20):
        rforest = ensemble.RandomForestClassifier(max_depth=max_depth, n_estimators=100)
        trainng_score = []
        testing_score = []
        # run 10 different cross-validation
        for index in range(10):
            # split into cross-validation sets.
            cv_data_train, cv_data_test, cv_target_train, cv_target_test = \
                cross_validation.train_test_split(X_train, y_train, test_size=0.1)
            # fit model using cross-validation data
            # tune parameters
            rforest = rforest.fit(cv_data_train, cv_target_train)
            trainng_score += [rforest.score(cv_data_train,cv_target_train)]
            testing_score += [rforest.score(cv_data_test,cv_target_test)]
        # Compute average score for traning and testing data
        trainng_avgScore = 1.0 * sum(trainng_score)/len(trainng_score)
        testing_avgScore = 1.0 * sum(testing_score)/len(testing_score)
        # find best score

        if testing_avgScore > BestScore:
            BestScore = testing_avgScore
            best_depth = max_depth
        resultList += [[best_depth, trainng_avgScore, testing_avgScore]]
    print ('best average score and the corresponding max_depth is: ')
    return BestScore, best_depth


def findRFBestN():

    """ findRFBestN iterates through model parameter n_estimators
        between 1 and 200 that are mutiples of 10 to determine which one
        performs best by returning the maximum testing_avgScore and
        corresponding max_depth value when max_depth is 16.
    """
    resultList = []
    BestScore = 0
    nList = [ n for n in range(1,200) if n%10 == 0]
    for n in nList:
        rforest = ensemble.RandomForestClassifier(max_depth=5, n_estimators=n)
        trainng_score = []
        testing_score = []
        # run 10 different cross-validation
        for index in range(10):
            # split cross-validation sets.
            cv_data_train, cv_data_test, cv_target_train, cv_target_test = \
                cross_validation.train_test_split(X_train, y_train, test_size=0.1)
            # fit model using the cross-validation data
            # and tune parameter
            rforest = rforest.fit(cv_data_train, cv_target_train)
            trainng_score += [rforest.score(cv_data_train,cv_target_train)]
            testing_score += [rforest.score(cv_data_test,cv_target_test)]
        # Compute the average score for both traning and testing data
        trainng_avgScore = 1.0 * sum(trainng_score)/len(trainng_score)
        testing_avgScore = 1.0 * sum(testing_score)/len(testing_score)

        # find best score
        if testing_avgScore > BestScore:
            BestScore = testing_avgScore
            best_n = n
        resultList += [[n, trainng_avgScore, testing_avgScore]]
    print ('best average score and the corresponding n_estimator is: ')
    return BestScore, best_n

rforest = ensemble.RandomForestClassifier(max_depth=5, n_estimators=110)

# fit the model using the cross-validation data
rforest = rforest.fit(X_train, y_train)

"""
The average cross-validated test-set accuracy for your best DT model:
    0.83900000000000008，3

The average cross-validated test-set accuracy for your best RF model:
    0.83600000000000008

Feature importances:
    0.20447085  0.532224    0.14179381  0.0545039   0.06700745

A brief summary of what the first two layers of the DT are "asking" about
    a titanic passenger.
    First layer: sex
    Second layer: class and age

"""

# Impute the missing ages
# Imputing


# impute with RFs


# print("RF imputed outputs are")
# print(all_data_imp[:30,3])

"""
RF imputed outputs

[ 28.61872875  28.63456658  28.65385468  28.7512153   28.51688421
  28.61481153  26.55535028  28.67823843  28.67123124  28.60948563
  33.99177592  34.14306998  30.3744952   33.17889396  30.29148392
  29.89082837  30.08769026  34.28713337  29.22173117  14.03788659
  36.51798391  17.54575112  44.39754546  43.0770746   42.30811932
  38.29996219  38.00541655  43.07320461  51.04449032  43.05613767]


"""
#
# now, building from iris5.py and/or digits5.py
#      create DT and RF models on the Titanic dataset!
#      Goal: find feature importances ("explanations")
#      Challenge: can you get over 80% CV accuracy?
#



# !conda update scikit-learn

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier

import numpy as np
import pandas as pd


#
# learn a two-input, two-output classifier
# 
# AND:
# OR:
# XOR: ???
#



# 
# try an iris classifier...
#



print("+++ Start of digits example +++\n")
# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
#df = pd.read_csv('iris.csv', header=0)    # read the iris file
df = pd.read_csv('digits.csv', header=0)  # read the digits file
df.head()                                 # first few lines
df.info()                                 # column details

def transform(s):
    """ from string to number
          setosa -> 0
          versicolor -> 1
          virginica -> 2
          unknown -> -1
    """
    d = { 'unknown':-1, 'setosa':0, 'versicolor':1, 'virginica':2 }
    return d[s]
    
# 
# this applies the function transform to a whole column
#
#df['irisname'] = df['irisname'].map(transform)  # apply the function to the column

print("+++ Converting to numpy arrays... +++")
# Data needs to be in numpy arrays - these next two lines convert to numpy arrays
X_data_complete = df.iloc[:,0:64].values         # iloc == "integer locations" of rows/cols
y_data_complete = df[ '64' ].values       # individually addressable columns (by name)

X_unknown = X_data_complete[:22,:]
y_unknown = y_data_complete[:22]

X_known = X_data_complete[22:,:]
y_known = y_data_complete[22:]

#
# we can scramble the remaining data if we want to (we do)
# 
KNOWN_SIZE = len(y_known)
indices = np.random.permutation(KNOWN_SIZE)  # this scrambles the data each time
X_known = X_known[indices]
y_known = y_known[indices]

#
# from the known data, create training and testing datasets
#
TRAIN_FRACTION = 0.85
#TRAIN_SIZE = int(TRAIN_FRACTION*KNOWN_SIZE)
TEST_SIZE = 22
#TEST_SIZE = KNOWN_SIZE - TRAIN_SIZE   # not really needed, but...
TRAIN_SIZE = KNOWN_SIZE - TEST_SIZE
X_train = X_known[:TRAIN_SIZE]
y_train = y_known[:TRAIN_SIZE]

X_test = X_known[TRAIN_SIZE:]
y_test = y_known[TRAIN_SIZE:]

#
# it's important to keep the input values in the 0-to-1 or -1-to-1 range
#    This is done through the "StandardScaler" in scikit-learn
# 
USE_SCALER = True
if USE_SCALER == True:
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)   # Fit only to the training dataframe
    # now, rescale inputs -- both testing and training
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    X_unknown = scaler.transform(X_unknown)

# scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html 
#
# mlp = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=400, alpha=1e-4,
#                     solver='sgd', verbose=10, tol=1e-4, random_state=1)
mlp = MLPClassifier(hidden_layer_sizes=(20, 20), max_iter=400, alpha=1e-4,
                    solver='sgd', verbose=True, shuffle=True, early_stopping = False, # tol=1e-4, 
                    random_state=None, # reproduceability
                    learning_rate_init=.1, learning_rate = 'adaptive')

print("\n\n++++++++++  TRAINING  +++++++++++++++\n\n")
mlp.fit(X_train, y_train)


print("\n\n++++++++++++  TESTING  +++++++++++++\n\n")
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))

# let's see the coefficients -- the nnet weights!
# CS = [coef.shape for coef in mlp.coefs_]
# print(CS)

# predictions:
predictions = mlp.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print("\nConfusion matrix:")
print(confusion_matrix(y_test,predictions))

print("\nClassification report")
print(classification_report(y_test,predictions))

# unknown data rows...
#
unknown_predictions = mlp.predict(X_unknown)
print("Unknown predictions:")
print("  Correct values:   [0 0 0 1 7 2 3 4 0 1 9 9 5 5 6 5 0 9 8 9 8 4]")
print("  Our predictions: ", unknown_predictions)


if False:
    L = [5.2, 4.1, 1.5, 0.1]
    row = np.array(L)  # makes an array-row
    row = row.reshape(1,4)   # makes an array of array-row
    if USE_SCALER == True:
        row = scaler.transform(row)
    print("\nrow is", row)
    print("mlp.predict_proba(row) == ", mlp.predict_proba(row))

# C = R.reshape(-1,1)  # make a column!

#
# In a short comment at the bottom of your hw7pr2.py file, compare how well the digit-prediction went using NNets, with respect to
# the other ML algorithms we've used:
#     + Nearest neighbors
#     + Decision Trees and Random Forests
#

"""

"""



"""
Also in that comment at the bottom of the hw7pr2.py file,  reflect on which of thoe three approaches:
Nearest neighbors
Decision Trees and Random Forests
Neural Networks (our MLPs)
Would be best at handling incomplete data  of the sort that the first few digits in digits.py show… ."""
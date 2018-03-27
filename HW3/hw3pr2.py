#
# hw3pr2.py 
#
# Person or machine?  The rps-string challenge...
#
# This file should include your code for 
#   + extract_features( rps ),               returning a dictionary of features from an input rps string
#   + score_features( dict_of_features ),    returning a score (or scores) based on that dictionary
#   + read_data( filename="rps.csv" ),       returning the list of datarows in rps.csv
#
# Be sure to include a short description of your algorithm in the triple-quoted string below.
# Also, be sure to include your final scores for each string in the rps.csv file you include,
#   either by writing a new file out or by pasting your results into the existing file
#   And, include your assessment as to whether each string was human-created or machine-created
# 
#

"""
Short description of (1) the features you compute for each rps-string and 
      (2) how you score those features and how those scores relate to "humanness" or "machineness"





"""


# Here's how to machine-generate an rps string.
# You can create your own human-generated ones!

import random
import csv
import os
from io import StringIO
from math import *

def gen_rps_string( num_characters ):
    """ return a uniformly random rps string with num_characters characters """
    result = ''
    for i in range( num_characters ):
        result += random.choice( 'rps' )
    return result

# Here are two example machine-generated strings:
rps_machine1 = gen_rps_string(200)
rps_machine2 = gen_rps_string(200)
# print those, if you like, to see what they are...




from collections import defaultdict

def comparePerc(percents):
    bool = True
    for percent in percents:
        if percent < 0.4 and percent > 0.2:
            bool = False

    return bool
#
# extract_features( rps ):   extracts features from rps into a defaultdict
#
def extract_features( rps ):
    """ We will examine three different features:
    1) Look for a 33-33-33 distribution for r, p, and s
    2) Look for repetitive strings of 5 or more
    3) Look for combinations of r, p, and s that are repeated
    """
    d = defaultdict( float )  # other features are reasonable

    # 1) First let's count the distributions
    # each combination of two letters should result in about 1/9 of the time.

    comb = ['rr', 'rp', 'rs', 'sr', 'sp', 'ss', 'pr', 'pp', 'ps']

    total = []
    for combination in comb:
        numberof = rps.count(combination) / len(rps)
        total.append(abs((1/9) - numberof))

    #print(total)
    scoredis = 0
    for num in total:
        if num > 0.1:
            scoredis += 1

    d['distribution'] = scoredis

    # 2) Repetitive strings of 5 or more
    scoreRep1 = 0
    for i in range(5, int(len(rps) / 2)):   # repeat for different lengths of strings all weighted differently

        repr = 'r' * i   # test string for r
        reps = 's' * i   # test string for s
        repp = 'p' * i   # test string for p
        boolRep = False  # boolean counting whether or not rps holds repeating values

        if repr in rps:     # first check to see if repeating 'r's
            scoreRep1 += i  # if there is, add a weighted score to scoreRep1
        if repp in rps:     # then check to see if repeating 'p's
            scoreRep1 += i  # if there is, add a weighted score to scoreRep1
        if reps in rps:     # then check finally for repeating 's's
            scoreRep1 += i  # if there is, add a weighted score to scoreRep1

    d['rep'] = scoreRep1

    # 3) Repetitive combinations of letters
    rep = 0
    # for loop iterating through different lengths of strings to compare
    for end in range(4, int(len(rps) / 2)):
        splitlist = [rps[i:i + end] for i in range(0, len(rps), end)]
        #print(splitlist)
        # for loop iterating through each item in the splitlist
        for num1 in range(len(splitlist)):
            item = splitlist[num1]
            count = 0
            # for loop comparing item to each consecutive item in splitlist
            for num2 in range(num1 + 1, len(splitlist)):
                item2 = splitlist[num2]
                #print('1:', item, " 2:", item2)
                if item == item2:
                    count += 1
                    #print("True")
                else:
                    #print("False")
                    break
            #print(count)
            rep += count * end
    d["multirep"] = rep

    return d   # return our features... this is unlikely to be very useful, as-is






#
# score_features( dict_of_features ): returns a score based on those features
#
def score_features( dict_of_features ):
    """
    In order to determine the score, I used a simple weighting system for each of the features:
    In most to least weight:
    1) Repeated combinations of characters
    2) Repeated strings of a single character
    3) Even distributions of two letter sequence

    Using this weight, we added up the scores of each feature, and determined a minimum number: 35
    This was determined by comparing known machine generated and human generated strings through brute force testing

    Then, we return a tuple containing two ordered lists: one determining human versus machine, and one displaying each score
    """
    count = 0         # we used this to make sure we had approximately half of the list as human
    humans = []       # humans is the list of decisions
    totals = []       # totals is the list of scores
    for i in range(len(dict_of_features)):  # using the range helped order the list
        #print(i, ":", dict_of_features[str(i)])
        total = dict_of_features[str(i)]['multirep'] + dict_of_features[str(i)]['rep'] + dict_of_features[str(i)]['distribution']  # add up features
        if total > 35:  # minimum amount
            count += 1
            humans.append('h')  # it's a human
        else:
            humans.append('m')  # it's a machine
        totals.append(total)   # always add score
    #print(count)
    #print(humans)
    #print(totals)

    return (humans, totals)  # return a humanness or machineness score

#
# read_data( filename="rps.csv" ):   gets all of the data from "rps.csv"
#
def read_data( filename="rps18.csv" ):
    """
    """
    with open(filename, 'r') as csvfile:
        filereader = csv.reader(csvfile)
        listCSV = dict(filereader)
    # for row in listCSV:
    #     print(', '.join(row))

    #print(len(listCSV.keys()))
    # you'll want to look back at reading a csv file!
    return listCSV


"""
Just a simple csv writer: takes a list of lists => each list is a row
"""
def writeToCSV(path, my_list):
    #print(my_list)

    with open(os.path.join(path, "results.csv"), "w") as f:
        csvfile = StringIO()
        csvwriter = csv.writer(csvfile)
        for l in my_list:
            csvwriter.writerow(l)
        for a in csvfile.getvalue():
            #print(a)
            f.writelines(a)



#
# you'll use these three functions to score each rps string and then
#    determine if it was human-generated or machine-generated 
#    (they're half and half with one mystery string)
#
# Be sure to include your scores and your human/machine decision in the rps.csv file!
#    And include the file in your hw3.zip archive (with the other rows that are already there)
#

def main():
    if 1:
        results = []
        count = 0

        rpsList = read_data()   # rpsList is the list of rps strings
        #print(rpsList)
        everything = {}         # this dictionary will hold all the extracted dictionaries of features
        for key in rpsList.keys():
            #print(key)
            #print(rpsList[key])
            d = extract_features(rpsList[key])   # extract features here
            everything[key] = d                  # store them all in here
            #print(d)
        result = score_features(everything)      # take the everything dictionary and extract scores from it as a tuple
        humans = result[0]                       # human versus machine decision list
        totals = result[1]                       # scores list

        my_list = []                             # this list is the list of rows to write into csv
        for i in range(len(rpsList)):
            my_list.append([i, totals[i], humans[i]])
        writeToCSV('.', my_list)

        #print(my_list)

        #writeToCSV('./', d)



if __name__ == "__main__":
        main()

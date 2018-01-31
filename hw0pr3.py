#
# hw0pr3.py ~ recipe analysis
#
# Name(s):
# Kenneth Park
# Rory Zhao
# Jason Jiang

#
# be sure your file runs from this location, 
# relative to the "recipes" files and directories
#

# OUR FUNCTIONS:

import shutil
import os
from collections import Counter

# clean_digits( s ):    returns only the digits in the input string s
def clean_digits(s):
    justNums = ''
    for i in s:
        try:
            # attempt to convert character i into integer
            num = int(i)
            # if works add to justNums
            justNums += str(num)
        except ValueError:
            # if fail DO NOTHING
            pass

    return justNums

def bigKilo(path):
    AllFiles = list(os.walk(path))
    # print(AllFiles)

    maxKilo = 0
    maxKiloS = ''

    # sort all files in directory "recipes"
    for item in AllFiles:
        folderName, LoD, LoF = item
        for file in LoF:
            f = open(folderName + '/' + file, 'r')
            try:
                contents = f.read()
                listC = contents.split('\n')
                for sub in listC:
                    if 'kilogram' in sub:
                        newsub = clean_digits(sub)
                        if not newsub == '':
                            if int(newsub) > int(maxKilo):
                                maxKilo = newsub
                                splitsub = sub.split(' ')
                                maxKiloS = splitsub[len(splitsub) - 1]
            except UnicodeDecodeError:
                pass

    return (maxKilo, maxKiloS)

def sortSweetSavory(path):
    AllFiles = list(os.walk(path))
    #print(AllFiles)

    vegetarian = []
    nonveg = []
    sweet = []

    # sort all files in directory "recipes"
    for item in AllFiles:
        folderName, LoD, LoF = item
        for file in LoF:
            f = open(folderName + '/' + file, 'r')
            try:
                contents = f.read()
                if not ".py" in file:
                    if "Savory" in contents:
                        check = ["beef", "pork", "chicken"]
                        if any(x in contents for x in check):
                            nonveg.append(folderName + '/' + file)
                        else:
                            vegetarian.append(folderName + '/' + file)
                    elif "Sweet" in contents:
                        sweet.append(folderName + '/' + file)
            except UnicodeDecodeError:
                pass

    #print(vegetarian)
    #print(nonveg)
    #print(sweet)

    os.mkdir(path + '/Sweet')
    os.mkdir(path + '/Savory')
    os.mkdir(path + '/Savory/Vegetarian')

    for f in sweet:
        destpart = f.split('/')
        shutil.copyfile(f, path + '/Sweet/' + destpart[len(destpart) - 1])
    for f in vegetarian:
        destpart = f.split('/')
        shutil.copyfile(f, path + '/Savory/Vegetarian/' + destpart[len(destpart) - 1])
    for f in nonveg:
        destpart = f.split('/')
        shutil.copyfile(f, path + '/Savory/' + destpart[len(destpart) - 1])

    return True

def metricCount(path):
    AllFiles = list(os.walk(path))
    # print(AllFiles)

    listM = []
    # sort all files in directory "recipes"
    for item in AllFiles:
        folderName, LoD, LoF = item
        for file in LoF:
            #print(file)
            f = open(folderName + '/' + file, 'r')
            try:
                contents = f.read()
                # narrow down string area
                try:
                    i1 = contents.index("Ingredients")
                    i2 = contents.index("Instructions")
                    contents = contents[i1:i2]
                    # create list of each line
                    listC = contents.split('\n')
                    for sub in listC:
                        try:
                            #print(sub)
                            splitsub = sub.split(' ')
                            int(splitsub[0])
                            listM.append(splitsub[1])
                        except ValueError:
                            pass
                except ValueError:
                    pass
            except UnicodeDecodeError:
                pass
    dict = {}
    dict = Counter(listM)
    return dict

def underHour(path):
    AllFiles = list(os.walk(path))
    # print(AllFiles)

    underHourL = []

    # sort all files in directory "recipes"
    for item in AllFiles:
        folderName, LoD, LoF = item
        for file in LoF:
            f = open(folderName + '/' + file, 'r')
            try:
                contents = f.read()
                try:
                    # create list of each line
                    listC = contents.split('\n')
                    test = listC[-2].split(' ')
                    if not test[-3] == "hours":
                        if int(test[-2]) <= 60:
                            underHourL.append(folderName + '/' + file)
                except ValueError:
                    pass
            except UnicodeDecodeError:
                pass

    os.mkdir(path + '/Cook Under an Hour')
    for f in underHourL:
        destpart = f.split('/')
        shutil.copyfile(f, path + '/Cook Under an Hour/' + destpart[-1])

def main():
    print("Start of Main:\n\n\n")

    if 1:
        print("Write functions to organize the files into a directory structure:")
        print(sortSweetSavory('.'))
        print('\n\n\n')

    if 1:
        print("Across all recipes, which recipe calls for the most kilograms of one ingredient?")
        print("What is that ingredient and how much does the recipe call for?")
        result = bigKilo('.')
        print("Largest amount of Kilograms used:", result[0])
        print("Ingredient with Largest Kilo:", result[1])
        print("\n\n\n")

    if 1:
        print("Across all recipes, what different metrics are used?")
        result = metricCount('.')
        #print(result)
        print("Number of Different Metrics:", len(result))
        print("List of Metrics:")
        str = ""
        for i in result.keys():
            str += i +" "
        str = str.split(' ')
        str.remove('')
        print(str)
        print("\n\n\n")

    if 1:
        print("Across all recipes, what is the most used metric?")
        result = metricCount('.')
        maxTuple = ("", 0)
        for key in result.keys():
            if result[key] > maxTuple[1]:
                maxTuple = (key, result[key])
        print(maxTuple[0], "is the most used.")
        print("Used:", maxTuple[1], "times.")
        print("\n\n\n")

    if 1:
        print("Make a new folder for recipes that take under an hour to cook.")
        underHour('.')
    print("End of Main")

# This conditional will run main() when this file is executed:
#
if __name__ == "__main__":
    main()

# Author: Kenneth Park

#
# hw0pr1b.py
#

import os
import os.path
from collections import Counter

# Example 1: How many top-level directories are there in the inclass folder
#
def find_dirs():
    """ returns the number of directories in the "." folder,
        which is the "inclass folder"
    """
    path = "."
    # get ALL contents
    ListOfContents = os.listdir( path )
    #print("Contents of", path, ":")
    #print(ListOfContents)

    # check for directories
    ListOfDirectories = [] # start empty...
    for item in ListOfContents:
        newpath = path + "/" + item  # create path name: ./item
        if os.path.isdir( newpath ):
            #print("Found a directory:", newpath)
            ListOfDirectories.append( item ) # add to our list!

    # yay!
    return ListOfDirectories




# Example 1: How many top-level directories are there in the inclass folder
#
def find_dirs1(path):
    """ returns the number of directories in the path folder,
        Note how close this is to the above!
    """
    # get ALL contents
    ListOfContents = os.listdir( path )
    #print("Contents of", path, ":")
    #print(ListOfContents)

    # check for directories
    ListOfDirectories = [] # start empty...
    for item in ListOfContents:
        newpath = path + "/" + item  # create path name: ./item
        if os.path.isdir( newpath ):
            #print("Found a directory:", newpath)
            ListOfDirectories.append( item ) # add to our list!

    # yay!
    return ListOfDirectories\

def find_dirs2(path):
    """ returns the number of directories in the path folder,
        Note how close this is to the above!
    """
    # get ALL contents
    ListOfContents = os.listdir( path )
    #print("Contents of", path, ":")
    #print(ListOfContents)

    # check for directories
    ListOfDirectories = [] # start empty...
    for item in ListOfContents:
        newpath = path + "/" + item  # create path name: ./item
        if os.path.isdir( newpath ):
            #print("Found a directory:", newpath)
            ListOfDirectories.append( item ) # add to our list!

    # yay!
    return ListOfDirectories

#_____________________MY CODE___________________________________

# ++ The challenges:  Create and test as many of these five functions as you can.
#
# These are the lab challenges:

# How many top level files are there?
def find_files():
    # set path to current
    path = "."
    # make a list of everything in the top level
    everything = os.listdir(path)
    #print("Contents of", path, ":")
    #print(everything)

    # empty list for files we find
    ListOfFiles = []

    for item in everything:
        buildpath = path + "/" + item
        # if it's not a directory add to the list
        if os.path.isfile(buildpath):
            #print("Found a file: " + buildpath)
            ListOfFiles.append(item)

    return ListOfFiles

def find_files1(path):
    # make a list of everything in the top level
    everything = os.listdir(path)
    #print("Contents of", path, ":")
    #print(everything)

    # empty list for files we find
    ListOfFiles = []

    for item in everything:
        buildpath = path + "/" + item
        # if it's not a directory add to the list
        if os.path.isfile(buildpath):
            #print("Found a file: " + buildpath)
            ListOfFiles.append(item)

    return ListOfFiles

def find_files2(path):
    # make a list of everything in the top level
    everything = os.listdir(path)
    #print("Contents of", path, ":")
    #print(everything)

    # empty list for files we find
    ListOfFiles = []

    for item in everything:
        buildpath = path + "/" + item
        # if it's not a directory add to the list
        if os.path.isfile(buildpath):
            #print("Found a file: " + buildpath)
            ListOfFiles.append(item)

    return ListOfFiles


def most_files():
    # Identify path as current
    path = '.'
    # use recursive to compare the number of files in each sub-directory
    return r_most_files(path, path)

#recursive supplemental for finding most_files
# most is the largest number of files found
# mostpath is the path where the most was found
# path is the current path we are looking through
def r_most_files(mostpath, path):
    # Find a list of sub-directories
    allDir = find_dirs2(path)
    # find out how many files are in the top-level
    most = len(find_files2(mostpath))
    curr = len(find_files2(path))
    # if the number of files in the current directory is more than the last biggest,
    # replace it as the largest number of files
    if(most < curr):
        mostpath = path
    # if there are no more sub-directories, return the values it currently has
    if len(allDir) == 0:
        return mostpath
    # otherwise go through the sub-directories recursively
    for dir in allDir:
        newpath = path + '/' + dir
        if(len(find_files2(r_most_files(mostpath, newpath))) > len(find_files2(mostpath))):
            mostpath = r_most_files(mostpath, newpath)

    return mostpath

def total_files():
    # Identify path
    path = '.'
    # use recursive to add up total number of files
    return r_total_files(0, path)

def r_total_files(total, path):
    # Find a list of sub-directories
    allDir = find_dirs2(path)
    # find out how many files are in the top-level and add it to the total
    #print(path,":", len(find_files2(path)))
    #print(find_files2(path), "\n")
    total += len(find_files2(path))
    # if there are no more sub-directories, return the values it currently has
    if len(allDir) == 0:
        return total
    # otherwise go through the sub-directories recursively
    for dir in allDir:
        newpath = path + '/' + dir
        total = r_total_files(total, newpath)

    return total

def file_name(key):
    # set path
    path = '.'
    # recursive search
    count = 0
    nameList = []
    return r_file_name(key, nameList, count, path)

def r_file_name(key, nameList, count, path):
    # Find a list of sub-directories
    allDir = find_dirs2(path)
    # find out how many files are in the top-level and add it to the total
    #print(path, ":", len(find_files2(path)))
    listFiles = find_files2(path)

    # parse through file list and see if "dog" is in the name
    for name in listFiles:
        if key in name:
            count += 1
            nameList.append(name)

    # if there are no more sub-directories, return the values it currently has
    if len(allDir) == 0:
        return (nameList, count)
    # otherwise go through the sub-directories recursively
    for dir in allDir:
        newpath = path + '/' + dir
        tempList = r_file_name(key, nameList, count, newpath)
        nameList = tempList[0]
        count = tempList[1]

    return (nameList, count)

def check(filename, key):
    # set the boolean to false for now
    instanceFound = False

    # open the filename as a file
    #print("file:", filename)
    try:
        datafile = open(filename, 'r')
        # check every line for the key
        try:
            for line in datafile:
                if key in line:
                  instanceFound = True
                  break
        except UnicodeDecodeError:
            #print("UnicodeDecodeError")
            pass

    except FileNotFoundError:
        #print('FileNotFoundError')
        pass

    return instanceFound

def check_in_file(key):
    # set current path
    path = '.'
    # recursively search
    list = []
    return r_check_in_file(key, path, 0, list)

def r_check_in_file(key, path, count, list):
    # Find a list of sub-directories
    allDir = find_dirs2(path)
    # Get a list of files
    fileList = find_files2(path)
    # check each file in the list for the key
    for file in fileList:
        for word in key:
            if check(path + '/' + file, word):
                count += 1
                list.append(file)
                break
    # if there are no more sub-directories, return the values it currently has
    if len(allDir) == 0:
        return (count, list)
    # otherwise go through the sub-directories recursively
    for dir in allDir:
        newpath = path + '/' + dir
        answer = r_check_in_file(key, newpath, count, list)
        count = answer[0]
        list = answer[1]

    return (count, list)

def check_in_file_num():
    key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return check_in_file(key)

def record_file_type():
    # set path
    path = '.'
    # recursive search
    nameList = []
    nameList = r_record_file_type(nameList, path)
    return Counter(nameList)

def r_record_file_type(nameList, path):
    # Find a list of sub-directories
    allDir = find_dirs2(path)
    # find out how many files are in the top-level and add it to the total
    # print(path, ":", len(find_files2(path)))
    listFiles = find_files2(path)

    # parse through file list and split file names by period
    for name in listFiles:
        if "." in name:
            fileNameSplit = name.split(".")
            nameList.append("." + fileNameSplit[len(fileNameSplit) - 1])

    # if there are no more sub-directories, return the values it currently has
    if len(allDir) == 0:
        return nameList
    # otherwise go through the sub-directories recursively
    for dir in allDir:
        newpath = path + '/' + dir
        nameList = r_record_file_type(nameList, newpath)

    return nameList

def s_record_file_type(list):
    nameList = []
    for name in list:
        if "." in name:
            fileNameSplit = name.split(".")
            nameList.append("." + fileNameSplit[len(fileNameSplit) - 1])

    return Counter(nameList)

def k_folderSearch():
    path = "."
    return recursiveFolderSearch(path)

def recursiveFolderSearch(path):
    newpath = ''
    listDir2 = os.listdir(path)
    #print(listDir2)
    for file in listDir2:
        newpath = path + '/' + file
        if os.path.isdir(newpath):
            # print("Looking through:", file)
            # print(file == "Downloads")
            # print(newpath)
            if file == "Downloads":
                #print (True)
                return newpath
            newpath = recursiveFolderSearch(newpath)
    return newpath


# An example main() function - to keep everything organized!
#
def main():
    """ main function for organizing -- and printing -- everything """

    # sign on
    print("\n\nStart of main()\n\n")

    # testing find_dirs
    # result = find_dirs()
    # print("QUESTION: How many top-level _files_ are there in the inclass folder?")
    # print("There are", result, "files in the 'inclass' folder.")
    # print("\n\n\n")

    # # testing find_dirs1
    # result = find_dirs1('.')
    # print("find_dirs1('.') returns", result)
    # print("\n\n\n")

    # # testing find_dirs1 for another dir...
    # result = find_dirs1('./hp')
    # print("find_dirs1('./hp') returns", result)
    # print("\n\n\n")

    # testing find_files
    result = find_files()
    print("QUESTION: How many top-level _files_ are there in the inclass folder?")
    print("There are", len(result), "files in the 'inclass' folder.")
    print("\n\n\n")

    # testing find_files1
    result = find_files1('./inclass/phone_files/00')
    print("QUESTION: How many top-level _files_ are there in the ./phone_files/00 folder?")
    print("There are", len(result), "files in the './phone_files/00' folder.")
    print("\n\n\n")

    # testing most_files
    result = most_files()
    print("QUESTION: Which top-level directory itself contains the most top-level _files_?")
    print("Directory with most files:", result)
    print("Number of files:", len(find_files2(result)))
    print("\n\n\n")

    # testing total_files
    result = total_files()
    print("QUESTION: How many files are there (total) in the whole directory tree?")
    print("Total number of files:", result)
    print("\n\n\n")

    # testing file_name with 'dog'
    result = file_name('dog')
    print("QUESTION: How many filenames contain the string “dog”?")
    print("Number of files with 'dog' in the name:", result[1])
    print("List of files with 'dog' in the name:")
    print(result[0])
    print("\n\n\n")


    # testing file_name with 'recipe'
    result = file_name('recipe')
    print("QUESTION: How many filenames contain the string “recipe”?")
    print("Number of files with 'recipe' in the name:", result[1])
    print("List of files with 'recipe' in the name:")
    print(result[0])
    print("\n\n\n")

    # testing check_in_file
    key = ['dog']
    result = check_in_file(key)
    print("QUESTION: How many files contain the string “dog” (inside the file contents)?")
    print("Number of files with '%s' in the file:" % key[0], result[0])
    print("List of files with '%s' in the file:" % key[0])
    print(result[1])
    print("\n\n\n")

    # testing check_in_file_num
    result = check_in_file_num()
    print("QUESTION: How many files have numbers somewhere in them (in their contents)?")
    print("Number of files with a number in the file:", result[0])
    print("List of files with a number in the file:")
    print(result[1])
    print("\n\n\n")

    result = record_file_type()
    print("QUESTION: How many .txt files are there?")
    print("Number of '.txt' files:", result[".txt"])
    print("\n\n\n")

    print("QUESTION: What types of files exist in the whole tree?")
    print("There are", len(result), "different types of files.")
    print("Types of files:")
    print(result.keys())
    print("\n\n\n")

    print("QUESTION: How many of each type of file are there?")
    print(result)
    print("\n\n\n")

    print("QUESTION: What are all the TYPES of files that contain the word dog (in their contents)?")
    key = ['dog']
    temp = check_in_file(key)
    result = s_record_file_type(temp[1])
    print("Types of files:")
    print(result.keys())
    print("\n\n\n")

    print("QUESTION: Where is the Downloads directory?")
    result = k_folderSearch()
    print("Path of Downloads folder:", result)
    print("\n\n\n")

    print("QUESTION: How many files are there (total) in the Downloads directory?")
    print("Files in Downloads:", find_files2(result))
    print("Number of files in Downloads:", len(find_files2(result)))
    print("\n\n\n")

    # sign off
    print("\n\nEnd of main()\n\n")

# This conditional will run main() when this file is executed:
#
if __name__ == "__main__":
    main()

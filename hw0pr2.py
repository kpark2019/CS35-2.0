#
# hw0pr2.py ~ phonebook analysis
#
# Name(s): Jason Jiang, Kenny Parck, Rory Zhao
#

#
# be sure your file runs from this location,
# relative to the "phonebook" directories
#

import os
import os.path
import shutil
import string


def how_many_txt_files(path):
    """ walks a whole directory structure
        and returns how many txt files are in it!

        call it with: how_many_txt_files(".")

        the (v1) (v2) etc. are different versions, to illustrate
        the process of _trying things out_ and _taking small steps_
    """
    # return 42  # just to check that it's working (v1)

    AllFiles = list(os.walk(path))
    # print(AllFiles)    # just to check out what's up (v2)

    #print("AllFiles has length: ", len(AllFiles), "\n")

    countTotal = 0
    for item in AllFiles:
        # print("item is", item, "\n")    (v3)
        foldername, LoDirs, LoFiles = item   # cool!
        #print("In", foldername, "there are", end=" ")

        count = 0
        for filename in LoFiles:
            if filename[-3:] == "txt":
                count += 1
        #print(count, ".txt files")
        countTotal += count
    return countTotal   # this is not _quite_ correct!

def getText(path):
    AllFiles = list(os.walk(path))
    paths = []
    for item in AllFiles:
        foldername, LoDirs, LoFiles = item
        for filename in LoFiles:
            if filename[-3:] == "txt":
                paths.append(foldername+"\\"+filename)
    return paths

def max_depth(path, depth=0):
    if not os.path.isdir(path):
        return depth
    maxdepth = depth
    for entry in os.listdir(path):
        fullpath = os.path.join(path,entry)
        maxdepth = max(maxdepth,max_depth(fullpath, depth+1))

    return maxdepth

def deepest_directory_path(path):
    AllFiles = list(os.walk(path))
    pathways = []
    for item in AllFiles:
        pathways.append(item[0])
    maxSlashes = 0
    deepestPath = ''
    for item in pathways:
        numSlashes = 0
        for letter in item:
            if letter == '\\':
                numSlashes += 1
        if numSlashes > maxSlashes:
            maxSlashes = numSlashes
            deepestPath = item
    return deepestPath

def clean_digits(s):
    result = ""
    for i in range(len(s)):
        if s[i].isdigit():
            result += s[i]
    return result

def numbers_contain_ten_digits(path):
    paths = getText(path)
    num_ten_digits = []

    for p in paths:
        f = open(p,'r')
        contents = f.read()
        number = clean_digits(contents)
        if len(number) == 10:
            num_ten_digits.append(number)
    return num_ten_digits

def ac909(path):
    result = numbers_contain_ten_digits(path)
    number = 0
    for item in result:
        if item[0:3]=='909':
            number += 1
    return number

def clean_word_last(s):
    result = ""
    s = s.lower()
    for i in range(len(s)):
        if s[i] in string.ascii_lowercase+" ":
            result += s[i]
    return result

def find_Davis_last(path):
    paths = getText(path)
    num_Davis_last = 0
    for p in paths:
        f = open(p,'r')
        contents = f.read()
        name = clean_word_last(contents)
        i = 0
        index = 0
        for i in range(len(name)):
            if name[i] == ' ':
                index = i
            i += 1
        if name[index+1:] == 'davis':
            num_Davis_last += 1
    return num_Davis_last

def clean_word_first(s):
    result = ""
    s = s.lower()
    for i in range(len(s)):
        if s[i] in string.ascii_lowercase:
            result += s[i]
    return result

def find_Davis_first(path):
    paths = getText(path)
    num_Davis_first = 0
    for p in paths:
        f = open(p,'r')
        contents = f.read()
        name = clean_word_first(contents)
        if name[0:5] == 'davis':
            num_Davis_first += 1
    return num_Davis_first

def more_than_ten(path):
    paths = getText(path)
    more_than_ten_digits = 0

    for p in paths:
        f = open(p,'r')
        contents = f.read()
        number = clean_digits(contents)
        if len(number) > 10:
            more_than_ten_digits += 1
    return more_than_ten_digits


# Self Questions: 1. Occurance- Count the occurance of each digit across all
#                    text files.
#                 2. Digits- How often 7 number, 8 number etc. phone numbers
#                    appear.
#                 3. Consecutive- Finds how many consecutive numbers in the text
#                    file
def occurance(path):
    """ Count the occurance of each digit across all the text files
    """
    paths = getText(path)
    d = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

    for p in paths:
        f = open(p,'r')
        contents = f.read()
        number = clean_digits(contents)
        for i in number:
            dTemp = {i:d[i]+1}
            d.update(dTemp)
    return d

def digits(path):
    """ Create a dictionary keeping track of the number of digits of each text
        file
    """
    paths = getText(path)
    d = {}

    for p in paths:
        f = open(p,'r')
        contents = f.read()
        number = clean_digits(contents)
        if len(number) in d:
            dTemp = {len(number):d[len(number)]+1}
            d.update(dTemp)
        else:
            dTemp = {len(number):1}
            d.update(dTemp)
    return d

def consecutive(path):
    """ Finding how many consecutive numbers in the phone numbers in the text
        file
    """
    paths = getText(path)
    d = {}

    for p in paths:
        f = open(p,'r')
        contents = f.read()
        number = clean_digits(contents)
        i = 0
        length = len(number)
        for i in range(length):
            numConsec = consecFromBeginning(number[i:])
            if numConsec in d:
                dTemp = {numConsec:d[numConsec]+1}
                d.update(dTemp)
            else:
                dTemp = {numConsec:1}
                d.update(dTemp)
            i += (1+numConsec)
    return d


def consecFromBeginning(number):
    """ Finds the numbers that appear consecutively from the beginning, one
        consecutive, two consecutive etc.
    """
    if len(number)==1:
        return 0
    elif number[1]==number[0]:
        return 1 + consecFromBeginning(number[1:])
    else:
        return 0



def main():
    """ overall function to run all examples """

    print("Start of main()\n")

    num_txt_files = how_many_txt_files(".")
    print("num_txt_files in . is", num_txt_files)

    print("maxdepth in . is", max_depth("."))

    print("deepestPath in . is", deepest_directory_path("."))

    print("num_ten_digits in . is", len(numbers_contain_ten_digits(".")))

    print("area_code909 in . is",  ac909("."))

    print("last_name_davis in . is",  find_Davis_last("."))

    print("first_name_davis in . is", find_Davis_first("."))

    print("more_than_ten_digits in . is", more_than_ten("."))

    print("occurance_each_number in . is", occurance("."))

    print("occurance_length_of_number in . is", digits("."))

    print("consecutive_numbers in . is", consecutive("."))





    print("End of main()\n")


if __name__ == "__main__":
    main()

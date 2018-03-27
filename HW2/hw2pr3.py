#
# starter file for hw1pr3, cs35 spring 2017...
# 

import csv

#
# readcsv is a starting point - it returns the rows from a standard csv file...
#
def readcsv( csv_file_name ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( csv_file_name, newline='' )  # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        all_rows = []                               # we need to read the csv file
        for row in csvrows:                         # into our own Python data structure
            all_rows.append( row )                  # adds only the word to our list

        del csvrows                                  # acknowledge csvrows is gone!
        csvfile.close()                              # and close the file
        return all_rows                              # return the list of lists

    except FileNotFoundError as e:
        print("File not found: ", e)
        return []



#
# write_to_csv shows how to write that format from a list of rows...
#  + try   write_to_csv( [['a', 1 ], ['b', 2]], "smallfile.csv" )
#
def write_to_csv( list_of_rows, filename ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( filename, "w", newline='' )
        filewriter = csv.writer( csvfile, delimiter=",")
        for row in list_of_rows:
            filewriter.writerow( row )
        csvfile.close()

    except:
        print("File", filename, "could not be opened for writing...")




#
# annotate_text_starter
#
#   Shows off how to style portions of an input text
#   This does not actually use the annotations dictionary (but you will...)
#
def annotate_text_starter( text, annotations ):
    """ this is a letter-by-letter (instead of word-by-word)
        text-annotater. It makes the 'z' characters in the input text bright red.
        It also changes the '\n' characters to "<br>"

        It does not use the annotations dictionary (but you'll want to!)
        It is not general (but you'll build a general template engine!)

        try with 
          + text = "Bees that buzz -\nand kids that blow dandelion fuzz..."
    """
    new_html_string = ''
    for c in text:    # letter-by-letter!
        if c == 'z':
            # we use Python's cool "text-formatting" ability...
            new_c = '<span style="color:{0};">{1}</span>'.format("red", c)
        elif c == '\n':  # handle new lines...
            new_c = "<br>"
        else:
            new_c = c

        # add the new character, new_c
        new_html_string += new_c 

    # finished!
    return new_html_string

def annotate_text(text, sub):
    new_html_string = '''<style>
.dropbtn {
    background-color: #4CAF50;
    color: white;
    padding: 16px;
    font-size: 16px;
    border: none;
}

.dropdown {
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f1f1f1;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

.dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown:hover .dropbtn {
    background-color: #3e8e41;
}
</style>
'''
    textlist = text.split(" ")
    for c in textlist:  # word by word
        # clean the string
        ''.join(e for e in c if e.isalnum())
        #print("c = " + c)
        # look through the dictionary of words to sub
        new_c = c
        #print(c)
        for word in sub:
            if word in new_c.lower():
                #print("FOUND:" + c)
                # we use Python's cool "text-formatting" ability...
                new_c = '<div class="dropdown"><span style="color:{0};font-weight:bold">{1}</span><div class="dropdown-content"><a>{2}</a></div></div>'.format("red", c, sub[word])
        if '\n' in c:  # handle new lines...
            new_c = "<br>" + new_c
            #print("new = " + new_c)

        # add the new character, new_c
        new_html_string += " " + new_c

        # finished!
    return new_html_string


def annotate(string, path):
    csvlist = readcsv(path)
    subdict = {}
    for item in csvlist:
        subdict[item[0]] = item[1]
    newStr = annotate_text(string, subdict)
    return newStr

HAMLET_A1S4 = """The king doth wake tonight and takes his rouse, 
Keeps wassail and the swaggering upspring reels, 
And, as he drains his draughts of Rhenish down, 
The kettle-drum and trumpet thus bray out 
The triumph of his pledge."""

#
# this would be read in from a csv file and constructed
#
# Again, we don't give that function (it's the hw!)
HAMLET_SUBS = { "doth":"does", "rouse":"partying",
                "wassail":"drinks",
                "reels":"dances", "rhenish":"wine",
                "bray":"blare", "pledge":"participation"}



#
# You can see the desired output in  hamlet_substitution.html


def main():
    """ running this file as a script """
    print("original:\n\n", HAMLET_A1S4, "\n\n\n")
    output_html = annotate_text(HAMLET_A1S4, HAMLET_SUBS)
    print("output_html is\n\n", output_html)


if __name__ == "__main__":
    main()



# Larger example for testing...


#
# Here are the text and dictionary of substitutions used in hamlet_substitution.html
#
# Note that we don't give away the template engine here (there'd be nothing left!) 
#
# Inspired by
# http://nfs.sparknotes.com/hamlet/page_50.html
#

#
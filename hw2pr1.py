# Author: Kenneth Park

#
# hw2pr1.py - write-your-own-web-engine...
#
# then, improve the page's content and styling!
#


import re
from copy import deepcopy


def apply_headers( OriginalLines ):
    """ should apply headers, h1-h5, as tags
    """
    # loop for all headings: h1-h5
    NewLines =[]
    # for each line,
    for line in OriginalLines:
        if line.startswith("#"): # check to see if the line starts with a "#"
            count = 0 # counter for how many h's
            for letter in line: # now check every letter in the line...
                if letter == "#": # to see if it's a "#"...
                    count += 1  # add to the counter if it is...
                else:   # until you find one that is not "#". Then break out of checking.
                    break
            line = "<h%i>" % count + line[count:] + "</h%i>" % count # put into html format
        NewLines += [line]
    return NewLines

def apply_wordstyling( OriginalLines ):
    """ should apply wordstyling here...
    """
    # loop for the word-stylings: here, ~word~
    NewLines =[]
    for line in OriginalLines:
        # regular expression example!
        line = re.sub(r"~~(.*)~~", r"<s>\1</s>", line)  # smaller (my personal one)
        line = re.sub(r"~(.*)~", r"<i>\1</i>", line) # italicize
        line = re.sub(r"\*(.*)\*", r"<b>\1</b>", line) # bold
        line = re.sub(r"_(.*)_", r"<u>\1</u>", line) # underline
        line = re.sub(r"&&(.*)&&", r'<mark class="rainbow">\1</mark>', line)  # smaller (my personal one)
        # blinking!
        #if "%%" in line:
            #line = "<style> blink { animation-name: example; animation-duration: 0.3s; animation-timing-function: linear; animation-iteration-count: infinite;} @keyframes example { 0% {color: black;} 25% {color: white;} } </style> " + re.sub(r"%%(.*)%%", r"<blink>\1</blink>", line)
        # <a href="url">line</a>
        line = re.sub(r"@(.*)@", r'<a href="\1">\1</a>', line)
        # let's practice some others...!
        # regular expressions:  https://docs.python.org/3.4/library/re.html
        NewLines += [ line ]
    return NewLines
    # Your task: add at least
    #   *bold*
    #   @link@  (extra: use a regular expression to match a link!)
    #   _underscore_
    #   extra-credit!  BLINKING (working!) or strikethrough
    #   remember for many special symbols, you need to "backslash" them...


def listify(OriginalLines):
    """ convert lists beginning with "   +" into HTML lists"""
    NewLines = []
    # loop for lists
    check = 0
    preline = ""
    boolean = False

    for line in OriginalLines:
        if line.startswith("   +"):
            boolean = True
            if check == 0:
                preline = "<ul>\n"
                check = 1
            line = preline + "<li>" + line[4:] + "</li>"
        else:
            if (boolean == True) and (not line.startswith(" ")):
                boolean = False
                line = postline = "</ul>\n" + line
        preline = ""
        NewLines += [ line ]
        # note - this is wrong: your challenge: fix it!
    return NewLines

def addStyle(OriginalLines):
    NewLines = []
    for line in OriginalLines:
        if "<body>" in line:
            # format the body to have rainbow gradient background
            line = re.sub(r"<body>", r'<body id="grad2">', line)
            # begin <style> and also background gradient
            line += "\n<style>\n#grad2 {\nbackground: black;\nbackground: linear-gradient(267deg, #000000, #f93b02, #f97102, #f9f402, #04f902, #02c0f9, #0802f9, #b602f9, #999999);\nbackground-size: 1600% 1600%;\n-webkit-animation: AnimationName 5s ease infinite;\n-moz-animation: AnimationName 5s ease infinite;\nanimation: AnimationName 5s ease infinite;\n}\n"
            # blink image :)
            line += "img {\nanimation: blink 0.2s;\nanimation-iteration-count: infinite;\n}\n"
            # mark black background
            line += "mark {\nbackground-color: black;\n}\n"
            #line += "\n<style>\nbody{\nbackground-color: gradient;\npadding: 0px;\nmargin: 0px;\n}\n#gradient\n{\nwidth: 100%;\nheight: 800px;\npadding: 0px;\nmargin: 0px;\n}\n"
            #line += ".span {\nbackground-color:black\n}\n"
            # rotate image
            line += ".image {\nposition: absolute;\ntop: 25%;\nleft: 50%;\nwidth: 200px;\nheight: 200px;\nanimation:spin 4s linear infinite;\n}\n"
            line += "@-moz-keyframes spin { 100% { -moz-transform: rotate(360deg); } }\n@-webkit-keyframes spin { 100% { -webkit-transform: rotate(360deg); } }\n@keyframes spin { 100% { -webkit-transform: rotate(360deg); transform:rotate(360deg); } }"
            # rainbow header animation
            line += ".rainbow {\n\n-webkit-animation: rainbow 1s infinite; \n-ms-animation: rainbow 1s infinite;\nanimation: rainbow 1s infinite; \n}\n"
            # other animation for gradient background
            line += '@-webkit-keyframes AnimationName {\n0%{background-position:0% 46%}\n50%{background-position:100% 55%}\n100%{background-position:0% 46%}\n}\n'
            line += '@-moz-keyframes AnimationName {\n0%{background-position:0% 46%}\n50%{background-position:100% 55%}\n100%{background-position:0% 46%}\n}\n'
            line += '@keyframes AnimationName { \n0%{background-position:0% 46%}\n50%{background-position:100% 55%}\n100%{background-position:0% 46%}\n}\n'
            line += "@-webkit-keyframes rainbow{\n20%{color: red;}\n40%{color: yellow;}\n60%{color: green;}\n80%{color: blue;}\n100%{color: orange;}\n}\n"
            line += "@-ms-keyframes rainbow{\n20%{color: red;}\n40%{color: yellow;}\n60%{color: green;}\n80%{color: blue;}\n100%{color: orange;}\n}\n"
            line += "@keyframes rainbow{\n20%{color: red;}\n40%{color: yellow;}\n60%{color: green;}\n80%{color: blue;}\n100%{color: orange;}\n}\n"
            line += "@keyframes blink {\n0% {\nopacity: 1;\n}\n49% {\nopacity: 1;\n}\n50% {\nopacity: 0;\n}\n100% {\nopacity: 0;\n}\n}\n"
            line += "</style>\n"
        if "<h1>" in line:
            line = re.sub(r"<h1>", r'<h1 class="rainbow">', line)
        NewLines += [line]
    return NewLines

def main():
    """ handles the conversion from the human-typed file to the HTML output """

    HUMAN_FILENAME = "starter.txt"
    OUTPUT_FILENAME = "starter.html"

    f = open(HUMAN_FILENAME, "r", encoding="latin1")
    contents = f.read()
    f.close()

    print("Original contents were\n", contents, "\n") 

    OriginalLines = contents.split("\n")  # split to create a list of lines 
    NewLines = apply_headers( OriginalLines )
    NewLines = apply_wordstyling(NewLines)
    NewLines = listify(NewLines)
    NewLines = addStyle(NewLines)

    # finally, we join everything with newlines...
    final_html = '\n'.join(NewLines)

    print("\nFinal contents are\n", final_html, "\n")

    f = open(OUTPUT_FILENAME, "w")     # write this out to a file...
    f.write( final_html )
    f.close()
    # then, render in your browser...


if __name__ == "__main__":
    main()



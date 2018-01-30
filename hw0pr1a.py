#
# hw0pr1a.py
#
# An example function
#
def plus1( N ):
    """ returns a number one larger than its input """
    return N+1

# An example loop (just with a printed countdown)
#
import time

def countdown( N ):
    """ counts downward from N to 0 printing only """
    for i in range(N,-1,-1):
        print("i ==", i)
        time.sleep(0.01)

    return    # no return value here!

# ++ The challenges:  Create and test as many of these five functions as you can.
#
# The final three may be helpful later...
#
# times42( s ):      which should print the string s 42 times (on separate lines)
def times42(s):
    string = ''
    for i in range(s):
        string += 's'

    return string

# alien( N ):          should return the string "aliii...iiien" with exactly N "i"s
def alien( N ):
    str1 = "al"
    for i in range(N):
        str1 += 'i'
    return str1 + 'en'

# count_digits( s ):    returns the number of digits in the input string s
def count_digits(s):
    count = 0
    for i in s:
        try:
            # attempt to convert character i into integer
            num = int(i)
            # if works add to count
            count += 1
        except ValueError:
            # if fail DO NOTHING
            pass

    return count

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

# clean_word( s ):    returns an all-lowercase, all-letter version of the input string s
def clean_word(s):
    justNums = ''
    for i in s:
        try:
            # attempt to convert character i into integer
            num = int(i)
            # if works DO NOTHING
        except ValueError:
            # if fail DO NOTHING
            if not(i == " "):
                justNums += i

    return justNums.lower()

# An example main() function - to keep everything organized!
#
def main():
    """ main function for organizing -- and printing -- everything """

    # sign on
    print("\n\nStart of main()\n\n")

    # testing plus1
    # result = plus1( 41 )
    # print("plus1(41) returns", result)

    # testing countdown
    # print("Testing countdown(5):")
    # countdown(5)  # should print things -- with dramatic pauses!

    # testing times42
    print("Testing 'times42(s)':")
    print("s = 10")
    print("result =", times42(10))
    print("s = 30")
    print("result =", times42(30))
    print("\n\n\n")

    # testing alien
    print("Testing 'alien(N)':")
    print("N = 1")
    print("result =", alien(1))
    print("N = 10")
    print("result =", alien(10))
    print("\n\n\n")

    # testing count_digits
    print("Testing 'count_digits(s)'")
    print("s = 'testtesttest'")
    print("Num. of Digits =", count_digits("testtesttest"))
    print("s = words@#12345")
    print("Num. of Digits =", count_digits("words@#12345"))
    print("\n\n\n")

    # testing clean_digits
    print("Testing 'clean_digits(s)'")
    print("s = 12345p")
    print("Cleaned Version =", clean_digits("12345p"))
    print("s = po@345po")
    print("Cleaned Version =", clean_digits("po@345po"))
    print("\n\n\n")

    # testing clean_words
    print("Testing 'clean_words(s)'")
    print("s = 909poi 909stuff")
    print("Cleaned Version =", clean_word("909poi 909stuff"))
    print("s = 1234567890pop")
    print("Cleaned Version =", clean_word("1234567890pop"))
    print("\n\n\n")

    # sign off
    print("\n\nEnd of main()\n\n")



# This conditional will run main() when this file is executed:
#
if __name__ == "__main__":
    main()

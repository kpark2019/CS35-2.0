#
# starting examples for cs35, week1 "Web as Input"
#

import requests
import string
import json

"""
Examples to run for problem 1:

Web scraping, the basic command (Thanks, Prof. Medero!)

#
# basic use of requests:
#
url = "https://www.cs.hmc.edu/~dodds/demo.html"  # try it + source
result = requests.get(url)
text = result.text   # provides the source as a large string...

#
# try it for another site...
#




#
# let's try the Open Google Maps API -- also provides JSON-formatted data
#   See the webpage for the details and allowable use
#
# Try this one by hand - what are its parts?
# http://maps.googleapis.com/maps/api/distancematrix/json?origins=%22Claremont,%20CA%22&destinations=%22Seattle,%20WA%22&mode=%22walking%22
#
# Take a look at the result -- perhaps using this nice site for editing + display:
#
# A nice site for json display and editing:  https://jsoneditoronline.org/
#
#
"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Problem 1
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#
# example of calling the google distance API
#
def google_api_national(Sources, Dests):
    """ Inputs: Sources is a list of starting places
                Dests is a list of ending places

        This function uses Google's distances API to find the distances
             from all Sources to all Dests. 
        It saves the result to distances.json

        Problem: right now it only works with the FIRST of each list!
    """
    print("Start of google_api_national")

    url="http://maps.googleapis.com/maps/api/distancematrix/json"

    if len(Sources) < 1 or len(Dests) < 1:
        #print("Sources and Dests need to be lists of >= 1 city each!")
        return

    start = '|'.join(Sources)
    end = '|'.join(Dests)
    # start = Sources[0]
    # end = Dests[0]
    my_mode="walking"  # walking, biking

    inputs={"origins":start,"destinations":end,"mode":my_mode}

    result = requests.get(url,params=inputs)
    data = result.json()
    #print("data is", data)

    #
    # save this json data to the file named distances.json
    #
    filename_to_save = "distances.json"
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file
    f.close()                                   # and closes the file
    #print("\nFile", filename_to_save, "written.")
    # no need to return anything, since we're better off reading it from file later...
    return

def google_api_intl(Sources, Dests):
    """ Inputs: Sources is a list of starting places
                Dests is a list of ending places

        This function uses Google's distances API to find the distances
             from all Sources to all Dests.
        It saves the result to distances.json

        Problem: right now it only works with the FIRST of each list!
    """
    print("Start of google_api_intl")

    url="http://maps.googleapis.com/maps/api/distancematrix/json"

    if len(Sources) < 1 or len(Dests) < 1:
        #print("Sources and Dests need to be lists of >= 1 city each!")
        return

    start = '|'.join(Sources)
    end = '|'.join(Dests)
    # start = Sources[0]
    # end = Dests[0]
    my_mode="driving"  # walking, biking

    inputs={"origins":start,"destinations":end,"mode":my_mode}

    result = requests.get(url,params=inputs)
    data = result.json()
    #print("data is", data)

    #
    # save this json data to the file named distances.json
    #
    filename_to_save = "distances.json"
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file
    f.close()                                   # and closes the file
    #print("\nFile", filename_to_save, "written.")
    # no need to return anything, since we're better off reading it from file later...
    return


#
# example of handling json data via Python's json dictionary
#
def json_process():
    """ This function reads the json data from "distances.json"

        It should build a formatted table of all pairwise distances.
        _You_ decide how to format that table (better than JSON!)
    """
    filename_to_read = "distances.json"
    f = open( filename_to_read, "r" )
    string_data = f.read()
    JD = json.loads( string_data )  # JD == "json dictionary"
    #print("The unformatted data in", filename_to_read, "is\n\n", JD, "\n")

    #print("Accessing some components:\n")

    # i is each 'elements' in JD['rows']
    count = 0
    for i in JD['rows']:
        #print(JD['rows'][0]['elements'][0]['distance']['text'])
        #print(i)
        # j is each dictionary in 'elements'
        print("From", JD['origin_addresses'][count])
        count2 = 0
        for dict in i['elements']:
            #print(dict)
            try:
                print(" . . . to", JD['destination_addresses'][count2], "==", dict['distance']['text'], "==", dict['duration']['text'])
            except KeyError:
                print(" . . . to", JD['destination_addresses'][count2], "==", "IMPOSSIBLE", "==", "IMPOSSIBLE")
            count2 += 1
        print("\n")
        count += 1

    #row0 = JD['rows'][0]
    #print("row0 is", row0, "\n")

    #cell0 = row0['elements'][0]
    #print("cell0 is", cell0, "\n")

    #distance_as_string = cell0['distance']['text']
    #print("distance_as_string is", distance_as_string, "\n")

    # we may want to continue operating on the whole json dictionary
    # so, we return it:
    return JD




#
# a main function for lab problem 1 (the multicity distance problem)
#
def main():
    """ top-level function for testing problem 1
    """

    Dests = ['Seattle,WA','Miami,FL','Boston,MA']  # ends
    Sources = ['Claremont,CA','Seattle,WA','Philadelphia,PA'] # starts

    Dests2 = ['Pyongyang,NK', 'Vancouver,BC', 'Mexico City,MX']
    Sources2 = ['Claremont,CA', 'Seattle, WA', 'Wonsan,NK']

    if 1:  # do we want to run the API call?
        google_api_national(Sources, Dests)  # get file
    json_process()
    if 1:
        google_api_intl(Sources2, Dests2)
    json_process()



if __name__ == "__main__":
    main()


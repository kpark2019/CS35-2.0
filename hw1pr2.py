#
# starting examples for cs35, week2 "Web as Input"
#

import requests
import string
import json


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Problem 2 starter code
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#
#
#

def apple_api(artist_name):
    """
    """
    ### Use the search url to get an artist's itunes ID
    search_url = "https://itunes.apple.com/search"
    parameters = {"term":artist_name,"entity":"musicArtist","media":"music","limit":200}
    result = requests.get(search_url, params=parameters)
    data = result.json()

    # What we want: data["results"][0]['artistId']

    # save to a local file so we can examine it
    filename_to_save = "appledata.json"
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    #print("\nfile", filename_to_save, "written.")

    for result in data['results']:
        if result['artistName'] == artist_name:
            return result['artistId']

    # Here, you should return the artist id:
    #
    # Note: it's helpful to find the iTunes artistId and return it here
    # (this hasn't been done yet... try it!) 
    # This is probably _not_ the correct answer...


#
# 
#
def apple_api_lookup(artistId, filename_to_save):
    """ 
    Takes an artistId and grabs a full set of that artist's albums.
    "The Beatles"  has an id of 136975
    "Kendrick Lamar"  has an id of 368183298
    "Taylor Swift"  has an id of 159260351

    Then saves the results to the file "appledata_full.json"

    This function is complete, though you'll likely have to modify it
    to write more_productive( , ) ...
    """
    lookup_url = "https://itunes.apple.com/lookup"    
    parameters = {"entity":"album","id":artistId}    
    result = requests.get(lookup_url, params=parameters)
    data = result.json()

    # save to a file to examine it...
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    #print("\nfile", filename_to_save, "written.")

    # we'll leave the processing to another function...
    return



#
#
#
def apple_api_lookup_process(filename_to_read):
    """ example opening and accessing a large appledata_full.json file...
        You'll likely want to do more!
    """
    f = open( filename_to_read, "r" )
    string_data = f.read()
    data = json.loads( string_data )
    #print("the raw json data is\n\n", data, "\n")
    #print(type(data))

    # for live investigation, here's the full data structure
    return data

# more_productive_analysis is a helper function for more_productive
# it utilizes apple_api_lookup_process to produce a dictionary of the data from itunes
# it then finds the resultCount and returns it
def more_productive_analysis(filename):
    # Get the data from the api_lookup_process
    data = apple_api_lookup_process(filename)
    return data['resultCount']

# more_productive finds the artist with more products (results) than the other by first
# accessing all results for each artist
# then using apple's built in resultCount to compare the number of products.
def more_productive(artist1, artist2):
    # We want to get the appleId's for each artist
    id1 = apple_api(artist1) # get appleID for first artist
    id2 = apple_api(artist2) # get appleID for second artist

    # Now we want to get all of the information from both artists
    apple_api_lookup(id1, "fname1.json")
    apple_api_lookup(id2, "fname2.json")

    data1 = more_productive_analysis("fname1.json")
    data2 = more_productive_analysis("fname2.json")

    print(artist1, "has", data1, "hits.")
    print(artist2, "has", data2, "hits.")

    if data1 > data2:
        return artist1 + ' has more hits.'
    elif data1 < data2:
        return artist2 + ' has more hits.'
    else:
        return artist1 + " and " + artist2 + ' have an equal number of hits.'

def most_recent_analysis(filename):
    # Get the data from the api_lookup_process
    data = apple_api_lookup_process(filename)
    return data['results']

def most_recent_iter(data):
    latest = [0, 0, 0]
    for itemList in data:
        try:
            date = itemList['releaseDate']
            date = date[0:9]
            #print(date) to test if date output worked correctly
            date = date.split("-")
            for i in range(len(date)):
                if int(date[i]) > int(latest[i]):
                    latest = date
                    break
            #print(latest)
        except KeyError:
            pass

    return latest

def most_recent(artist1, artist2):
    # We want to get the appleId's for each artist
    id1 = apple_api(artist1)  # get appleID for first artist
    id2 = apple_api(artist2)  # get appleID for second artist

    # Now we want to get all of the information from both artists
    apple_api_lookup(id1, "artist1.json")
    apple_api_lookup(id2, "artist2.json")

    data1 = most_recent_analysis("artist1.json")
    data2 = most_recent_analysis("artist2.json")

    lateDate1 = most_recent_iter(data1)
    lateDate2 = most_recent_iter(data2)

    for i in range(3):
        if lateDate1[i] > lateDate2[i]:
            return (artist1, lateDate1)
        elif lateDate1[i] < lateDate2[i]:
            return (artist2, lateDate2)
        else:
            pass

#
# main()  for testing problem 2's functions...
#
def main():
    """ a top-level function for testing things... """
    # routine for getting the artistId
    if 0:
        artistId = apple_api("The Beatles") # should return 136975
        #artistId = apple_api("Kendrick Lamar") # should return 368183298
        #artistId = apple_api("Taylor Swift") # should return 159260351
        print("artistId is", artistId)

    if 0:
        apple_api_lookup(368183298, "appledata_full.json")
        data = apple_api_lookup_process("appledata_full.json")

    if 0:
        print(more_productive("Katy Perry", "Steve Perry"))
    # get each one's id
    # get each one's file
    # compare number of albums! Done!
    # then ask two of your own questions

    if 1:
        print("Own Question: Which artist has the most recent releaseDate, Katy Perry or Michael Jackson?")
        result = most_recent("Michael Jackson", "Katy Perry")
        print(result[0], "has a song with the more recent releaseDate on iTunes:", result[1][2], "-", result[1][1], "-", result[1][0])


#
# passing the mic (of control) over to Python here...
#
if __name__ == "__main__":
    main()


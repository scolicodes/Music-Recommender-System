import os
from functools import reduce

# Names of group members: Pragati Kumar, Michael Scoli and Parth Kumar Hirpara

fileName = "musicrecplus.txt"

def readFile():
    """
    Name: Michael
    Purpose: Reads contents from file assigned to fileName and returns contents in the form
    of a string
    """
    file = open(fileName, 'r')
    contents = file.read()
    file.close()
    return contents

def writeFile(string):
    """
    Name: Michael
    Purpose: Overwrites file assigned to fileName with input string; if file doesn't exist,
    it creates it
    """
    file = open(fileName, "w")
    file.write(string)
    file.close()

def loadUsers():
    """
    Name: Michael
    Purpose: Loads file contents in a dictionary and returns the dictionary
    """
    contents = readFile()
    dict = {}

    listOfLines = contents.split("\n")
    for line in listOfLines:
        if ':' in line:
            [name, bands] = line.split(':')
            dict[name] = bands

    return dict

def addNewUserToDict():
    """
    Name: Pragati
    Purpose: Adds the current user and their arist preferences to the dictionary
    """
    enterLoop = True
    preferences = []
    while enterLoop == True:
        currPreference = input("Enter an artist that you like (Enter to finish): ")
        if currPreference != '':
            preferences.append(currPreference)
        else:
            enterLoop = False

    prefDict[userName] = ','.join(preferences)
    formatDictItems()

def standardizeAll(listOfBands):
    """
    Name: Pragati
    Purpose: Helper function for formatDictItems(); it takes in a list
    containing strings elements, capitalizes the first letter and makes the remaining letters lowercase
    for each element
    """
    for i in range(len(listOfBands)):
        listOfBands[i] = listOfBands[i].title()


def formatDictItems():
    """
    Name: Michael
    Purpose: Formats the user-names and artist preferences in the way described in 'The Basics'
    section of the instructions. First it formats the values in prefDict, then it sorts the user names,
    and finally its returns a string containing the formatted data (to be written to the file)
    """
    for key in prefDict.keys():
        bandList = prefDict[key].split(",")
        standardizeAll(bandList)  # standardize band names using "title case"
        bandList = list(set(bandList))   # remove duplicate band names
        bandList.sort()  # sort band names alphabetically
        prefDict[key] = ",".join(bandList)   # set current value to formatted bandList string

    # Copy dict items into list and sort by user-name
    formattedContent = []
    for key in sorted(prefDict):
        formattedContent.append(key + ':' + prefDict[key])

    formattedContent = '\n'.join(formattedContent)
    return formattedContent


def overrideFileWFormattedContents(formattedContents):
    """
    Name: Michael
    Purpose: Takes in the formatted data string output from the formatDictItems() func
    and overwrites the file with formatted content
    """

    writeFile(formattedContents)


def enterPreferences():
    """
    Name: Pragati
    Purpose: Prompts user to enter artist preferences and appends newly entered data to
    the existing value for the user in the dictionary
    """
    enterLoop = True
    preferences = []
    while enterLoop == True:
        currPreference = input("Enter an artist that you like (Enter to finish): ")
        if currPreference != '':
            preferences.append(currPreference)
        else:
            enterLoop = False

    if prefDict[userName] == "":
        prefDict[userName] += ','.join(preferences)
    else:
        prefDict[userName] += ',' + ','.join(preferences)

    formatDictItems()

def getReccs():
    """
    Name: Pragati
    Purpose: Prints the artists who are preferred by the most similar user (whose preferences are not
    the same as or subset of the current user's) to the current user
    and are also not preferred by the current
    """
    maxNumOfMatches = 0
    nameOfUserWithMostMatches = ""
    for key in prefDict:   # loop through userNames
        if key != userName:
            if key == '' or (len(key) > 0 and key[-1] != '$'):
                currNumOfMatches = 0
                isSubset = True
                for artist in prefDict[key].split(','):
                    if artist in prefDict[userName].split(','):
                        currNumOfMatches += 1
                    if artist not in prefDict[userName].split(','):
                        isSubset = False
                if currNumOfMatches > maxNumOfMatches and isSubset == False:
                    maxNumOfMatches = currNumOfMatches
                    nameOfUserWithMostMatches = key

    if maxNumOfMatches == 0:
        print("No recommendations available at this time")
    else:
        for artist in prefDict[nameOfUserWithMostMatches].split(','):
            if artist not in prefDict[userName].split(','):
                print(artist)

def createArtistPopularityDict():
    """
    Name: Parth
    Purpose: Creates a dictionary in which the keys are assigned to each artist present in the
    dictionary and the values represent how many times each artist appears in the users'
    preferences
    """
    artistPopularityDict = {}
    # Populate dictionary with all preferred artists
    for key in prefDict:
        if len(prefDict[key]) > 0:
            for artist in prefDict[key].split(","):
                if artist not in artistPopularityDict:
                    artistPopularityDict[artist] = 0

    # Add 1 score each time artist appears
    for key in prefDict:
        if key == '' or (len(key) > 0 and key[-1] != '$'):
            for artist in prefDict[key].split(","):
                if artist != '':
                    artistPopularityDict[artist] += 1

    return artistPopularityDict

def showMostPopular():
    """
    Name: Parth
    Purpose: Sorts the artist popularity dictionary from most popular artists to least popular
    and print the top 3
    """
    artistPopularityDict = createArtistPopularityDict()
    if artistPopularityDict == {}:
        print('Sorry , no artists found ')
        return

    artistPopularityDict = dict(sorted(artistPopularityDict.items(),
                                       key=lambda x: x[1], reverse=True))
    count = 1
    for i in artistPopularityDict.keys():
        if count == 4:
            return
        print(i)
        count += 1


def howPopular():
    """
    Name: Parth
    Purpose: Returns the highest score/value in artist popularity dictionary
    """
    highestScore = 0
    artistPopularityDict = createArtistPopularityDict()

    for key in artistPopularityDict:
        if artistPopularityDict[key] > highestScore:
            highestScore = artistPopularityDict[key]

    if highestScore == 0:
        print("Sorry, no artists found.")
    else:
        print(highestScore)

def userWMostLikes():
    """
    Name: Pragati
    Purpose: Prints the name(s) of the user(s) who like(s) the most artists
    """
    numOfMostLikes = []
    usersNumOfLikesDict = {}
    for key in prefDict:
        if key == '' or (len(key) > 0 and key[-1] != '$'):
            numOfLikes = 0
            for artist in prefDict[key].split(','):
                numOfLikes += 1
            usersNumOfLikesDict[key] = numOfLikes


    for key in usersNumOfLikesDict:
        numOfMostLikes.append(usersNumOfLikesDict[key])

    numOfMostLikes = reduce(max, numOfMostLikes)
    usersWithMostLikes = list(filter(lambda item: item[1] == numOfMostLikes, usersNumOfLikesDict.items()))
    usersWithMostLikes.sort()

    if numOfMostLikes == 0:
        print("Sorry, no user found")
    else:
        for user in usersWithMostLikes:
            print(user[0])

def deletePreferences():
    """
    Name: Pragati
    Purpose: Displays to the current user his/her preferred artists and removes the selected artist
    from current user's preferences from the dictionary
    """
    artistList = prefDict[userName].split(',')
    if len(artistList) == 1 and artistList[0] == '':
        print("There are no artists to delete")
    else:
        enterLoop = True
        while enterLoop == True:
            print("Choose which artist to delete from your preferences\n"
                  "by selecting the associated number:")
            i = 1
            for artist in artistList:
                print(str(i) + ". " + artist)
                i += 1

            artistToDelete = input()
            if artistToDelete not in map(lambda x: str(x), range(1, len(artistList) + 1)):
                print("Invalid input, please try again")
            else:
                artistToDelete = artistList[int(artistToDelete) - 1]
                artistList.remove(artistToDelete)
                prefDict[userName] = ','.join(artistList)
                enterLoop = False

def showPreferences():
    """
    Name: Pragati
    Purpose: Prints the current user's preferences that are stored in the dictionary
    """
    artistList = prefDict[userName].split(',')

    if artistList == ['']:
        print("You don't have any current preferences")
    else:
        print("Your current preferences are:")
        for artist in artistList:
            print(artist)

def saveAndQuit():
    """
    Name: Parth
    Purpose: Formats current prefDict contents if not formatted already, overwrites file with
    formatted contents, and exits program
    """
    formattedContents = formatDictItems()
    overrideFileWFormattedContents(formattedContents)

def theBasics():
    """
    Name: Michael
    Purpose: Executes above programs that relate to "The Basics" section of the project
    """
    if os.path.exists(fileName) == False:   # if the file doesn't exist, create it
        writeFile('')

    global prefDict
    prefDict = loadUsers()   # prefDict assigned to dictionary containing file contents


    global userName
    userName = input("Enter your name (put a $ symbol after your name if you wish your preferences"
                 " to\nremain private): ")

    if userName not in prefDict:
        addNewUserToDict()

def main():
    """
    Name: Parth
    Purpose: Main function that calls theBasics() function first, then continuously prompts
    user with menu options until user selects save and quit option
    """
    theBasics()

    menuSelection = ""
    while menuSelection != 'q':
        menuSelection = input("Enter a letter to choose an option:\n"
                              "e - Enter preferences\n"
                              "r - Get recommendations\n"
                              "p - Show most popular artists\n"
                              "h - How popular is the most popular\n"
                              "m - Which user has the most likes\n"
                              "d - Delete preferences\n"
                              "s - Show preferences\n"
                              "q - Save and quit\n")

        if menuSelection == 'e':
            enterPreferences()
        elif menuSelection == 'r':
            getReccs()
        elif menuSelection == 'p':
            showMostPopular()
        elif menuSelection == 'h':
            howPopular()
        elif menuSelection == 'm':
            userWMostLikes()
        elif menuSelection == 'd':
            deletePreferences()
        elif menuSelection == 's':
            showPreferences()
    if menuSelection == 'q':
        saveAndQuit()

main()











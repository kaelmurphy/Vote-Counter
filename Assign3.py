# KAEL MURPHY
# CS1026B Assignment3
# Voting thing


def inputfunction(fileInput):
    """This function takes the user input as a parameter and takes each line of data and turns in into a list of
    lists, with each internal list representing one person's vote """

    voteList = []

    with open(fileInput, 'r') as fh:

        # each line that is read is made into its own list,
        # it is then stored into a larger list containing all the sub-lists
        for line in fh:
            # every time there is a comma, the values separated by the commas are put into separate lists

            data = line.strip().split(',')

            voteList.append(data)

    # returns the votelist, which has all the voter data stored in it
    return voteList


def rankingfunction(voteList):
    """this function is responsible for taking the votelist as a parameter and returning both the candidate that came
    in last as well as the candidate that won the election """

    voteDict = {}

    # this for loop takes the first value of each voters list and checks to see whether it is in the dictionary or not
    for i in range(len(voteList)):

        if len(voteList[i]) > 0:
            print(voteList[1][0])
            x = int(voteList[i][0])

            # if the candidate is in the dictionary, their number of votes increases
            if voteList[i][0] in voteDict:

                voteDict[x] += 1

            # if the candidate is not in the dictionary, yet it will be added
            else:
                voteDict[x] = 1
    # this turns takes all the items in the dictionary and stores it sorted, in a list
    sortingList = list(sorted(voteDict.items()))

    # this sets q equal to the first key-value pair in the sorting list
    q = sortingList[0]

    # this for loop sorts the results of the election
    # starting from the lowest candidate id as a tiebreaker for the winner
    for l in range(len(sortingList)):

        # y is set equal to the number of votes a candidate got
        # and is compared with the previous highest number of votes
        y = sortingList[l][1]

        x = q[1]

        if y > x:
            # this continuously updates the value of q so we are always comparing with the highest number of votes seen
            q = sortingList[l]

    # this sorts the list in the opposite direction in order to complete the tiebreaker for the least amount of votes
    sortingList.sort(reverse=True)

    z = sortingList[0]

    # this is the same idea as the for loop above
    for j in range(len(sortingList)):

        y = sortingList[j][1]

        x = z[1]

        if y < x:

            z = sortingList[j]

    # returns the loser of the election on this run-through as z, and the winner as q
    return z, q


def newvotinglist(x, y):
    """this is the function that is responsible for updating the voting list, if there is no winner after a read
    through of the votes, this function will take the votelist and the loser of the election and get rid of all
    occurences of votes for the loser in a new, updated votelist, x is the voting list and y is eliminated """

    finalvotelist = []

    # creates a list that we can put the new votelsit values into,
    # so it will have the same format as the original list but with slightly different values
    for i in range(len(x)):

        finalvotelist.append('')

    # this for loop goes through the imported voterlist and removes all votes for the loser
    for k in range(len(x)):

        newVoteList = []

        # x represents the imported voterlist and y represents the loser of the imported election
        for j in range(len(x)):

            w = x[k]

            if y[0] in w:
                w = x[k].remove(y[0])
            # this creates a new list with all of the values except for the ones that have been removed
            if w != '':

                newVoteList.append(w)

        # the new voterlist after the losers values have been removed
        finalvotelist[k] = newVoteList

    # returning the list for the votes to be counted again and to see if there is now a winner of the election
    return finalvotelist


def winneryet(voteList):
    """this is the function that will determine if one of the cnadidates has passed 50% of the votes, if it does this
    function will return the boolean value true, as well as the sorted lsit of runners up which will all be added to
    the elimination list """

    voteDict = {}

    # this is the same as the for loop seen above that will count all of the first place votes for each candidate
    for j in range(len(voteList)):

        if len(voteList[j]) > 0:
            print(voteList[j][0])
            x = int(voteList[j][0])

            if voteList[j][0] in voteDict:

                voteDict[x] += 1

            else:

                voteDict[x] = 1

    sortingList = list(sorted(voteDict.items()))

    votes = 0

    # this function counts the total number of votes by adding all the recorded first place votes
    for i in range(len(sortingList)):

        votes = votes + sortingList[i][1]

    percentagevotes = []

    # this for loop calculates the percentage of first place votes received for each candidate
    for j in range(len(sortingList)):

        percentagevotes.append((sortingList[j][1]) / votes)

    # this for loop checks to see if any candidate has passed 50% of total first place votes
    for k in range(len(percentagevotes)):

        if percentagevotes[k] > 0.5:

            # this will remove the winner from the list of remaining candidates
            del sortingList[k]

            # this returns the function as true, it also returns a sorted list of the runners-up
            return True, sortingList

    # if no candidate wins this function returns as false and the while loop will continue
    return False


def eliminationfunction(x, y, z):
    """this function is responsible for creating the output of this program, it will take all the eliminated
    candidates, returned from the ranking function, and then add the runners-up in order of their id which is
    returned from the winner yet function as the runnersup list, before finally adding the winner at the end which is
    also returned from the rankingfunction """

    eliminationlist = x

    runnersup = y

    outputstring = 'Elimination order:'

    # this inital for loop will add all of the eliminated candidates to the output line, gathered from ranking function
    for i in range(len(eliminationlist)):

        outputstring = outputstring + ' {},'.format(eliminationlist[i][0])

    # this function will go through the runnersup list and add them onto the end of the outputstring
    for j in range(len(runnersup)):

        outputstring = outputstring + ' {},'.format(runnersup[j])

    # this final line will add the winner of the election onto the end of the output line
    outputstring = outputstring + ' {}'.format(z)

    print(outputstring)


def main():
    """this is the main function, it will ask the user for the file, it will then call the winner yet function to see
    whether there is a winner after the initial votes are counted, if there isn't it will run a while loop,
    that runs until the winner yet funciton returns as true, each time through the wile loop one candidate is
    eliminated and the votes are recounted until there is a winner """

    t = []

    eliminationlist = []

    userInp = input('Enter the name of the file: ')

    x = inputfunction(userInp)

    v = winneryet(x)

    rankingfunction(x)

    # the while loop that runs until there is a winner
    while not v:

        # this sets y equal to the loser of the most recent vote counts
        y = rankingfunction(x)[0]

        # this will remove the loser(y) from the votelist(x) and return a new votelist
        x = (newvotinglist(x, y))

        # this will look through the new votelist and determine whether a candidate has won yet
        v = winneryet(x)

        # this will add the candidate that has been removed on this runthrough to the elimination list
        eliminationlist.append(y)

    # when a candidate wins, the candidates that are still in the election will be stored as e(runnersup)
    e = winneryet(x)[1]

    # this for loop will take the candidate id for the runners up and adds them to a new list
    for i in range(len(e)):

        t.append(e[i][0])

    # this sets the winner of the election, from the rankings function, to the variable winner
    winner = rankingfunction(x)[1][0]

    # this calls the output function that takes the elimination list, runnersup list, and the winner as parameters
    eliminationfunction(eliminationlist, t, winner)


main()

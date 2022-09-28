#junior football

#import libraries

import os

#fill lists with data
teamList = ["Cumnock Juniors","Hurlford United","Irvine Meadow", "Auchinleck Tablot"]
parkList = ["Townhead Park", "Blair Park", "Meadow Park", "Beechwood Park"]
capacityList = [3000, 1500, 5000, 4000]
highestList  = [3000, 1100, 3500, 4000]
lowestList   = [1200, 300, 2000, 2750]
averageList  = []   # empty list

#methods will go here

def clearScreen():
    os.system("cls")
#end clearScreen

#this method will be used to print the contents of the lists
def printLists(teamList, parkList, capacityList, averageList, maxAttendance, maxPosition, minAttendance, minPosition):
    clearScreen()
    if len(teamList)> 0:
        for index in range(len(teamList)):
            print(format(teamList[index],"20"), 
                  format(parkList[index],"20"), 
                  format(capacityList[index], "8"),
                  format(averageList[index], "8"))
        #end for
        print(teamList[maxPosition], "highest average attendance =", averageList[maxPosition])
        print(teamList[minPosition], "lowest average attendance  =", averageList[minPosition])
    #end if
    input("\nPress Enter to Continue")
#end printLists

#find a team
# input a team to find and search through the lists
#comparing each team with the team to find. 
#if found display the team, park and capacity.
def findTeam(teamList, parkList, capacityList):
    clearScreen()
    found = False        # set to True if team found
    position = 0         # hold position of index if team found
    
    team = input("Enter team to find :")
    if len(teamList) > 0:
        for index in range (len(teamList)):
            if team == teamList[index]:
                found = True
                position = index
                break
            #end if
        #end for
    #end if
    if found == True:
        print(teamList[index],"play at", parkList[index],
              "which has a capacity of", capacityList[index])
    else:
        print(team,"not in list")
    #end if
    input("\nPress Enter to Continue")
#end findTeam

#find average and add the averageList
def findAverage(highestList, lowestList):
    clearScreen()
    print("Finding Average")
    if len(highestList)>0:
        for index in range(len(highestList)):
            average = (highestList[index] + lowestList[index])/2
            averageList.append(average)
        #end for
    #end if
    return averageList
    input("\nPress Enter to Continue")
#end findAverage

#find highest average attendance and position in list
#return maxAttendance and maxPosition values back to main program
def findMax(avergeList):
    print("Finding Maximum")
    if len(averageList)>0:
        maxAttendance = averageList[0] # equals first value in list 
        for index in range(len(averageList)):
            if averageList[index]> maxAttendance:
                maxAttendance = averageList[index]
                maxPosition = index
            #end if
        #end for
    #end if
    return maxAttendance, maxPosition
#end find Maximum

#return minAttendance and minPosition values back to main program
def findMin(avergeList):
    print("Finding Maximum")
    if len(averageList)>0:
        minAttendance = averageList[0] # equals first value in list 
        for index in range(len(averageList)):
            if averageList[index]< minAttendance:
                minAttendance = averageList[index]
                minPosition = index
            #end if
        #end for
    #end if
    return minAttendance, minPosition
#end find Minimum

#main program
findTeam(teamList, parkList, capacityList)
averageList = findAverage(highestList, lowestList)
maxAttendance, maxPosition = findMax(averageList)
minAttendance, minPosition = findMin(averageList)
printLists(teamList, parkList, capacityList, averageList, maxAttendance, maxPosition, minAttendance, minPosition)
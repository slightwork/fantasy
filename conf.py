from twelveTeamLeague import managerInfo

#Date Settings
year = 2016
week = "1" # Values - "Preseason", 1, 2, 3 ... 13

firstYear = 2013
yearsCompleted = ['2013','2014','2015']

#League Settings
numberOfTeams = 12
homeFieldAdv = 0.0
# assuming 3 playoff weeks in weeks 14, 15 and 16 of the NFL regular season
# Valid numbers are 5, 6, 7 and 8
# otherwise you wouldnt have 3 weeks worth of playoffs
# room for improvement here - maybe also consider leagues with championship games that span two games
numInPlayoffs = 6
#Starting Spots
numOfQBs = 1
numOfWRs = 2
numOfRBs = 2
numOfTE = 1
numOfFlex = 1
numOfDef = 1
numOfIDP = 0
numOfK = 1

numOfPlayers = numOfQBs + numOfWRs + numOfRBs + numOfTE + numOfFlex + numOfDef + numOfIDP + numOfK

managers = []

for manager in managerInfo:
    managers.append(manager.get('name'))

def getShortenedName(manager):
    "Return nickname for given manager"
    managerIndex = managers.index(manager)
    return managerInfo[managerIndex].get('nickname')

def getLastYearPosition(manager):
    "Return Last Years Final Standings position for given manager"
    managerIndex = managers.index(manager)
    return "Last Year: " + str(managerInfo[managerIndex].get('lastYearPosition'))

def getPicture(manager):
    "Return picture for given manager"
    managerIndex = managers.index(manager)
    return managerInfo[managerIndex].get('picture')

def getClubHouseLink(manager):
    "Return club house link for given manager"
    managerIndex = managers.index(manager)
    return managerInfo[managerIndex].get('clubHouse')

def getNumTeamsInRoundOneOfPlayoffs():
    if numInPlayoffs == 4:
        return 4
    elif numInPlayoffs == 5:
        return 2
    elif numInPlayoffs == 6:
        return 4
    elif numInPlayoffs == 7:
        return 6
    else:
        return 8

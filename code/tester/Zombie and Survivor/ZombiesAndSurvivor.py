import copy
import math
from collections import deque
import glob
from datetime import datetime, date, time

#Global variables
distanceMatrix = []

class Vertex:
    def __init__(self, vertexId):
        self.vertexId = vertexId
    def setAdjacent(self, adjacent):
        self.adjacent = adjacent
    def __gt__(self, other):
        return self.vertexId > other.vertexId
    def __lt__(self, other):
        return self.vertexId < other.vertexId
    def __str__(self):
        return str(self.vertexId)
    def __eq__(self, other):
        return self.vertexId == other.vertexId

class Graph:
    def __init__(self, verticies):
        self.verticies = verticies

class Configuration:
    def __init__(self, zombieVerticies, survivorVertex, numberOfMultipleShortesrtPaths):
        self.zombieVerticies = zombieVerticies
        self.survivorVertex = survivorVertex
        self.numberOfMultipleShortesrtPaths = numberOfMultipleShortesrtPaths

    def AddZombieVertex(vertex):
        zombieVerticies.append(vertex)

def CheckForWin(configuration, previousConfigurations):
    #zombie wins
    for zombieVertex in configuration.zombieVerticies:
        if zombieVertex.vertexId == configuration.survivorVertex.vertexId:
            return -1
    
    #survivor wins
    for prev in previousConfigurations[0:len(previousConfigurations)-1]:
        if prev.zombieVerticies == configuration.zombieVerticies and prev.survivorVertex == configuration.survivorVertex:
            return 1

    #Game has not ended
    return None

def ZombieMove(configuration, previousConfigurations):
    global numberOfMultipleShortesrtPaths

    #Get all move each individual zombie can make
    moveLists=[]
    for z in configuration.zombieVerticies:
        zMoves = []
        distanceToSurvivor  = distanceMatrix[z.vertexId][configuration.survivorVertex.vertexId]
        for a in z.adjacent:
            if distanceMatrix[a.vertexId][configuration.survivorVertex.vertexId] == distanceToSurvivor - 1:
                zMoves.append(a)
        if len(zMoves) > 1:
            configuration.numberOfMultipleShortesrtPaths += 1
        moveLists.append(zMoves)
        

    #Get the list of all possible combinations of moves the zombies can make
    possibleMoves = []
    for i in range(0, len(moveLists)):
        possibleMoves = ProductOfTwoLists(possibleMoves, moveLists[i])

    #Turn each move into a configuration and get the value of that configuration (zombie win(-1), survivor win(1), neither(None))
    #Also add the list of previous configurations
    possibleConfigurations = []
    for move in possibleMoves:
        config = Configuration(move, configuration.survivorVertex, configuration.numberOfMultipleShortesrtPaths)
        val = CheckForWin(config, previousConfigurations)
        prevConfig = previousConfigurations + [config]
        possibleConfigurations.append([config, val, prevConfig])

    #If any configuration results in the zombie winning don't bother calculating the others
    for i in range(0, len(possibleConfigurations)):
        if possibleConfigurations[i][1] == -1:
            return possibleConfigurations[i]

    #For each congifuration of the game that isn't over, continue the game
    for i in range(0, len(possibleConfigurations)):
        if possibleConfigurations[i][1] == None:
            tmp = SurvivorMove(possibleConfigurations[i][0], possibleConfigurations[i][2])
            possibleConfigurations[i][1] = tmp[1]
            possibleConfigurations[i][2] = tmp[2]
    
    #Find the configuration with the lowest value
    min = [[], 2,[]]
    for config in possibleConfigurations:
        if config[1] < min[1]:
            min = config
    return min

def SurvivorMove(configuration, previousConfigurations):
    #Get all moves the survivor can make
    possibleMoves = configuration.survivorVertex.adjacent + [configuration.survivorVertex]

    #Turn each move into a configuration and get the value of that configuration (zombie win(-1), survivor win(1), neither(None))
    possibleConfigurations = []
    for move in possibleMoves:
        config = Configuration(configuration.zombieVerticies, move, configuration.numberOfMultipleShortesrtPaths)
        val = CheckForWin(config, previousConfigurations)
        prevConfig = previousConfigurations + [config]
        possibleConfigurations.append([config, val, prevConfig])

    #If any configuration results in the zombie winning don't bother calculating the others
    for i in range(0, len(possibleConfigurations)):
        if possibleConfigurations[i][1] == 1:
            return possibleConfigurations[i]
        
    #For each congifuration of the game that isn't over, continue the game
    for i in range(0, len(possibleConfigurations)):
        if possibleConfigurations[i][1] == None:
            tmp = ZombieMove(possibleConfigurations[i][0], possibleConfigurations[i][2])
            possibleConfigurations[i][1] = tmp[1]
            possibleConfigurations[i][2] = tmp[2]

    #Find the configuration with the highest value
    max = [[], -2,[]]
    for config in possibleConfigurations:
        if config[1] > max[1]:
            max = config
    
    return max

#Calculates the cross-product of two lists
def ProductOfTwoLists(list1, list2):
    result = []
    if list1 == []:
        for l2 in list2:
            result.append([l2])
    else:
        for l in list1:
            for l2 in list2:
                lcopy = copy.deepcopy(l)
                lcopy.append(l2)
                result.append(lcopy)
    return result

#Similar to product of two lists but for use on lists that are the same
#In the case of this program it is soecifically for zombie starting positions
#This method avoids duplicates as it considers [0,1] the same as [1,0]
def CreateZombieStartingPositions(startingPositions, verticies):
    result = []
    if startingPositions == []:
        for v in verticies:
            result.append([v])
    else:
        for i in range(0,len(startingPositions)):
            for j in range(i,len(verticies)):
                lcopy = copy.deepcopy(startingPositions[i])
                lcopy.append(verticies[j])
                result.append(lcopy)
    return result

#Finds the distance from a source vertex to every other vertex in the graph using breadth-first search
def breadthFirstSearchShortestPath(graph, srcVertexId):
    q = deque();
    visited = [False for x in range(len(graph.verticies))]
    distance = [math.inf for x in range(len(graph.verticies))]
    predecessor = [-1 for x in range(len(graph.verticies))]

    visited[srcVertexId] = True
    distance[srcVertexId] = 0
    q.append(srcVertexId)

    while len(q) != 0:
        u = q.popleft()
        for v in graph.verticies[u].adjacent:
            if visited[v.vertexId] == False:
                visited[v.vertexId] = True
                distance[v.vertexId] = distance[u] + 1
                predecessor[v.vertexId] = u
                q.append(v.vertexId)
    return distance

        
def runGame():
    global distanceMatrix

    #Let the user choose how they want to run their files
    print("1 - Run for all files in the /Graphs subfolder.")
    print("2 - Specify the name of a text file in the /Graphs subfolder.")
    print("3 - Specify a file path for a text file.")
    fileMethod = int(input())
    graphFiles = []
    if fileMethod == 1:
        graphFiles = glob.glob("Graphs/*.txt")
    elif fileMethod == 2:
        textFileName = "Graphs/" + input("Enter the name of the text file (including .txt): \n")
        graphFiles = [textFileName]
    elif fileMethod == 3:
        filePath = input("Specify a file path for a text file: \n")
        graphFiles = [filePath]
    else:
        print("Not a valid input")
        raise Exception("exit")

    
    #Get number of zombies from the user
    numberOfZombies = int(input("How many zombies would you like to test this graph with? "))

    #Let the user choose if they want to find all configurations
    print("1 - Find all possible winning zombie configurations.")
    print("2 - Find only the first winning zombie configuration.")
    configurationMethod = int(input())
    allConfigurations = False
    if configurationMethod == 1:
        allConfigurations = True
    elif configurationMethod == 2:
        allConfigurations = False
    else:
        print("Not a valid input")
        raise Exception("exit")
    
    print("Sit back, this may take a while...")

    
    resFile = open('Results.txt','w')
    
    for filename in graphFiles:
        #print file name so user knows what graph the result is for
        
        #open the file to read
        file=open(filename,'r')

        #create the graph from the text file
        n = int(file.readline())
        verticies = [Vertex(i) for i in range(n)]
        for i in range(0,n):
            line = file.readline().rstrip().split(',')
            verticies[i].setAdjacent([verticies[int(adj)] for adj in line])
        g = Graph(verticies)
        
        file.close()

        #Create and print the distance matrix
        for v in g.verticies:
            distanceMatrix.append(breadthFirstSearchShortestPath(g, v.vertexId))
            
        #Create all the starting positions for the zombies
        possibleZombieStartingPositions = []
        for z in range(0, numberOfZombies):
            possibleZombieStartingPositions = CreateZombieStartingPositions(possibleZombieStartingPositions, g.verticies)
        
        zombieWin = False
        winningZombieStartingConfigurations = []

        numberOfMultipleShortesrtPaths = 0
        #Beging testing zombie starting positions
        startTime = datetime.now()
        for zStart in possibleZombieStartingPositions:
            #Get the possible starting positions for the survivor
            survivorStartOptions = copy.deepcopy(g.verticies)
            
            #Remove the positions that have or are adjacent to zombies from the survivors possible starting positions
            for z in zStart:
                for s in survivorStartOptions:
                    if z == s:
                        survivorStartOptions.remove(s)
                for adj in z.adjacent:
                    for s in survivorStartOptions:
                        if adj == s:
                            survivorStartOptions.remove(adj)


            survivorWon = False
            #Start testing survivor starting positions
            for v in survivorStartOptions:
                #Create the configuration and run the game
                config = Configuration(zStart, v, 0)
                game = ZombieMove(config, [config])
                
                numberOfMultipleShortesrtPaths += game[2][len(game[2])-1].numberOfMultipleShortesrtPaths
                
                #If the survivor won, this zombie starting configuration cannot make the graph a zombie win graph
                #So we move on to the next zombie starting configuration
                if game[1] == 1:
                    survivorWon = True
                    break

            #If the survivor never won a round for this zombie starting configuration then the graph is a zombie win graph
            if survivorWon == False:
                zombieWin = True
                #Save the zombie configuration that won as well as the number of times a zombie had multiple shortest paths
                winningZombieStartingConfigurations.append([zStart, numberOfMultipleShortesrtPaths])

                #If we are not finding all possible winning zombie starting configurations then no need to continue
                if allConfigurations == False:
                    break

        resFile.write("========================\n")
        
        #The zombies won, display the position(s) that lead to them winning
        if zombieWin == True:
            resFile.write(filename + "\n")
            resFile.write("This is a zombie win graph when there is/are " + str(numberOfZombies) + " zombie(s)" + "\n")
            resFile.write("The zombie(s) start on position(s):" + "\n")
            for w in winningZombieStartingConfigurations:
                resFile.write("=================" + "\n")
                for z in w[0]:
                    resFile.write(str(z) + "\n")
                    
                #Display the number of times a zombie had multiple shortesr paths it could take
                resFile.write("The number of times a zombie had multiple shortest paths was: " + str(w[1]) + "\n")
        #The survivor won
        else:
            resFile.write("This is not a zombie win graph when there is/are " + str(numberOfZombies) + " zombie(s)" + "\n")

        #Add the running time to the output
        endTime = datetime.now()
        diff = endTime - startTime
        d = divmod(diff.days * 86400 + diff.seconds, 60)
        resFile.write("Total time was: ")
        resFile.write(str(d[0]) + " Minutes ")
        resFile.write(str(d[1]) + " Seconds")
        resFile.write("\n")
        resFile.write("========================\n")

        #Reset the distance matrix
        distanceMatrix = []
        
    resFile.close()

runGame()

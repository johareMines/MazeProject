import sys
import networkx as nx
from collections import defaultdict

import time

from collections import deque

startTime = time.time()

inputData = set()

readFile = open(sys.argv[1])

inputLine = readFile.readline().split()

startVillage = inputLine[2]
endVillage = inputLine[3]


def putCurrentVillageFront(node, currentVillage, frontOrBack):
    char1, char2, char3, char4 = node

    # Ensure the operation can be conducted
    if currentVillage == char1:
        if frontOrBack == "Front":
            # print("Current already in front: " + str(node))
            return node
        else:
            #Flip
            # print("Flipping (Back), before: " + str(node))
            char2, char1 = char1, char2
            returnFormat = tuple([char1, char2, char3, char4])
            # print("After flip: " + str(returnFormat))
            return returnFormat
    elif currentVillage == char2:
        if frontOrBack == "Front":
            # Flip
            # print("Flipping (Front), before: " + str(node))
            char2, char1 = char1, char2
            returnFormat = tuple([char1, char2, char3, char4])
            # print("After flip: " + str(returnFormat))
            return returnFormat
        else:
            # print("Current already in back: " + str(node))
            return node
    else:
        # print("Current Village is not either village")
        return

G = nx.DiGraph()
inputSet = set()

adjacencyList = defaultdict(list)

# Create set that holds all input data
for line in readFile:
    line = line.strip()

    elements = tuple(line.split())

    inputSet.add(elements)

    # For ex ABBL, dict[b] now holds ABBL - when standing on B, you can reach ABBL
    adjacencyList[elements[1]].append(elements)

    # BABL, dict[a] holds BABL
    reverseElement = putCurrentVillageFront(elements, elements[0], "Back")
    adjacencyList[reverseElement[1]].append(reverseElement)


for key in adjacencyList:
    adjacencyList[key] = sorted(adjacencyList[key])

# Sort so alphabetically higher nodes get put into the processing queue sooner
inputSet = sorted(inputSet)


processingQueue = deque()
startNode = (startVillage, '?', None, None)
endNode = (endVillage, '?', None, None)
G.add_node(startNode)
G.add_node(endNode)

# Add any edges attached to the start node to the processing queue
# print("Considering which lines are edges attached to start node " + str(startNode))
for element in inputSet:
    char1 = element[0]
    char2 = element[1]
    # print(" - Considering " + str(element) + " | " + char1 + " " + char2)

    char1Start = (char1 == startVillage)
    char2Start = (char2 == startVillage)
    if char1Start or char2Start:
        # print("\tStart path found, flipping")

        # Ensure the start point isn't in front (after traveling the first edge, you're not standing on the start point)
        orderedElement = putCurrentVillageFront(element, startVillage, "Back")


        processingQueue.append(orderedElement)
        G.add_node(orderedElement)
        G.add_edge(startNode, orderedElement)
    
# print ("\nStarting queue:")
# print(processingQueue)
# print("\n")

# Loop until empty
while processingQueue:
    currentNode = processingQueue.popleft()

    # Break up into good names
    currentChar1, currentChar2, currentChar3, currentChar4 = currentNode

    # Only check nodes that have the possibility to be adjacent
    nodeAdjacencies = adjacencyList[currentChar1]

    # print("Current node: " + str(currentNode) + " | Adj list: " + str(nodeAdjacencies))

    for element in nodeAdjacencies:

        # Break element into good vars
        char1, char2, char3, char4 = element

        # print(" - Comparing to  " + str(char1) + str(char2) + str(char3) + str(char4))

        # Determine if equal
        flippedElement = putCurrentVillageFront(element, char1, "Back")

        #Check if we're at the end
        if (currentChar1 == endVillage):
            G.add_edge(currentNode, endNode)
            

        # Ensure node can't map to itself
        if (currentNode == element) or (currentNode == flippedElement):
            # print("\tThese nodes are equal")
            continue


        villageNeighbor1 = (currentChar1 == char1)

        # Check if legal path, if so, add edge
        if (currentChar3 == char3) or (currentChar4 == char4):
                
            properElement = element
            # Format it so the new node has the new village first
            if villageNeighbor1:
                # Node is not formatted correctly, flip
                properElement = flippedElement
                    
            # print("Proper Element is: " + str(properElement))

            # Handle differently if node hasn't been seen before
            if properElement in G.nodes:
                # print("\tThis element was already discovered, adding edge (if needed)")
                G.add_edge(currentNode, properElement)
            else:
                # print("\tThis node has been added to the graph and to the processing queue")
                G.add_node(properElement)
                G.add_edge(currentNode, properElement)
                processingQueue.append(properElement)
                if properElement[0] == endVillage:
                    # This node is an endpoint, link it to the end node
                    G.add_edge(properElement, endNode)

                    


    # Current node finished being processed



endTime = time.time()
totalTime = endTime - startTime
# print("Total time taken: {:.2f} seconds".format(totalTime))



if nx.has_path(G, startNode, endNode):
    allPaths = nx.all_shortest_paths(G, startNode, endNode)


    #Setup print format
    pathsOrdered = []
    for path in allPaths:
        pathChars = []
        for letters in path:

            villageChars = letters[:2]
            pathChars.append(villageChars)
        
        pathsOrdered.append(pathChars)

    
    pathsOrdered = sorted(pathsOrdered)
    bestAlphabetPath = pathsOrdered[0]

    printString = ""
    printString = ' '.join(node[0] for node in bestAlphabetPath)
    lastSpaceIndex = printString.rfind(" ")
    if lastSpaceIndex != -1:
        printString = printString[:lastSpaceIndex]
    print(printString)

        
else:
    print("NO PATH")






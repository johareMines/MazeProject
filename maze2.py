import sys
import networkx as nx

from collections import deque

inputData = set()

readFile = open(sys.argv[1])

inputLine = readFile.readline().split()

villageQuantity = inputLine[0]
transitQuantity = inputLine[1]
startVillage = inputLine[2]
endVillage = inputLine[3]


G = nx.Graph()
inputSet = set()

# Create set that holds all input data
for line in readFile:
    line = line.strip()

    elements = tuple(line.split())

    inputSet.add(elements)

# Sort so alphabetically higher nodes get put into the processing queue sooner
inputSet = sorted(inputSet)
for line in inputSet:
    print(line)
print("\n\n")




processingQueue = deque()

# Add any edges attached to the start node to the processing queue
print("Considering which lines are edges attached to start node")
for element in inputSet:
    char1 = element[0]
    char2 = element[1]
    print("Considering " + str(element) + " | " + char1 + " " + char2)

    if char1 == startVillage or char2 == startVillage:
        print("yes")
        processingQueue.append(element)
        G.add_node(element)
    
print ("\n\n")
print(processingQueue)

# print("\n\n")
# for node in G:
#     print (node)
# print("\n\n")

processedNodes = set()

# Loop until empty
while processingQueue:
    currentNode = processingQueue.popleft()

    
    currentChar1 = currentNode[0]
    currentChar2 = currentNode[1]
    currentChar3 = currentNode[2]
    currentChar4 = currentNode[3]
    print("Current node: " + str(currentChar1) + str(currentChar2) + str(currentChar3) + str(currentChar4))

    # Find all nodes that are attached to this node, add them to queue
    for element in inputSet:
        char1 = element[0]
        char2 = element[1]
        char3 = element[2]
        char4 = element[3]
        print(" - Comparing to  " + str(char1) + str(char2) + str(char3) + str(char4))
        if (currentNode == element):
            print("\tThese nodes are equal")
            continue

        # Do I need to check edge color / type for this input?
        villageNeighbor1 = (currentChar1 == char1)
        villageNeighbor2 = (currentChar1 == char2)
        villageNeighbor3 = (currentChar2 == char2)
        villageNeighbor4 = (currentChar2 == char1)

        # print("\t" + str(villageNeighbor1) + " " + str(villageNeighbor2) + " " + str(villageNeighbor3) + " " + str(villageNeighbor4))

        if villageNeighbor1 or villageNeighbor2 or villageNeighbor3 or villageNeighbor4:

            # Check if legal path, if so, add edge
            if (currentChar3 == char3) or (currentChar4 == char4):
                similarChar = ''
                if villageNeighbor1 or villageNeighbor2:
                    similarChar = currentChar1
                elif villageNeighbor3 or villageNeighbor4:
                    similarChar = currentChar2
                

                print("\tThe similar village is: " + str(similarChar))

                # Handle differently if node hasn't been seen before
                


    # Current node finished being processed
    processedNodes.add(currentNode)


    

    

#     #G.add_edge(inputLine[0], inputLine[1], color=inputLine[2], type=inputLine[3])


#     inputLine = readFile.readline()
# add data to graph
    # if inputLine[0] not in G.nodes:
    #     G.add_node(inputLine[0])
    # if inputLine[1] not in G.nodes:
    #     G.add_node(inputLine[1])

#G.add_node(str(inputLine))


# for node in G.nodes:
#     print(node)
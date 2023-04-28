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

print("Inputset after sorting")
for line in inputSet:
    print(line)
print("\n")




def putCurrentVillageFront(node, currentVillage, frontOrBack):
    print(node)
    char1, char2, char3, char4 = node

    # Ensure the operation can be conducted
    if currentVillage == char1:
        if frontOrBack == "Front":
            print("Current already in front: " + str(node))
            return node
        else:
            #Flip
            print("Flipping (Back), before: " + str(node))
            char2, char1 = char1, char2
            returnFormat = tuple([char1, char2, char3, char4])
            print("After flip: " + str(returnFormat))
            return returnFormat
    elif currentVillage == char2:
        if frontOrBack == "Front":
            # Flip
            print("Flipping (Front), before: " + str(node))
            char2, char1 = char1, char2
            returnFormat = tuple([char1, char2, char3, char4])
            print("After flip: " + str(returnFormat))
            return returnFormat
        else:
            print("Current already in back: " + str(node))
            return node
    else:
        print("Current Village is not either village")
        return




processingQueue = deque()

# Add any edges attached to the start node to the processing queue
print("Considering which lines are edges attached to start node")
for element in inputSet:
    char1 = element[0]
    char2 = element[1]
    print(" - Considering " + str(element) + " | " + char1 + " " + char2)

    char1Start = (char1 == startVillage)
    char2Start = (char2 == startVillage)
    if char1Start or char2Start:
        print("\tStart path found, flipping")

        # Ensure the start point isn't in front (after traveling the first edge, you're not standing on the start point)
        orderedElement = putCurrentVillageFront(element, startVillage, "Back")


        processingQueue.append(orderedElement)
        G.add_node(orderedElement)
    
print ("\nStarting queue:")
print(processingQueue)
print("\n")

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
    print("\nCurrent node: " + str(currentChar1) + str(currentChar2) + str(currentChar3) + str(currentChar4))

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
                if element in G.nodes:
                    print("\tThis element was already discovered")
                    G.add_edge(currentNode, element)
                else:
                    print("\tThis node has been added to the graph and to the processing queue")
                    G.add_node(element)
                    G.add_edge(currentNode, element)
                    processingQueue.append(element)


    # Current node finished being processed
    processedNodes.add(currentNode)
    print(str(currentNode)+ " Finished processing. The queue is: " + str(processingQueue))
    print("The Processed Set is: " + str(processedNodes))

print("\n")
processedNodes = sorted(processedNodes)
if processedNodes == inputSet:
    print("All nodes were processed.")

else:

    for node in inputSet:
        if node not in processedNodes:
            print("Node " + str(node) + " not processed.")
        print("\t" + str(node))
    for i in inputSet:
        print("\t" + str(i))

print("\n")
print(G)
print("Nodes: " + str(sorted(G.nodes)))
print("\nEdges: " + str(sorted(G.edges)))


print("\n\nRunning BFS")
# BFS = nx.bfs_edges(G, ('A', 'B', 'B', 'L'))

# print(list(BFS))


# Traverse the graph using BFS
start_node = ('A', 'B', 'B', 'L')

endNodes = set()
endNodes.add(('E', 'B', 'G', 'S'))
endNodes.add(('F', 'G', 'B', 'A'))
queue = [(start_node, [start_node])]
done = False
while queue and not done:
    (node, path) = queue.pop(0)
    for neighbor in G.neighbors(node):
        if neighbor in endNodes:
            print("Path found:", path + [neighbor])
            done = True
            break
        else:
            queue.append((neighbor, path + [neighbor]))
    

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
import sys
import networkx as nx

from collections import deque


transitLayout = dict()


readFile = open(sys.argv[1])

inputLine = readFile.readline().split()

villageQuantity = inputLine[0]
transitQuantity = inputLine[1]
startVillage = inputLine[2]
endVillage = inputLine[3]

# Fill inputLIne with fresh line
G = nx.Graph()
inputLine = readFile.readline().split()
while inputLine:
    # Format
    key = str(inputLine[0]) + str(inputLine[1])
    value = [inputLine[2], inputLine[3]]

    # add data to graph
    if inputLine[0] not in G.nodes:
        G.add_node(inputLine[0])
    if inputLine[1] not in G.nodes:
        G.add_node(inputLine[1])

    G.add_edge(inputLine[0], inputLine[1], color=inputLine[2], type=inputLine[3])

    # add to dictionary
    transitLayout[key] = value

    inputLine = readFile.readline().split()


# for key in transitLayout:
#     print(key, transitLayout[key])



for edge in G.edges(data=True):
    print(edge)


# BFS
queue = deque()
discovered = set()


queue.append((startVillage, None, None, ()))
discovered.add((startVillage, None, None, ()))
print("Start village " + startVillage + " added to queue")

# While loop executes as long as queue isn't empty
while queue:
    currentVillage = queue.popleft()

    if currentVillage == endVillage:
        # Traceback time
        print("good")
        print(currentVillage[3][::-1])
        break


    print("Current: " + str(currentVillage[0]) + str(currentVillage[1]) + str(currentVillage[2]) + str(currentVillage[3]))
    for neighbor in G.neighbors(currentVillage[0]):

        # grabs edge no matter the order
        edge_data = G.get_edge_data(currentVillage[0], neighbor)
        #print(edge_data)
        
        tracebackVar = currentVillage[3]
        if tracebackVar == None:
            tracebackVar = currentVillage[0]
        else:
            tracebackVar = currentVillage[3] + tuple([currentVillage[0]])
        
        neighborTuple = (neighbor, edge_data['color'], edge_data['type'], tracebackVar)

        # create a new tuple holding only the indexes we want to check for in the dict
        neighborTupleTriple = (neighborTuple[0], neighborTuple[1], neighborTuple[2])
        if not any(t[:3] == neighborTupleTriple for t in discovered):
            # Check if this path can be taken given how we arrived
            if(currentVillage[1] == None) :
                print("Neighbor: " + str(neighborTuple[0]) + str(neighborTuple[1]) + str(neighborTuple[2]) + str(neighborTuple[3]) + " valid, added to queue")
                queue.append(neighborTuple)
                discovered.add(neighborTuple)
            elif ((currentVillage[1] == neighborTuple[1]) or (currentVillage[2] == neighborTuple[2])):
                if (neighborTuple[0] != currentVillage[3][-1]):
                    #print(neighborTuple[0] + " || " + currentVillage[3][-1])
                    print("Neighbor: " + str(neighborTuple[0]) + str(neighborTuple[1]) + str(neighborTuple[2]) + str(neighborTuple[3]) + " valid, added to queue")
                    queue.append(neighborTuple)
                    discovered.add(neighborTuple)
            else:
                print("Neighbor: " + str(neighborTuple[0]) + str(neighborTuple[1]) + str(neighborTuple[2]) + str(neighborTuple[3]) + " not valid")
            
print("done") 
            
    

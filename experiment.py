import sys
import networkx as nx


# Define a dictionary to hold the transit layout data
transitLayout = dict()

# Read in the input file and store data in the graph and the transit layout dictionary
with open(sys.argv[1]) as readFile:
    inputLine = readFile.readline().split()

    villageQuantity = inputLine[0]
    transitQuantity = inputLine[1]
    startVillage = inputLine[2]
    endVillage = inputLine[3]

    G = nx.Graph()
    inputLine = readFile.readline().split()
    while inputLine:
        # Format the data
        key = str(inputLine[0]) + str(inputLine[1])
        value = [inputLine[2], inputLine[3]]

        # Add data to the graph
        if inputLine[0] not in G.nodes:
            G.add_node(inputLine[0])
        if inputLine[1] not in G.nodes:
            G.add_node(inputLine[1])

        G.add_edge(inputLine[0], inputLine[1], color=inputLine[2], type=inputLine[3])

        # Add data to the dictionary
        transitLayout[key] = value

        inputLine = readFile.readline().split()


# Perform a BFS on the graph
queue = nx.utils.create_node_dict_bfs(G, startVillage)

# Traceback if a path to the end village is found
if endVillage in queue:
    tracebackVar = ()
    currentVillage = endVillage
    while currentVillage is not None:
        tracebackVar = (currentVillage,) + tracebackVar
        edge_data = G.get_edge_data(currentVillage, queue[currentVillage])
        currentVillage = queue[currentVillage]

    print(tracebackVar)
else:
    print("No path from " + startVillage + " to " + endVillage)

# Close the file
readFile.close()
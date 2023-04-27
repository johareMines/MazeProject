import sys
import networkx as nx

inputData = set()

readFile = open(sys.argv[1])

inputLine = readFile.readline().split()

villageQuantity = inputLine[0]
transitQuantity = inputLine[1]
startVillage = inputLine[2]
endVillage = inputLine[3]

# Fill inputLine with fresh line
G = nx.Graph()
inputLine = readFile.readline().split()
while inputLine:
    #print(inputLine)


    # add data to graph
    # if inputLine[0] not in G.nodes:
    #     G.add_node(inputLine[0])
    # if inputLine[1] not in G.nodes:
    #     G.add_node(inputLine[1])

    G.add_node(str(inputLine))

    #G.add_edge(inputLine[0], inputLine[1], color=inputLine[2], type=inputLine[3])


    inputLine = readFile.readline().split()


for node in G.nodes:
    print(node)
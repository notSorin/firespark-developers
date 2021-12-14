"""
This script demonstrates how to:
    1 - Use the data from firespark_users.json (generated using the script get_all_users.py)
        to create a NetworkX graph with the users who mutually follow each other.
    2 - Apply the Louvain algorithm on the graph to detect its different communities.
    3 - Draw the graph so we can visualize the friendship relations between the users,
        and the different communities they form. (For simplicity and easier visualization,
        nodes will be named according to the user's id, but it is possible to name
        each node using the user's username or their first and last name.)
"""

from community import best_partition
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx
import json

#Read users data from file.
with open("firespark_users.json") as usersFile:
    jsonUsers = json.load(usersFile)

#Create a graph with all the user connections.
G = nx.graph.Graph()

for user in jsonUsers:
    userId = user["userid"]
    following = user["following"]
    followers = user["followers"]

    for followingUser in following:
        #For community detection, we are looking for users who mutually follow each other.
        if followingUser in followers:
            G.add_edge(userId, followingUser)

#Apply Louvain to the graph to determine its communities.
partition = best_partition(G)

#Calculate some values for drawing the graph.
positions = nx.spring_layout(G, scale = 20)
nodesDegrees = dict(G.degree)
nodesSizes = [nodesDegrees[k] * 200 for k in nodesDegrees]
cmap = cm.get_cmap('plasma', max(partition.values()) + 1)
nodesColors = list(partition.values())

#Draw the graph, labels, and edges.
nx.draw_networkx_nodes(G, positions, partition.keys(), node_size = nodesSizes, cmap = cmap, node_color = nodesColors)
nx.draw_networkx_labels(G, positions)
nx.draw_networkx_edges(G, positions)

#Plot the graph.
plt.subplots_adjust(left = 0, right = 1, top = 1, bottom = 0)
plt.show()
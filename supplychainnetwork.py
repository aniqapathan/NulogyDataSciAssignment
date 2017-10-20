import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# initialize graph
G = nx.Graph()

# read in data
df = pd.read_csv('nodesAndLabel.csv')
rel = pd.read_csv('shipAndConsignRelation.csv')

#initialize colours for shippers and consignee
colours = []

# colour coordinate shippers ad consignee
for index, row in df.iterrows():
    if (row['label'] == 'shipper'):
        colours.append('blue')
    else:
        colours.append('green')
    G.add_node(row['name'])

# create edges between shipper and consignee
for index, row in rel.iterrows():
    G.add_edge(row['SHIPPER'], row['CONSIGNEE'], weight=row['total.qty'])

# max and min degree
max_degree = max(G.degree().values())
min_degree = min(G.degree().values())

# density calculation
nodes = len(G.nodes())
edges = len(G.edges())
density = 2.0 * edges / (nodes *(nodes - 1))

# network visualization
pos = nx.spring_layout(G,k=3)
plt.figure(2,figsize=(25,20)) 
nx.draw(G, pos, node_color=colours)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

# print answers
print("Max number of degrees: " , max_degree)
print("Min number of degrees: " , min_degree)
print("Density of network: " , density)
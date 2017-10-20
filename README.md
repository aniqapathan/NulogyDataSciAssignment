# NulogyDataSciAssignment
# Description: The visualization was created by first reading in the data from the two files using the read_csv function in pandas and then reading in the shipper and consignee row by row and making the shipper blue and the consignee green. It would be nice to also label each node with the actual names however that would clutter the visual. Next the edges were created by reading the shipAndConsignRelation.csv document row by row. Next, the position of the nodes were established by playing around with different positions such as random_layout, spring_layout, circular_layout, etc, however, it was found that spring_layout worked best. Next matplotlip was used to change the size of the figures and finally labels were created for the edges because it is important to be able to see clearly how much quanity is moving between the nodes.
# Assumptions: at least one shipper was assigned to atleast one consignee
# Packages used: NetworkX
# Libraries used: Pandas, Matplotlib
# 1. Max Number of Degrees for Network Graph: 13
#    Min Number of Degrees for Network Graph: 1
# 2. Desnity of Network Graph: 0.018386108273748723
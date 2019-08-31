import networkx as nx
import time
import osmnx as ox
import math 
import random
import  shapefile
import arcpy


arcpy.env.workspace = 'D:\RA\Python\mapmatching'

def pointsToShape(file):
    
    csvFile = file
    in_x_field = "Longitude"
    in_y_field = "Latitude"
    out_layer = "Timeframe"
    spatial_reference = 4326

    csvLayer=arcpy.MakeXYEventLayer_management(csvFile,in_x_field,in_y_field,out_layer,spatial_reference)
    # arcpy.CopyFeatures_management(csvLayer,"shapenamesd.shp")
    arcpy.SaveToLayerFile_management(csvLayer, "shapename.shp")
    print("done")



pointsToShape("sample.csv")


# g=ox.graph_from_point((53.3102, -6.2483),distance=7500)
# g=ox.graph_from_bbox(53.4238129951,53.2631172037,-6.1275556119,-6.3926007779)
# # G=nx.Graph()
# ox.save_graph_shapefile(g, filename='network-shape')





# mapping = {}
# counter = 0
# radius=100000
# # for d in g.nodes_iter(data=True):
# for n, d in list(g.nodes(data=True)): #I know this is a round about way to do this, but I might need node attributes later
#         #Generate point location
#         t = random.random() * (math.pi * math.pi)
#         r = radius * math.sqrt(random.random())
#         x = r * math.cos(t)
#         y = r * math.sin(t)
#         co_od=(x,y)
#         nx.set_node_attributes(g, 'loc', {0: co_od})
#         mapping[counter] = co_od
#         counter += 1

# g=nx.relabel_nodes(g, mapping)
# nx.write_shp(g, '/test.shp') 


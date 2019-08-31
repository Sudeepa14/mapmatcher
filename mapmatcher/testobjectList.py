import arcpy

fields = arcpy.ListFields("D:/RA/Python/mapmatching/edges.shp")

for field in fields:
    print("{0} is a type of {1} with a length of {2}"
          .format(field.name, field.type, field.length))
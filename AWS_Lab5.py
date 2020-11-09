#Import os module
import os
#from os.path import abspath
import xml.etree.ElementTree as ET
rawData = ('c:/users/19293/Documents/Git Project/rawdata.xml')
output_file = ('c:/users/19293/Documents/Git Project/output_file.txt')
data_out = open(output_file, "w")
data_in = open(rawData, "r")

#print(str(data_in))
#print(str(data_out))

tree = ET.parse('c:/users/19293/Documents/Git Project/rawdata.xml')
root = tree.getroot()
print(root.tag)

for child in root:
    print(child.tag, child.attrib)
    data_out.write("%s" % child.text)
data_out.close()

"""
for x in range(0, 3):
    print(root[0][x].text)
"""
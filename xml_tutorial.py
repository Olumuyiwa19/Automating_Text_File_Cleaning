#Import os module
import os
#from os.path import abspath
import xml.etree.ElementTree as ET
tree = ET.parse('c:/users/19293/Documents/Git Project/xml_tutorial_data.xml')
root = tree.getroot()
print(root.tag)

for child in root:
    print(child.tag, child.attrib)
    
for x in range(0, 3):
    print(root[0][x].text)

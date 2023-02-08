import xml.etree.ElementTree as ET

# Parse the XML document
tree = ET.parse('model.xml')

# Get the root element
root = tree.getroot()

# Iterate over all the elements in the XML document
for elem in root.iter():
    # Print the tag and text for each element
    print(elem.tag, elem.attrib, elem.text)

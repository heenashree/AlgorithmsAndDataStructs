import xml.etree.cElementTree as ET
import yaml
tree = ET.parse("XML_py.xml")
root = tree.getroot()
print(root.tag, root.attrib)

for child_of_root in root:
   print child_of_root.tag, child_of_root.attrib

f = open('result.yaml')

with open('result.yaml', 'w') as f:
    for elem in tree.iter():
        f.write('%s:%s\n' % (elem.tag, elem.attrib))



#with open('result.yaml', 'w') as tempor:
#    yaml.dump(result, tempor)


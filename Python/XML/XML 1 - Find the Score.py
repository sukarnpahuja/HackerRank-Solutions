import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    score = len(node.attrib)
    for element in node.findall('.//*'):
        score += len(element.attrib)
    return score
    

if __name__ == '__main__':

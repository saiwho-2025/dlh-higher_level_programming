#!/usr/bin/env python3
"""This module handles XML serialization and deserialization"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    try:
        # Create the root element
        root = ET.Element("data")

        # Iterate through dictionary and add as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            # XML only stores strings, so we must cast the value
            child.text = str(value)

        # Create the tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"Error during serialization: {e}")
        return False

def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs it into a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary
        # Note: All values will be returned as strings by default
        return {child.tag: child.text for child in root}

    except FileNotFoundError:
        return None
    except ET.ParseError:
        return None
    except Exception:
        return None

#!/usr/bin/python3
"""
Convert csv to .gpx format for import in OSMAnd.
csv string example: "34.14322, 14.23489\tNAME\tADDRESS\tTYPE"
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom

import csv
import sys
import time


def create_dot(parent, data):
    wpt = ET.SubElement(parent, "wpt", lat=data[0].split(", ")[0], lon=data[0].split(", ")[1])
    ET.SubElement(wpt, "name").text = data[1]
    ET.SubElement(wpt, "desc").text = data[2]
    ET.SubElement(wpt, "type").text = data[3]
    ext = ET.SubElement(wpt, "extensions")
    ET.SubElement(ext, "color").text = "#b4eecc22"


def main(csv_path):
    with open(csv_path) as csvfile:
        dots = csv.reader(csvfile, delimiter='\t')
        root = ET.Element('gpx')
        root.append(ET.Comment(f'Generated with https://github.com/meugr/scripts/blob/master/gpx_generator.py | \
{time.strftime("%Y-%m-%d %H:%M", time.localtime())}'))
        meta = ET.SubElement(root, "metadata")
        ET.SubElement(meta, "name").text = "favorites"

        for dot in dots:
            create_dot(root, dot)

        tree = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
        with open("filename.gpx", "w") as f:
            f.write(tree)


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        print('Error: missing csv file path')

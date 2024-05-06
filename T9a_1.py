import xml.etree.ElementTree as et
import json
import sys


if __name__ == '__main__':

    file = "com.whatsapp_preferences.xml"

    tree = et.parse(file)
    root = tree.getroot()

    dict = {}

    for i in root:
        tag = i.tag
        if tag == "string":
            dict[i.attrib["name"]] = i.text
        elif tag == "int" or tag == "long":
            dict[i.attrib["name"]] = int(i.attrib["value"])
        elif tag == "boolean":
            dict[i.attrib["name"]] = bool(i.attrib["value"])
        else:
            print(f"Type not supported: {tag}", file=sys.stderr)

    print(dict)

    with open(file.replace("xml", "json"), "w") as json_file:
        json.dump(dict, json_file, indent=4)



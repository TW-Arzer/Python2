import xml.etree.ElementTree as et

tree = et.parse("notes.xml")
root = tree.getroot()

notes = [float(i.text) for i in root.findall("note")]
calculs = sum(notes) / len(notes) if len(notes) > 0 else 0.0
print(f"{calculs:.2f}")
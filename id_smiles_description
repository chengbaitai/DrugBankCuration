import xml.etree.ElementTree as ET
print("start loading")
tree = ET.parse("./drugbank.xml")
print("loading...")
drugs = tree.getroot()
print("loading done!")
for drug in drugs:
    print(drug.tag)
    drug_id = drug.find("./drugbank-id[@primary='true']").text
    print(drug_id)
    groups = drug.find("./groups")
    flag = False
    if not groups:
        continue
    for group in groups:
        if group.text == 'approved':
            flag = True
            break
    if not flag:
        continue
    flag = False
    smiles = ""
    if drug.find("./calculated-properties") is None:
        continue
    for property in drug.find("./calculated-properties"):
        if property.find("./kind").text == 'SMILES':
            flag = True
            smiles = property.find("./value").text
            continue
    if not flag:
        continue
    
    describe = drug.find("./description")

    if describe is None:
        describe = ""
    else:
        describe = drug.find("./description").text
        if describe is None:
            describe = ""
        else:
            describe = describe.replace("\r", " ")
            describe = describe.replace("\n", " ")
    with open("DDI.txt", 'a') as f:
        f.write(drug_id)
        f.write("\t" + smiles)
        f.write("\t" + describe + "\n")
        f.close()


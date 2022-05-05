
import xml.etree.ElementTree as ET

drug_ids = set()
with open("./approved_drugs_smiles_desc.txt") as f:
    line = f.readline()
    while line:
        drug_ids.add(line.split("\t")[0])
        line = f.readline()
    f.close
print(len(drug_ids))

print("start loading")
tree = ET.parse("./full database.xml")
print("loading...")
drugs = tree.getroot()
print("loading done!")

print("loading dict")
dic = {}
with open("drugid2name.txt", "r") as f:
    line = f.readline()
    while line:
        dic[line.split("\t")[0]] = line.split("\t")[1].strip("\n")
        line = f.readline()
print("loading done!" + str(len(dic)))
with open("DDI.txt", 'w') as f:
    for drug in drugs:
        drug_id = drug.find("./drugbank-id[@primary='true']").text
        if drug_id not in drug_ids:
            continue
        for drug_inter in drug.find("./drug-interactions"):
            id = drug_inter.find("./drugbank-id").text
            if id not in drug_ids:
                continue
            relation = drug_inter.find("./description").text
            
            relation = relation.replace(dic[drug_id], "DRUG_CHENG")
            relation = relation.replace(dic[id], "DRUG_CHENG")
            
            f.write(drug_id + "\t" + id + "\t" + relation + "\t" + dic[drug_id] + "\t" + dic[id] + "\n")
    f.close()


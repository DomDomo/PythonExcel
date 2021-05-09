import json

CG = []
CMC = []

with open('CG.txt', 'r') as f:
    CG = json.loads(f.read())

with open('CMC.txt', 'r') as f:
    CMC = json.loads(f.read())

CGnames = []
CMCnames = []

for crypto in CG:
    CGnames.append(crypto["name"])
for crypto in CMC:
    CMCnames.append(crypto["name"])

same = set(CGnames).intersection(set(CMCnames))

for name in same:
    result = ""
    result += name
    for c in CG:
        if c["name"] == name:
            result += " | CG: "
            result += c["time"]
    for c in CMC:
        if c["name"] == name:
            result += " | CMC: "
            result += c["time"]
    print(result)
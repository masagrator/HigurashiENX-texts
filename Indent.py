import glob
import json

Files = glob.glob("*.json")

print(Files)

for i in range(0, len(Files)):
    print(Files[i])
    file = open(Files[i], "r")
    data = json.load(file)
    data = data["Main"]
    file.close()
    file = open(Files[i], "w", encoding="UTF-8")
    json.dump(data, file, indent="\t", ensure_ascii=False)
    file.close()
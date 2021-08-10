import json

with open("./DRONE_GCC_SECRET_DEV.json") as f:
    json_file = json.load(f)
    print(json_file)

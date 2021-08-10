import json
import os


drone_cred = os.environ.get("DRONE_GCC_SECRET_DEV")
json_file = json.dumps(drone_cred)
with open("./DRONE_GCC_SECRET_DEV.json","w",encoding='utf-8') as f:
    f.write(json.dumps(json.loads(drone_cred)))
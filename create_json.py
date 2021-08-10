import json
import os


drone_cred = os.environ.get("DRONE_GCC_SECRET_DEV")
print(drone_cred)
with open("./DRONE_GCC_SECRET_DEV.json","w",encoding='utf-8') as f:
    json.dump(drone_cred,f,ensure_ascii=True)
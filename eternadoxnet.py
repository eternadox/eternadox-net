import requests
import random
import time
import json
import string
import pycountry
S = requests.Session()

webhooks = [] # webhook here
while True:
   try: 
    delay = random.randint(0, 10000) / 1000

    fake_name_gen = json.loads(S.get("https://api.namefake.com/").content.decode("utf-8"))

    name_gen_2 = json.loads(S.get("https://randomuser.me/api/").content.decode("utf-8"))

    time.sleep(delay)

    desktopname = random.choice(["Desktop-"+''.join(random.choices(string.ascii_uppercase + string.digits, k=6)), str(name_gen_2["results"][0]["name"]["first"]).upper()+"-PC"])

    username=random.choice([name_gen_2["results"][0]["login"]["username"], str(name_gen_2["results"][0]["name"]["first"][0]+name_gen_2["results"][0]["name"]["last"]).lower(), str(name_gen_2["results"][0]["name"]["first"]).lower()])

    ip = fake_name_gen.get("ipv4")
    print(name_gen_2["results"])
    country = name_gen_2["results"][0]["location"]["country"]
    payload = {
        "content":f"{username}@{desktopname} :flag_{pycountry.countries.get(name=country).alpha_2.lower()}: ({ip}) joined the botnet!"
    }

    r = S.post(random.choice(webhooks), data=payload)
   except:
    time.sleep(120)
    continue
    


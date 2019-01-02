import requests as req
import json
import random
import time

i = 1

while True:
    try:
        print "Iteration: ", i
        r = req.get('https://api.nag-iot.zcu.cz/v2/variables?api_key=API')
        print r.text
        # print r.text.replace("[", "").replace("]", "")
        array = json.loads(r.text.replace("[", "").replace("]", ""))

        print array["value"]

        array["value"] = float(float(random.randint(242, 251)) / float(10))

        print array["value"]

        s = req.put('https://api.nag-iot.zcu.cz/v2/variable/teplota?api_key=API', json.dumps(array))
        # print json.dumps(array)
        print s.status_code
        time.sleep(100)
        i += 1
    finally:
        print ("lul")

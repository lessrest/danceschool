#!/usr/bin/env python
import json
import sys
import time
uid = sys.argv[1]
with open('/var/door/access.json') as accessfile:
    data = json.load(accessfile)
    row = data.get(uid)

    log = {
        "access": None,
        "uid": uid,
        "name": None,
        "date": time.strftime("%Y-%m-%d %H:%M")
    }
    
    if row is not None:
        log["access"] = row.get("access") == "Yes"
        log["name"] = row.get("name")
        
    print json.dumps(log)
    if log["access"] == True:
        sys.exit(0)
    else:
        sys.exit(-1)

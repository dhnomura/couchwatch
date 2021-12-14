import json
import requests
import glom
from get_keys import get_keys
from filter_metrics import filter_list

def get_couch_stats(couch_user, couch_pass, db_address, db_port, api):
    if api == "_system":
        api_url = "_node/_local/_system"
    elif api == "_stats":
        api_url = "_node/_local/_stats"
    exported_dictionary={}

    response = requests.get(f"{db_address}:{db_port}/{api_url}", auth=(couch_user,couch_pass))
    value    = (json.loads(response.text))
    for key in get_keys(value):
        val_key = (key)
        if "@" in val_key: 
            pass
        else:
            val_value = glom.glom(value, key)
            if isinstance(val_value,str) or isinstance(val_value,list):
                pass
            else:
                val_key=".".join([api,val_key]) # This was used to join ec2 hostname with the metric name
                exported_dictionary[val_key]=(val_value)
    return exported_dictionary
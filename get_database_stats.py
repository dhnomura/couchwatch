import json
import requests
import glom
from get_keys import get_keys
from filter_metrics import filter_list

def get_database_stats(couch_user, couch_pass, db_address, db_port):
    response = requests.get(f"{db_address}:{db_port}/_all_dbs", auth=(couch_user,couch_pass))
    value    = (json.loads(response.text)) # List of all user databases
    database_stats = {}
    filtered_list = {} 
    new_dict = {}
    for n in value:
        if not n.startswith('_'):
            response = requests.get(f"{db_address}:{db_port}/{n}", auth=(couch_user,couch_pass))
            db_info = (json.loads(response.text))
            for key in get_keys(db_info):
                # val_key = ".".join(['_db_metric', n, key])
                val_key = ".".join(['_db_metric', key])                
                val_value = glom.glom(db_info,key)
                if isinstance(val_value,str) or isinstance(val_value,list):
                    pass
                elif val_key.endswith("compact_running"):
                    database_stats[val_key]=(int(val_value))
                    filtered_list = filter_list(database_stats, "_database")
                else:
                    database_stats[val_key]=(val_value)
                    filtered_list = filter_list(database_stats, "_database")
            #filtered_list = filter_list(database_stats, "_database")
            #print(f"saida: {n}:{filtered_list}")
            new_dict[n] = filtered_list
            #print(new_dict)
    #return filtered_list 
    return new_dict

import json
import requests
import glom
from get_keys import get_keys
from filter_metrics import filter_list

def get_design_database_stats(couch_user, couch_pass, db_address, db_port):
    response = requests.get(f"{db_address}:{db_port}/_all_dbs", auth=(couch_user,couch_pass))
    value    = (json.loads(response.text)) # List of all user databases
    design_database_stats = {}
    filtered_list = {}
    new_dict = {}

    for n in value:
        if n.startswith('_'):
            pass
        else:
            database=n
            response = requests.get(f"{db_address}:{db_port}/{n}/_design_docs", auth=(couch_user,couch_pass))
            design_info = (json.loads(response.text))
            if design_info["total_rows"] == 0:
                pass
            else:
                design_docs=(design_info["rows"])
                i=0
                while i < (len(design_info["rows"])):
                    design_path=(design_docs[i]["id"])
                    i += 1
                    ddoc_url="/".join([database, design_path,"_info"])
                    response = requests.get(f"{db_address}:{db_port}/{ddoc_url}", auth=(couch_user,couch_pass))
                    ddoc_info = (json.loads(response.text))
                    for key in get_keys(ddoc_info):
                        val_key = ".".join(['_design_doc', key])
                        val_value = glom.glom(ddoc_info,key)
                        if isinstance(val_value,str) or isinstance(val_value,list):
                            pass
                        elif val_key.endswith("_running"):
                            design_database_stats[val_key]=(int(val_value))
                            filtered_list = filter_list(design_database_stats, "_design_database")
                        elif val_key.endswith("waiting_commit"):
                            design_database_stats[val_key]=(int(val_value))
                            filtered_list = filter_list(design_database_stats, "_design_database")
                        else:
                            design_database_stats[val_key]=(val_value)
                            filtered_list = filter_list(design_database_stats, "_design_database")
                new_dict[n] = filtered_list
    # print(new_dict)
    return new_dict
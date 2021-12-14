import boto3
from pprint import pprint
from couch_metrics_list.couch_metric_system import couch_system_filtered
from couch_metrics_list.couch_metric_stats  import couch_stats_filtered
from couch_metrics_list.couch_metric_stats  import requested_type
from couch_metrics_list.couch_metric_stats  import httpd_200
from couch_metrics_list.couch_metric_stats  import httpd_400
from couch_metrics_list.couch_metric_stats  import httpd_500
from couch_metrics_list.couch_metric_stats  import other_stats
from couch_metrics_list.couch_database_metrics import couch_database_filtered
from couch_metrics_list.couch_designdoc_metrics import couch_designdoc_filtered

def filter_list(couch_dictionary, api):
    """ Create a filtered list of key pairs according to couch_metrics_list files
    input(couch_dictionary[list], name_space[str], instance_name[str], api[str])
    output(newdict[dict]) 
    """
    couch_dictionary = couch_dictionary
    if api == "_system":
        filtered_list = couch_system_filtered
    elif api  == "_stats":
        filtered_list = couch_stats_filtered
    elif api  == "_stats_requested_type":
        filtered_list = requested_type
    elif api  == "_stats_200":
        filtered_list = httpd_200
    elif api  == "_stats_400":
        filtered_list = httpd_400
    elif api  == "_stats_500":
        filtered_list = httpd_500
    elif api  == "_stats_other":
        filtered_list = other_stats
    elif api == "_database":
        filtered_list = couch_database_filtered
    elif api == "_design_database":
        filtered_list = couch_designdoc_filtered
    main_dictionary = couch_dictionary
    newdict = { key:main_dictionary[key] for key in main_dictionary if key in filtered_list }
    return(newdict)

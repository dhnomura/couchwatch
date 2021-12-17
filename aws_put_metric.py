import boto3
from pprint import pprint
from filter_metrics import filter_list 

def create_cloudwatch_list(couch_dictionary, name_space, instance_name, api):
    """ Create a list of key pairs formated to be used by Cloudwatch putmetric api call
    input(couch_dictionary[list], name_space[str], instance_name[str])
    output(new_list[list]) 
    """
    a="MetricName"
    b="Value"
    couch_dictionary = couch_dictionary
    name_space       = name_space
    # if api == "_system" or api == "_stats":
    if api in ( "_system","_stats","_stats_requested_type","_stats_200","_stats_400","_stats_500","_stats_other"):
        instance_name    = instance_name
        dimension_key = "Dimensions"
        dimension_value = [{"Name": "Server", "Value": instance_name}]
        new_dict = {}
        new_dict_values = new_dict.values()
        for key, val in couch_dictionary.items():
            position=len(new_dict)
            new_dict[position]=({a: key, b:val, dimension_key: dimension_value})
        new_list = list(new_dict_values)
        # pprint(new_list)
        return(new_list)
    elif api == "_database" or api == "_design_database":
        new_dict = {}
        new_dict_values = new_dict.values()
        for database in couch_dictionary:
            instance_name = database
            inner_dict = couch_dictionary[instance_name]
            dimension_key = "Dimensions"
            dimension_value = [{"Name": "Database", "Value": instance_name}]
            for key, val in inner_dict.items():
                position=len(new_dict)
                new_dict[position]=({a: key, b:val, dimension_key: dimension_value})
        new_list = list(new_dict_values)
        return(new_list)


def aws_put_metric(couch_dictionary, name_space, instance_name, aws_region, api):
    """ This is the main function that is called by the main program,
    it's call the other two functions and at the end input couchdb metric to AWS Cloudwatch
    input(couch_dictionary[list], name_space[str], instance_name[str], aws_region[str] ,api[str])
    api_call_response[Boolean]
    """
    if api == "_database" or api == "_design_database":
        input_list    = create_cloudwatch_list(couch_dictionary, name_space, instance_name, api)
        #print(input_list)
#    elif api == "_system" or api == "_stats":
#    elif api == "_system" or api == "_stats" or api == "_stats_requested_type" or api == "_stats_200" or api == "_stats_400" or api == "_stats_500" or api == "_stats_other":
    elif api in ( "_system","_stats","_stats_requested_type","_stats_200","_stats_400","_stats_500","_stats_other"):
        # Filters metric according to couch_metrics_list/*.py
        filtered_list = filter_list(couch_dictionary, api)
        # Create an organized list to be used by cloudwatch input metrics
        input_list    = create_cloudwatch_list(filtered_list, name_space, instance_name, api)
    # Set cloudwatch class
    cloudwatch    = boto3.client("cloudwatch", region_name=aws_region) 
    # Insert Metrics
    response = cloudwatch.put_metric_data(
        MetricData = input_list,
        Namespace = name_space
    )
    # pprint(response)
    response_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if response_code == 200:
        return(True)
    else:
        return(False)


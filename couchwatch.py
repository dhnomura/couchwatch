#!/usr/bin/python3

# This python program collects metrics from CouchDB and upload to cloudwatch metrics.
# The metrics comes from _stats, _system and for each user database.

# Modules
import boto3
import json
import urllib.request
import requests
import time
import sys
from get_keys import get_keys
from aws_put_metric import aws_put_metric
from utilities import get_secret_value, password_is_valid, is_couch_up, get_instance_name
from get_database_stats import get_database_stats
from get_design_database_stats import get_design_database_stats
from get_couch_stats import get_couch_stats
from aws_put_metric import aws_put_metric

# Shell Variables
aws_secretid   = sys.argv[1] # first arg received from shell - SecretsManager Name
name_space     = sys.argv[2] # second arg received from shell - CloudWatch Name Space
timer          = int(sys.argv[3]) # time in seconds to retrieve metrics
metrics        = str(sys.argv[4]).lower() # Which Metrics to collect (all, db, ddocs, system)

# if input_metrics != "":
#     metrics = input_metrics.lower()

# Variables
db_address = "http://127.0.0.1"
db_port    = 5984

# Metric Dictionary
couchdb_system        = {}
couchdb_stats         = {}
database_stats        = {}
design_database_stats = {}

# AWS Resource Metadata
ec2_metadata   = json.loads(urllib.request.urlopen("http://169.254.169.254/latest/dynamic/instance-identity/document").read().decode())
ec2_hostname   = (''.join(urllib.request.urlopen("http://169.254.169.254/latest/meta-data/public-hostname").read().decode().split(".")[0]))
ec2_resourceid = ec2_metadata["instanceId"] # Dynamic way to get the current resource id
aws_region     = ec2_metadata["region"] # Dynamic way to get the region where the script is deployed
cloudwatch     = boto3.client("cloudwatch", region_name=aws_region) # set cloudwatch class
ec2            = boto3.client("ec2", region_name=aws_region) # set ec2 class

# Retrive Password from Secrets Manager
secrets = json.loads(get_secret_value(aws_secretid,aws_region)["SecretString"])
couch_user = secrets["username"]
couch_pass = secrets["password"]
instance_name = get_instance_name(ec2_resourceid, aws_region)

# Check if CouchDB is running
while True: # Run Forever
    if not is_couch_up(couch_user, couch_pass, db_address, db_port):
        sys.exit(f"Error 500: CouchDB is not running")

    # Loop all urls and put the metrics recived on cloudwatch metrics
    # while True: # Run Forever
    if not password_is_valid(couch_user,couch_pass,db_address,db_port):
        sys.exit(f"Error 401: Invalid Password") # Exit the program if the password fail

    else:
        if True: # Run Forever
            couchdb_system = get_couch_stats(couch_user, couch_pass, db_address, db_port, "_system")
            couchdb_stats  = get_couch_stats   (couch_user, couch_pass, db_address, db_port, "_stats")
            database_stats = get_database_stats(couch_user, couch_pass, db_address, db_port)
            design_database_stats = get_design_database_stats(couch_user, couch_pass, db_address, db_port)
            if len(couchdb_system) > 0 :
                if not aws_put_metric(couchdb_system, name_space, instance_name, aws_region, "_system"):
                    sys.exit(f"Error 99: Cloudwatch inputmetric fails") # Exit the program
            if len(couchdb_stats) > 0 :
                if not aws_put_metric(couchdb_stats, name_space, instance_name, aws_region, "_stats_requested_type"):
                    sys.exit(f"Error 99: Cloudwatch inputmetric fails") # Exit the program
                if not aws_put_metric(couchdb_stats, name_space, instance_name, aws_region, "_stats_200"):
                    sys.exit(f"Error 99: Cloudwatch inputmetric fails") # Exit the program
                if not aws_put_metric(couchdb_stats, name_space, instance_name, aws_region, "_stats_400"):
                    sys.exit(f"Error 99: Cloudwatch inputmetric fails") # Exit the program
                if not aws_put_metric(couchdb_stats, name_space, instance_name, aws_region, "_stats_500"):
                    sys.exit(f"Error 99: Cloudwatch inputmetric fails") # Exit the program
                if not aws_put_metric(couchdb_stats, name_space, instance_name, aws_region, "_stats_other"):
                    sys.exit(f"Error 99: Cloudwatch inputmetric fails") # Exit the program
            if len(database_stats) > 0 :
                if not aws_put_metric(database_stats, name_space, instance_name, aws_region, "_database"):
                    sys.exit(f"Error 99: Cloudwatch inputmetric fails") # Exit the program
            if len(design_database_stats) > 0 :
                if not aws_put_metric(design_database_stats, name_space, instance_name, aws_region, "_design_database"):
                    sys.exit(f"Error 99: Cloudwatch inputmetric fails") # Exit the program
    time.sleep(timer) # Sleep 150 seconds
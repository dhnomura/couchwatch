import boto3
import requests

def get_secret_value(name, region_name, version=None):
    """Gets the value of a secret.

    Version (if defined) is used to retrieve a particular version of
    the secret.
    """
    secrets_client = boto3.client("secretsmanager", region_name=region_name)
    kwargs = {'SecretId': name}
    if version is not None:
        kwargs['VersionStage'] = version
    response = secrets_client.get_secret_value(**kwargs)
    return response


def password_is_valid(couch_user, couch_pass, db_address, db_port):
    """Check if the version of password is correct
    input(couch_user[str], couch_pass[str])
    output(CouchDB API Response Code)
    This function is made to avoid unecessary API Calls to secrets manager
    """
    response = requests.get(f"{db_address}:{db_port}", auth=(couch_user,couch_pass))
    response_code = response.status_code
    if response_code == 401: # 401 - Authent Error: then retrive password
        return False
    elif response_code == 200: # 200 - Ok: continue with the program
        return True
    else:
        return False


def is_couch_up(couch_user, couch_pass, db_address, db_port):
    """Check if CouchDB is running, return(Boolean)
    """
    response = requests.get(f"{db_address}:{db_port}/_up", auth=(couch_user,couch_pass))
    response_code = response.status_code
    if response_code == 200:
        return(True)
    else:
        return(False)


def get_instance_name(ec2_resourceid, aws_region):
    """ When given an instance ID as str e.g. 'i-1234567', return the instance 'Name' from the name tag
    input(str, EC2InstanceID)
    output(str, EC2 Tag Name) 
    """
    ec2 = boto3.resource('ec2', region_name=aws_region)
    ec2instance = ec2.Instance(ec2_resourceid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return instancename
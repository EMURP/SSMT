import boto
import boto.s3.connection
import os
import sys

access_key = os.environ.get('access_key')
secret_key = os.environ.get('secret_key')
endpoint = os.environ.get('endpoint')

def interface_pull(filename):

    conn = boto.connect_s3(
                aws_access_key_id = access_key,
                aws_secret_access_key = secret_key,
                host = endpoint,
                #is_secure=False,               # uncomment if you are not using ssl
                calling_format = boto.s3.connection.OrdinaryCallingFormat(),
                )
    bucket = conn.get_bucket('Automated-Report')
    key_name = 'OpenShift/' + filename
    key = bucket.get_key(key_name)
    x = '/tmp/SSMT/'+str(key.key) # path to download the file from object store
    key.get_contents_to_filename(x)

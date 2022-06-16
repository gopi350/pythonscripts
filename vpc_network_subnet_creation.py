"""
//organization : Sonata-software-Limited
//developed by : python team
//code         : vpc_with_subnet_creation
//created on   : 26-05-2022
//code language: python
 """

from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import time

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

region = 'us-central1'      # add region

# Project ID for this request.
project = 'sonata-automation'           # Project ID

network_body = {
    "routingConfig": {
        "routingMode": "REGIONAL"    # Dynamic routing mode """Regional"""
    },
    "autoCreateSubnetworks": False,    # creation mode ""Custom""
    "name": "sonatanetwork",          # vpc network name
    "mtu": 1460,
    "region": f"{region}"
}

subnetwork_body = {
    "enableFlowLogs": False,
    'ipCidrRange': "10.0.0.0/24",   # range
    "name": "publicsubnet",
    "network": "projects/sonata-automation/global/networks/sonatanetwork",  # important
    "privateIpGoogleAccess": False,
    "region": f"{region}"
}


request1 = service.networks().insert(project=project, body=network_body)
response1 = request1.execute()


print("creating network...\n")
time.sleep(30)

request2 = service.subnetworks().insert(project=project, region=region, body=subnetwork_body)
response2 = request2.execute()

pprint(response1)
pprint(response2)


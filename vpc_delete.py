"""
//organization : Sonata-software-Limited
//developed by : python team
//code         : vpc_network_delete
//created on   : 26-05-2022
//code language: python
 """

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import time

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'sonata-automation'

# Name of the network to delete.
network = 'sonata-network'

request = service.networks().delete(project=project, network=network)

print("deleting network...\n")
time.sleep(25)

response = request.execute()

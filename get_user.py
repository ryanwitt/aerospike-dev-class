from aerospike_client import client
import sys
import pprint

client.connect()

# Get parameters from command line
username = sys.argv[1]

# Grab user object
key = ('test', 'users', username)
(key, metadata, record) = client.get(key)
print 'user:', record

client.close()

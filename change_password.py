from aerospike_client import client
import sys
import pprint

client.connect()

# Get parameters from command line
username, new_password = sys.argv[1:]

# Grab user object
key = ('test', 'users', username)
ret = client.apply(key, 'tweetspike', 'update_password', [new_password])
print ret

client.close()

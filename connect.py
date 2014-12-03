from aerospike_client import client
import sys

print 'connectng'
client.connect()
print 'disconnecting'
client.close()

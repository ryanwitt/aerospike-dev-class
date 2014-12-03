from aerospike_client import client
import sys
client.connect()
client.udf_put({}, 'tweetspike.lua', 0)
print 'registered module'
client.close()

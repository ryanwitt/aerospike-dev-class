from aerospike_client import client
import sys

client.connect()

# Get parameters from command line
username, password, gender, region, interests = sys.argv[1:]
key = ('test', 'users', username)
rec = {
    'username': username,
    'password': password,
    'gender': gender,
    'region': region,
    'lasttweeted': 0,
    'tweetcount': 0,
    'interests': interests.split(','),
}
meta = { 'ttl': 3600, 'gen': None }
policy = None #{'retry': 0,'key':0,'generation': 0,'exists': 3}
#print key, rec, meta, policy
client.put(key, rec, meta, policy)
print 'created', rec

client.close()

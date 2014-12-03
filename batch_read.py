from aerospike_client import client
import sys, time

client.connect()

# Get parameters from command line
username = sys.argv[1]

# Grab user object
key = ('test', 'users', username)
(key, metadata, record) = client.get(key)
print 'user:', record
tweetcount = record.get('tweetcount', 0)
for i in range(tweetcount):
    key = ('test', 'tweets', username + ':' + str(i+1))
    try:
        (key, metadata, record) = client.get(key)
    except:
        import traceback; traceback.print_exc()
    print 'tweet:', record

client.close()

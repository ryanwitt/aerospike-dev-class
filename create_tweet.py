from aerospike_client import client
import sys, time

client.connect()
print client

# Get parameters from command line
username, tweet = sys.argv[1:]

# Grab user object
key = ('test', 'users', username)
(key, metadata, record) = client.get(key)
print key, metadata, record

# HACK: grab current tweetcount. We actually should
#       atomically increment this before creating tweet
tweetcount = record.get('tweetcount', 0) + 1

# Increment the tweet count
client.put(key, {'tweetcount': tweetcount})

# Post tweet
key = ('test', 'tweets', username + ':' + str(tweetcount))
tweet = {
    'username': username,
    'tweet': tweet,
    'ts': int(time.time()),
}
client.put(key, tweet)

client.close()

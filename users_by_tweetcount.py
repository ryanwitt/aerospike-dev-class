from aerospike_client import client
from aerospike import predicates as p
import sys
client.connect()
min_tweets, max_tweets = sys.argv[1:]
query = client.query('test', 'users')
query.where(p.between('tweetcount', int(min_tweets), int(max_tweets)))
def callback((key, meta, record)):
    print record
query.foreach(callback)
client.close()

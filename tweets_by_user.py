from aerospike_client import client
from aerospike import predicates as p
import sys
client.connect()
username = sys.argv[1]
query = client.query('test', 'tweets')
query.where(p.equals('username', username))
def callback((key, meta, record)):
    print record
query.foreach(callback)
client.close()

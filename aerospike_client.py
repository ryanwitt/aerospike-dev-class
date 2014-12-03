import aerospike

config = {
    'hosts': [
        ( '54.146.64.48', 3000 )
    ],
    'policies': {
        'timeout': 1000 # milliseconds
    }
}

client = aerospike.client(config)

import redis

# Connect to Redis Client
hostname = 'redis-19968.c257.us-east-1-3.ec2.redns.redis-cloud.com'
portnumber = 19968
password = '4vB8DkhC4TNFsfW5SgMOUIdPZnswSdID'

r = redis.StrictRedis(host=hostname,
                      port=portnumber,
                      password=password)

# Simulated Logs
with open('simulated_logs.txt', 'r') as f:
    logs_text = f.read()

encoded_logs = logs_text.split('\n')

# Push into Redis database
r.lpush('attendance:logs', *encoded_logs)

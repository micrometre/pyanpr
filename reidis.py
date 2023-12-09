import redis
 
redis_client = redis.Redis(host='localhost', port=6379, db=0)
 
redis_client.set('key', 'value')
data = redis_client.get('key')
print(data) 
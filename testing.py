#!/home/dell/repos/pyanpr/.venv/bin/python
import redis

r = redis.StrictRedis(host='0.0.0.0', port=6379, db=0, decode_responses=True)

def list_items():
    list_alpr= []
    stored_alpr  = r.hgetall(
        f"alpr_id*"
        )
    print((stored_alpr))
    for x in stored_alpr:
        print((x))
    return("22")

list_items()    
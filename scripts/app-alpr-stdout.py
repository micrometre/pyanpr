import redis
import os   


r = redis.Redis(
    host='localhost',
    port=6379,
)
redis_host = "redis"
stream_key = "alpr"


               


def alpr_from_img():
    result_stdout = os.popen('./scripts/monit.sh').read()
    stdout_list = result_stdout.split()
    l2=stdout_list[::2]
    l3=stdout_list[1::2]
    for f, b in zip(l2, l3):
        print(result_stdout)
        r.xadd( stream_key, { f: b} )
        return(f,b)

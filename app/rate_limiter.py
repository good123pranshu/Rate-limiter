import time
from app.redis_client import redis_client
from app.config import RATE_LIMIT,RATE_WINDOW

MAX_TOKENS = RATE_LIMIT 
TTL = RATE_WINDOW             
REFILL_RATE = 1 / 6     

def is_allowed(identifier: str) :
    key = f"rate:{identifier}"
    now = time.time()

    pipe = redis_client.pipeline()
    pipe.hgetall(key)
    result = pipe.execute()[0]

    if result:
        tokens = float(result.get("tokens", MAX_TOKENS))
        last_time = float(result.get("timestamp", now))
    else:
        tokens = MAX_TOKENS
        last_time = now

    elapsed = now - last_time
    tokens = min(MAX_TOKENS, tokens + elapsed * REFILL_RATE)

    if tokens < 1:
        return False
    tokens -= 1

    pipe = redis_client.pipeline()
    pipe.hset(key, mapping={
        "tokens": tokens,
        "timestamp": now
    })
    pipe.expire(key, TTL)
    pipe.execute()

    return True

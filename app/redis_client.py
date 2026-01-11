from redis import Redis
from app.config import REDIS_URL
import os




redis_client = Redis.from_url(
    REDIS_URL,   
    decode_responses=True
)


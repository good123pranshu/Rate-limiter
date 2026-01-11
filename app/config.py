import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0") 


RATE_LIMIT = 10    
RATE_WINDOW = 120   

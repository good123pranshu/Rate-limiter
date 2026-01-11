import os
from dotenv import load_dotenv

load_dotenv()
REDIS_URL =os.environ.get("REDIS_URL", "") 



RATE_LIMIT = 10    
RATE_WINDOW = 120   

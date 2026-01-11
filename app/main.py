from fastapi import FastAPI, Request, HTTPException
from app.rate_limiter import is_allowed
from fastapi.responses import JSONResponse

app = FastAPI(title="Redis Rate Limiter")

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host

    if not is_allowed(client_ip):
       return JSONResponse(
            status_code=429,
            content={"detail": "Too many requests"}
        )

    return await call_next(request)

@app.get("/")
def home():
    try:
        return {"message": "Hello, you are within the rate limit!"}
    except Exception as e:
        return {"error":e}

@app.get("/data")
def get_data():
    return {"data": "This endpoint is rate-limited"}

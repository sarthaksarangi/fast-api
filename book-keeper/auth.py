from fastapi import  HTTPException, Header

API_KEY = "my_secret_api"

def verify_api_key(x_api_key: str = Header()):
    """Verify API KEY"""
    if  x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from auth import verify_api_key
from database import get_session
from models.user import User, UserCreate, UserCreateResponse


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserCreateResponse)
def register_user(user_data: UserCreate, session: Session = Depends(get_session),
api_key: str = Depends(verify_api_key)):
   
   #match the api key with env
   if api_key != os.getenv("API_KEY"):
    raise HTTPException(status_code=401, detail="Invalid API Key")
   #check if the user already exists
   existing_user = session.exec(select(User).where(User.email == user_data.email)).first()
   if existing_user:
    raise HTTPException(status_code=400, detail="User already exists")

   new_user = User.validate_and_create(user_data)
   session.add(new_user)
   session.commit()
   session.refresh(new_user)
   return new_user
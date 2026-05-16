from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    user_name : str
    user_email : EmailStr
    user_password : str
    user_contact_no : str

class UserResponse(BaseModel):
    user_name : Optional[str]
    user_email : Optional[EmailStr]
    user_contact_no : Optional[str]

class UserUpdate(BaseModel):
    user_name : Optional[str] = None
    user_email : Optional[EmailStr] = None
    user_contact_no : Optional[str] = None
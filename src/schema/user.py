from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    user_name : str
    user_email : EmailStr
    user_password : str
    user_contact_no : str
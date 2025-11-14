# Base case, all PII is logged
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class PersonalInfo(BaseModel):
    name: str
    email: EmailStr


class ResponseModel(BaseModel):
    status: str
    data: PersonalInfo


@app.post("/pii")
def post_pii(personal_info: PersonalInfo) -> dict:
    print("Received personal information:", personal_info)
    return {"status": "success", "data": personal_info}

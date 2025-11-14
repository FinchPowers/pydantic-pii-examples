# improvement: by using SecretStr, PII is not logged, but not returned either
from fastapi import FastAPI
from pydantic import (
    BaseModel,
    EmailStr,
    SecretStr,  # new import
)

app = FastAPI()


class PersonalInfo(BaseModel):
    name: SecretStr  # changed to SecretStr
    email: EmailStr


class ResponseModel(BaseModel):
    status: str
    data: PersonalInfo


@app.post("/pii")
def post_pii(personal_info: PersonalInfo) -> dict:
    print("Received personal information:", personal_info)
    print("name:", personal_info.name)  # still renders '**********'
    print(
        "name.get_secret_value():", personal_info.name.get_secret_value()
    )  # renders the actual value
    return {"status": "success", "data": personal_info}

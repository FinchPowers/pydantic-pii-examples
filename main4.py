# Improvement: Deal with the EmailStr field
from typing import Annotated

from fastapi import FastAPI
from pydantic import (
    BaseModel,
    BeforeValidator,  # new import
    EmailStr,
    PlainSerializer,
    SecretStr,
)

app = FastAPI()


PIIStr = Annotated[
    SecretStr,
    PlainSerializer(
        lambda x: x.get_secret_value(),
        return_type=str,
        when_used="json",
    ),
]

# Introducing PIIEmailStr
PIIEmailStr = Annotated[
    SecretStr,
    # introducing the BeforeValidator
    BeforeValidator(lambda x: EmailStr._validate(x)),  # noqa: SLF001
    PlainSerializer(
        lambda x: x.get_secret_value(),
        return_type=str,
        when_used="json",
    ),
]


class PersonalInfo(BaseModel):
    name: PIIStr
    email: PIIEmailStr


class ResponseModel(BaseModel):
    status: str
    data: PersonalInfo


@app.post("/pii")
def post_pii(personal_info: PersonalInfo) -> dict:
    print("Received personal information", personal_info)
    return {"status": "success", "data": personal_info}

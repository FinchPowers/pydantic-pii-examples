# improvement, with the Annotated type PIIStr, we can hide it when logging,
# but still return the value when serializing to json
from typing import Annotated  # new import

from fastapi import FastAPI
from pydantic import (
    BaseModel,
    EmailStr,
    PlainSerializer,  # new import
    SecretStr,
)

app = FastAPI()

# introducing PIIStr
PIIStr = Annotated[
    SecretStr,  # under the hood, that's the real type
    PlainSerializer(  # when serializing ...
        lambda x: x.get_secret_value(),  # ... render the value ...
        return_type=str,
        when_used="json",  # ... but only when serializing to json
    ),
]


class PersonalInfo(BaseModel):
    name: PIIStr  # switch to PIIStr
    email: EmailStr


class ResponseModel(BaseModel):
    status: str
    data: PersonalInfo


@app.post("/pii")
def post_pii(personal_info: PersonalInfo) -> dict:
    print(
        "raw personal information:",
        personal_info,
    )
    print(
        "default model dump (python) of personal information:",
        personal_info.model_dump(),
    )
    print(
        "json model dump of personal information:",
        personal_info.model_dump(mode="json"),
    )
    return {"status": "success", "data": personal_info}

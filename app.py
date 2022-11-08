import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class VerifyData(BaseModel):
    user_image: str
    id_image: str


@app.get('/')
async def index():
    '''
    Application root.
    '''
    return {"Server": "Running"}

@app.post("/verify")
async def make_verification(request_data:VerifyData):
    '''
    Make recommendations using the users unique serial number.
        :param userid: the unique serial number of the user.
        :returns: a json (map) of the recommendations made.
    '''
    return {"Authorize User": True}




if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8004)
    #uvicorn app:app --reload


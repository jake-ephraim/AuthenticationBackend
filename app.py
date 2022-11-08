import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

USERPATH = "./user"
IDPATH = "./id"


class VerifyData(BaseModel):
    user_image: str
    id_image: str
    file_type: str


def save_file(file_bin:str, file_path:str, file_type:str):
    pass

@app.get('/')
def index():
    '''
    Application root.
    '''
    return {"Server": "Running"}

@app.post("/verify")
async def make_verification(request_data:VerifyData):
    '''
    cross-validate user and submitted identity.
    '''
    authorize_user = False
    try:
        save_file(request_data.user_image, USERPATH, request_data.file_type)
        save_file(request_data.user_image, IDPATH, request_data.file_type)
    except Exception as e:
        pass
    return {"Authorize User": authorize_user}




if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8004)
    #uvicorn app:app --reload


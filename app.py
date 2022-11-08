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


def save_file(file_bin:str|list, file_path:str|list, file_type:str):
    pass

def its_a_face(image:str, file_type:str) -> bool:
    pass

@app.get('/')
def index():
    '''
    Application root.
    '''
    return {"Server": "Running"}

@app.post("/verify")
def make_verification(request_data:VerifyData):
    '''
    cross-validate user and submitted identity.
    '''
    authorize_user = False
    msg = ""
    user_image = request_data.user_image
    id_image = request_data.id_image
    file_type = request_data.file_type
    try:
        save_file([user_image, id_image], [USERPATH, IDPATH], file_type)
        if not its_a_face(USERPATH, file_type):
            msg = "User image not a face"
            raise(Exception("User image not a face"))
        if not its_a_face(IDPATH, file_type):
            msg = "ID image not a face"
            raise(Exception("ID image not a face"))
    except Exception as e:
        pass
    return {"Authorize User": authorize_user, "msg": msg}




if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8004)
    #uvicorn app:app --reload


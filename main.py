from fastapi import FastAPI

app = FastAPI()#インスタンス化、


@app.get("/hello")#デコレータ、API根幹作成
async def hello():
    return {"message": "hello world!"}
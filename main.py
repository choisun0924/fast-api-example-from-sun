from fastapi import FastAPI
import uvicorn

testServer = FastAPI()

@testServer.get("/")
def test():
    return 'testServer'

@testServer.get("/data")
def test():
    return {'testServer': 1234}

if __name__ == '__main__':
    uvicorn.run(app="main:testServer",
                host="localhost",
                port=7000,
                reload=True,
                workers=4)



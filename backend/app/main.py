from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def start():
    return {'Hello': 'World'}

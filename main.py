from fastapi import FastAPI
from routers.login import router

app = FastAPI()

app.include_router(router)
#app.include_router()
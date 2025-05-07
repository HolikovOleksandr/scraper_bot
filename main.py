from fastapi import FastAPI
from routers import olx_scraper 


app = FastAPI()

app.include_router(olx_scraper.router)

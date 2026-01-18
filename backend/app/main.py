from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request

from app.db.database import Base, engine
from app.routers.auth import router as auth_router

templates = Jinja2Templates(directory="app/templates")

Base.metadata.create_all(engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/templates/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def accueil(request: Request):
        return templates.TemplateResponse("layout.html", {"request": request, "titre": "Enrollix"})
    
app.include_router(auth_router)

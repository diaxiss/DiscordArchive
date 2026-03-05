from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routers.router import router

app = FastAPI()

app.mount(
    '/data/media',
    StaticFiles(directory="data/media"),
    name="media"
)
app.mount(
    '/data/guild_icons',
    StaticFiles(directory="data/guild_icons"),
    name="guild_icons"
)
app.mount(
    '/data/avatars',
    StaticFiles(directory="data/avatars"),
    name="avatars"
)


# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
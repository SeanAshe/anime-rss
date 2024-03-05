from fastapi import FastAPI
from nicegui import app, ui
from .web import main

app = FastAPI()
ui.run_with(app)


from fastapi import FastAPI
from generator import MapGenerator
app = FastAPI()

generator = MapGenerator()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


@app.get("/start")
async def map_info() -> dict:
    generator.start_generator()
    return {"start": f"{generator.current_map_state}"}


@app.get("/stop")
async def map_info() -> dict:
    generator.stop_generator()
    return {"stop": f"{generator.current_map_state}"}


@app.get("/update")
async def map_info() -> dict:
    generator.restart_generator()
    return {"res": f"{generator.current_map_state}"}


@app.get("/status")
async def map_info() -> dict:
    return {"now": f"{generator.current_map_state}"}

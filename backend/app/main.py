from imp import reload
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from water_jud_riddle import JugTooSmallException, WaterJugSolver

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_root():
    return {"Hello": "World"}


@app.post("/solve")
def solve(x: int, y: int, z: int):
    solver = WaterJugSolver(x, y, z)
    result = solver.solve()
    return result


@app.exception_handler(JugTooSmallException)
def jug_too_small_exception(request, excep: JugTooSmallException):
    return JSONResponse({"reason": excep.reason}, status_code=400)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True, workers=3)

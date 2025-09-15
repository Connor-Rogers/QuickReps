import os

from fastapi import FastAPI
from rest_lib.routes import router as rest_lib_router
# Get the server script path (same directory as this file)
current_dir = os.path.dirname(os.path.abspath(__file__))



def create_app() -> FastAPI:
    app = FastAPI()

    # Include the router from rest_lib
    from rest_lib.routes import router as rest_lib_router
    app.include_router(rest_lib_router)
    
    return app

if __name__ == "__main__":
    app = create_app()
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

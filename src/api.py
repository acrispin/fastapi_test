from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
from src.log import setup_custom_logger, formatter, logging, fileHandler

logger = setup_custom_logger(__name__)
fastapi_logger.handlers = logger.handlers
fastapi_logger.setLevel(logger.level)

# uvicorn_access_logger = logging.getLogger("uvicorn.access")
# uvicorn_access_logger.handlers = logger.handlers
# uvicorn_access_logger.setLevel(logger.level)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = []
uvicorn_access_logger.addHandler(handler)
uvicorn_access_logger.setLevel(logger.level)
uvicorn_access_logger.addHandler(fileHandler)

app = FastAPI()


# @app.on_event("startup")
# async def startup_event():
#     logger.info("startup_event.")
#     handler = logging.StreamHandler()
#     handler.setFormatter(formatter)
#     uvicorn_access_logger = logging.getLogger("uvicorn.access")
#     uvicorn_access_logger.handlers = []
#     uvicorn_access_logger.addHandler(handler)
#     uvicorn_access_logger.setLevel(logger.level)
#     uvicorn_access_logger.addHandler(fileHandler)


@app.get("/")
async def root():
    logger.info("root.")
    return {"message": "Hello World."}

"""
# No usar flag --reload por problemas de archivos logs, 
# Solo usar --reload-dir en desarrollo
uvicorn src.api:app --reload-dir src/ --debug
uvicorn src.api:app --debug --reload-dir src/
"""

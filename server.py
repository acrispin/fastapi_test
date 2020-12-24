import os
import uvicorn
from src.log import setup_custom_logger, BASE_DIR

logger = setup_custom_logger(__name__)


if __name__ == "__main__":
    logger.info("Inicio de server ...................")
    # uvicorn.run("src.api2:app", host="127.0.0.1", port=8000, debug=True, reload_dirs=[os.path.join(BASE_DIR, "src")], log_config=None)
    uvicorn.run("src.api2:app", host="127.0.0.1", port=8000, debug=True, reload_dirs=[os.path.join(BASE_DIR, "src")], log_config=None, workers=2)

"""
# No usar flag reload por problemas de archivos logs, 
# Solo usar reload-dirs en desarrollo
python server.py
python -m server
"""

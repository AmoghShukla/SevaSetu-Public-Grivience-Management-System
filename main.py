from fastapi import FastAPI
from src.utlis.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title="SevaSetu : Public Grivience Resolution System")

@app.get('/')
def home():
    logger.info("The Application is running")
    return {
        'message' : 'The Application is up and running!!!'
    }
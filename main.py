from fastapi import FastAPI, APIRouter

app = FastAPI(title="SevaSetu : Public Grivience Resolution System")
health_router = APIRouter(prefix='/app/v1')

@health_router.get('/health', tags=['health'])
def health():
    return {
        'message' : "Welcome to the SevaSetu Application!!"
    }


app.include_router(health_router)
from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from database import init_db, engine


logging.basicConfig(level=logging.INFO, filename='server.log',)
logging.basicConfig(level=logging.ERROR, filename='error.log',)

@asynccontextmanager
async def lifespan(app: FastAPI):
  logging.info("Server is starting up...")
  logging.info("Initializing the database...")
  init_db()
  
  yield
  engine.dispose()
  logging.info("Server is shutting down...")

app = FastAPI(lifespan=lifespan)


# endpoints
@app.get('/health')
def health_check():
  logging.info("Health check performed")
  return {"status": "healthy"}

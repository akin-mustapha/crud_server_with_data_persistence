from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO, filename='server.log',)
logging.basicConfig(level=logging.ERROR, filename='error.log',)

# endpoints
@app.get('/health')
def health_check():
  logging.info("Health check performed")
  return {"status": "healthy"}
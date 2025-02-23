from fastapi import FastAPI
import random


app = FastAPI()

@app.get("/health")
def health_check():
    return "Healthy"

@app.get("/random_choice")
def random_choice():
    random_number = random.randint(0, 200)
    return {"random_number": random_number}
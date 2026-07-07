from fastapi import FastAPI

app = FastAPI(title="Student Services Assistant API")


@app.get("/health")
def health():
    return {"status": "ok"}
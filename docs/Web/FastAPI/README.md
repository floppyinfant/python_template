# FastAPI
https://fastapi.tiangolo.com/  

uvicorn  
https://www.uvicorn.org/  
ASGI web server implementation for Python  

---

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

```
fastapi dev main.py
```
open browser at http://localhost:8000
open browser at http://127.0.0.1:8000/docs

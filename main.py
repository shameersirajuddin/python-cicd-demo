import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 1. Mount the static directory
# We check if it exists first to avoid the RuntimeError locally
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. Set up templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Renders the home page using the index.html template.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
def health_check():
    """
    Simple health check for CI/CD pipelines.
    """
    return {"status": "healthy"}

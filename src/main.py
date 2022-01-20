from fastapi import FastAPI
from src.database import Base, engine
from src.routers import product
from fastapi.responses import RedirectResponse

# Create the database
Base.metadata.create_all(engine)

# Initialize the app
app = FastAPI()
app.include_router(product.router)


@app.get("/", response_class=RedirectResponse)
def root():
    return "/docs"

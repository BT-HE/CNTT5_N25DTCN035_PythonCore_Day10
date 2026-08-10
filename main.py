from fastapi import FastAPI

from database import engine, Base

from routers import book_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library Management API"
)

app.include_router(book_router.router)
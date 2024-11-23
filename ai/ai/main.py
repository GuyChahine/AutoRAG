from fastapi import FastAPI

from ai.routes import embed, scrap, chunk

app = FastAPI()


@app.get("/")
def root():
    return "ai is running!"


app.include_router(embed.router)
app.include_router(scrap.router)
app.include_router(chunk.router)

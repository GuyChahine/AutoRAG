from fastapi import FastAPI

from ai.routes import embed, scrap, chunk, clean, llm

app = FastAPI()


@app.get("/")
def root():
    return "ai is running!"


app.include_router(scrap.router)
app.include_router(clean.router)
app.include_router(chunk.router)
app.include_router(embed.router)
app.include_router(llm.router)

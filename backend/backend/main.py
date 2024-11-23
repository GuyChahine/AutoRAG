from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "backend is running!"


# add chatbot
# remove chatbot
#

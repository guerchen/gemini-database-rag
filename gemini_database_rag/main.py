from fastapi import FastAPI

from gemini_database_rag.agents import (
    create_retrieval, create_response_generation
    )
from gemini_database_rag.database import Base, engine, query_db, import_data
from gemini_database_rag.models import Prompt

app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    import_data()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/source_data")
async def retrieve_source_data():
    return {"result": query_db("SELECT * FROM users")}


@app.post("/prompt")
async def prompt_model(prompt: Prompt):
    sql_query = create_retrieval(prompt.question)
    if sql_query == "idk":
        return {"answer": "I am sorry, but I'm not able to fulfill this request"}

    relevant_data = query_db(sql_query)
    print(relevant_data)
    response = create_response_generation(
        prompt.question, sql_query, relevant_data
        )

    return {"answer": response}

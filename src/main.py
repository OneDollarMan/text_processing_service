from contextlib import asynccontextmanager
from fastapi import FastAPI
from schemas import InputTextSchema, ProcessedTextSchema, SearchResultsSchema
from utils import process_text, search


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)


@app.post('/process_text', response_model=ProcessedTextSchema)
def post_process_text(text_schema: InputTextSchema):
    return process_text(text_schema.text)


@app.post('/search', response_model=SearchResultsSchema)
def post_search(text_schema: InputTextSchema):
    return search(text_schema.text)
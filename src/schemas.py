from pydantic import BaseModel


class InputTextSchema(BaseModel):
    text: str


class ProcessedTextSchema(BaseModel):
    tokens: list[str]


class SearchResultSchema(BaseModel):
    text: str
    score: float


class SearchResultsSchema(BaseModel):
    results: list[SearchResultSchema]
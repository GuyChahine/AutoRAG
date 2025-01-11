from pydantic import BaseModel


class LLM(BaseModel):
    query: str
    query_results: list[str]
    prompt_id: str = "6782950fd77e9d5427fe58ef"


class LLMResponse(BaseModel):
    output: str
    prompt_tokens: int
    completion_tokens: int

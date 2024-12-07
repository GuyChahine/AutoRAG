from fastapi import APIRouter, Path
from pydantic import BaseModel
from bson import ObjectId

from ai.src import llm
from ai.backend import MONGO_CLIENT

router = APIRouter(prefix="/llm")

LLM_MAP = {"gpt": llm.GPT()}


class LLMSchema(BaseModel):
    query: str
    query_results: list[str]
    query_type: str = "ui"
    prompt_id: str = "67539384c8a90354a93e32f2"


@router.post("/{model}/{sub_model}")
def llm(
    data: LLMSchema,
    model: str = "gpt",
    sub_model: str = "gpt-4o-mini",
) -> str:
    col = MONGO_CLIENT["prompt"][data.query_type]
    prompt = col.find_one(
        {"_id": {"$eq": ObjectId(data.prompt_id)}},
        {"prompt": 1},
    )["prompt"]
    for message in prompt:
        message["content"] = message["content"].format(
            query=data.query,
            query_results="\n".join(data.query_results),
        )
    output = LLM_MAP[model](
        sub_model=sub_model,
        prompt=prompt,
    )
    return output

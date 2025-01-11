from fastapi import APIRouter, Path, Body, Query
from pydantic import BaseModel
from bson import ObjectId

from ai.src import llm
from ai.backend import MONGO_CLIENT
from ai.models import llm as models

router = APIRouter(prefix="/llm")

LLM_MAP = {"gpt": llm.GPT()}


@router.post("")
def llm(
    model: str = Query("GPT"),
    sub_model: str = Query("gpt-4o-mini"),
    data: models.LLM = Body(...),
) -> models.LLMResponse:
    col = MONGO_CLIENT["ai"]["prompts"]
    prompt = col.find_one(
        {"_id": {"$eq": ObjectId(data.prompt_id)}},
        {"prompt": 1},
    )["prompt"]
    for message in prompt:
        message["content"] = message["content"].format(
            query=data.query,
            query_results="\n".join(data.query_results),
        )
    llm_model = getattr(llm, model)()
    output = llm_model(
        sub_model=sub_model,
        prompt=prompt,
    )
    return output

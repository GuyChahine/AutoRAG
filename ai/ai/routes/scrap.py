from fastapi import APIRouter

router = APIRouter(prefix="/scrap")


@router.post("/link")
def link(link: str):
    return {"page": "page..."}

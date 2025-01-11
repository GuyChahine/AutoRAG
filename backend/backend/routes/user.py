from fastapi import APIRouter, Response

from backend.models import user as models

router = APIRouter(prefix="/user")


@router.post("/create")
def create():
    return Response(status_code=501)


@router.post("/login")
def login():
    return Response(status_code=501)


@router.post("/remove")
def remove():
    return Response(status_code=501)

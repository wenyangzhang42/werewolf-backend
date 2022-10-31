from fastapi import APIRouter, Request, HTTPException

router = APIRouter()


@router.get('/')
def test():
    return {"Ping": "Pong"}

from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from models.birdspotting import BirdspottingCreate, BirdspottingRead
from repositories.birdspotting import BirdspottingRepository


router = APIRouter(prefix="/birdspotting", tags=["Birdspotting"])


def get_birdspotting_repository(
    session: Annotated[Session, Depends(get_session)],
) -> BirdspottingRepository:
    return BirdspottingRepository(session)


@router.get("/", response_model=List[BirdspottingRead])
async def get_birdspottings(
    repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]
):
    """Get all bird observations."""
    return repo.get_all()


@router.get("/{id}", response_model=BirdspottingRead)
async def get_birdspotting(
    id: int,
    repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]
):
    """Get one bird observation."""
    return repo.get_one(id)


@router.post("/", response_model=BirdspottingRead)
async def add_birdspotting(
    birdspotting: BirdspottingCreate,
    repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]
):
    """Create a bird observation."""
    return repo.insert(birdspotting)
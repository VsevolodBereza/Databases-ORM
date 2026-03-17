from typing import List, Annotated
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from database import get_session
from models.species import Species, SpeciesCreate
from repositories.species import SpeciesRepository

router = APIRouter(prefix="/species", tags=["Species"])


def get_species_repository(
    session: Annotated[Session, Depends(get_session)],
) -> SpeciesRepository:
    return SpeciesRepository(session)


@router.get("/", response_model=List[Species], status_code=status.HTTP_200_OK)
async def get_species(
    repo: Annotated[SpeciesRepository, Depends(get_species_repository)]
):
    """Get all species."""
    return repo.get_all()


@router.post("/", response_model=Species, status_code=status.HTTP_201_CREATED)
async def add_species(
    species: SpeciesCreate,
    repo: Annotated[SpeciesRepository, Depends(get_species_repository)]
):
    """Create a new species."""
    return repo.insert(species)
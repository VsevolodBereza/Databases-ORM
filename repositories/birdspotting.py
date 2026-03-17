from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from models.birds import Bird
from models.birdspotting import Birdspotting, BirdspottingCreate


class BirdspottingRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = (
            select(Birdspotting)
            .options(selectinload(Birdspotting.bird))
        )
        items = self.session.exec(statement).all()
        return items

    def get_one(self, id: int):
        statement = (
            select(Birdspotting)
            .where(Birdspotting.id == id)
            .options(selectinload(Birdspotting.bird))
        )
        item = self.session.exec(statement).first()

        if item is None:
            raise HTTPException(status_code=404, detail="Birdspotting not found")

        return item

    def insert(self, payload: BirdspottingCreate):
        bird = self.session.get(Bird, payload.bird_id)

        if bird is None:
            raise HTTPException(status_code=400, detail="Invalid bird_id")

        item = Birdspotting.model_validate(payload)
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return self.get_one(item.id)
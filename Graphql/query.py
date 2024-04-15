from typing import List

import strawberry

from service.note import NoteService
from schema import NoteType
from middleware.JWTBearer import IsAuthenticated


@strawberry.type
class Query:

    @strawberry.field
    def hello(self) -> str:
        return "Hello World!"

    @strawberry.field(permission_classes=[IsAuthenticated])
    async def get_all(self) -> List[NoteType]:
        return await NoteService.get_all_note()

    @strawberry.field(permission_classes=[IsAuthenticated])
    async def get_by_id(self, id: int) -> NoteType:
        return await NoteService.get_by_id(note_id=id)

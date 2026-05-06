from pydantic import BaseModel, PrivateAttr
from typing import ClassVar, Optional

class Uitspraak(BaseModel):
    class_name: ClassVar[str] = "fietsendiefstal"
    search_url: ClassVar[str] = "https://uitspraken.rechtspraak.nl/resultaat?zoekterm=fietsendiefstal%20utrecht&inhoudsindicatie=zt0&publicatiestatus=ps1&sort=Relevance"
    filter_query: ClassVar[str] = "Het gaat over een fietsendiefstal in Utrecht."

    conforms_to_filter_query: bool = False
    leeftijd_verdachte: Optional[int] = None

    _inhoud: str = PrivateAttr(default="")

    @property
    def inhoud(self) -> str:
        return self._inhoud

    @inhoud.setter
    def inhoud(self, value: str) -> None:
        self._inhoud = value

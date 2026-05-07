from pydantic import BaseModel
from typing import ClassVar, Optional

class Uitspraak(BaseModel):
    class_name: ClassVar[str] = "fietsendiefstal"
    search_url: ClassVar[str] = "https://uitspraken.rechtspraak.nl/resultaat?zoekterm=explosief&inhoudsindicatie=zt0&publicatiestatus=ps1&sort=Relevance&rechtsgebied=r3&uitspraak=ud3"
    filter_query: ClassVar[str] = "Het gaat over het plaatsen van een explosief of vuurwerkbom bij een woning of bedrijfspand."

    zaak_nr: str = ""
    inhoud: str = ""
    conforms_to_filter_query: bool = False
    leeftijd_verdachte: Optional[int] = None

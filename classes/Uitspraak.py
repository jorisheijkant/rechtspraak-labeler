from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Uitspraak:
    class_name: str | "fietsendiefstal"
    search_url: str | "https://uitspraken.rechtspraak.nl/resultaat?zoekterm=fietsendiefstal%20utrecht&inhoudsindicatie=zt0&publicatiestatus=ps1&sort=Relevance"
    conforms_to_filter_query: bool | True
    inhoud: str
    leeftijd_verdachte: Optional[int] = None


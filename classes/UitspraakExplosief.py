from pydantic import BaseModel
from typing import ClassVar, Optional

class UitspraakExplosief(BaseModel):
    class_name: ClassVar[str] = "explosief"
    search_url: ClassVar[str] = "https://uitspraken.rechtspraak.nl/resultaat?zoekterm=explosief&inhoudsindicatie=zt0&publicatiestatus=ps1&sort=Relevance&rechtsgebied=r3&uitspraak=ud3,ud4"
    filter_query: ClassVar[str] = "Het gaat over het plaatsen van een explosief of vuurwerkbom bij een woning of bedrijfspand, of over bemiddelingen daarbij."

    zaak_nr: str = ""
    inhoud: str = ""
    conforms_to_filter_query: bool = False

    leeftijd_verdachte: Optional[int] = 0
    aantal_aanslagen: Optional[int] = 1 
    doelwit_type: Optional[str] = ""
    aanslag_uitgevoerd: Optional[bool] = True
    strafeis: Optional[str] = ""
    opgelegde_straf: Optional[str] = ""


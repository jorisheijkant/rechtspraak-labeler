from pydantic import BaseModel
from typing import ClassVar, Optional

class UitspraakDetentieMarokko(BaseModel):
    class_name: ClassVar[str] = "detentie_marokko"
    search_url: ClassVar[str] = "https://uitspraken.rechtspraak.nl/resultaat?uitspraakdatuma=01-06-2021&uitspraakdatumb=05-05-2026&uitspraakdatumrange=tussen&zoekterm=marokko%20EN%20detentie&inhoudsindicatie=zt0&publicatiestatus=ps1&sort=Relevance"
    filter_query: ClassVar[str] = "Het gaat over iemand uit Marokko die in vreemdelingendetentie is geplaatst."

    zaak_nr: str = ""
    inhoud: str = ""
    conforms_to_filter_query: bool = False

    leeftijd_verdachte: Optional[int] = 0
    datum_van_uitspraak: Optional[str] = ""
    geworteldheid: Optional[bool] = False 
    verblijfsduur_in_nl_in_jaren: Optional[int] = 0 
    familie_in_nederland: Optional[bool] = False 
    school_studie_werk_in_nl: Optional[bool] = False 


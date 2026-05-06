from pydantic import BaseModel

def get_uitspraak_schema(uitspraak_class: type[BaseModel]) -> dict:
    return uitspraak_class.model_json_schema()

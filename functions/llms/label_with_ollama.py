import ollama
from pydantic import BaseModel

from functions.llms.get_uitspraak_schema import get_uitspraak_schema

def label_with_ollama(prompt: str, content: str, uitspraak_class: type[BaseModel], model: str = "gemma4") -> BaseModel:
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": f"{prompt}\n\n{content}"}],
        format=get_uitspraak_schema(uitspraak_class)
    )

    raw = response['message']['content'] if isinstance(response, dict) else response.message.content
    return uitspraak_class.model_validate_json(raw)

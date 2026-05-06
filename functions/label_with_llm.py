from pydantic import BaseModel

from functions.llms.label_with_anthropic import label_with_anthropic
from functions.llms.label_with_ollama import label_with_ollama
from variables.prompt import prompt

def label_with_llm(uitspraak: BaseModel, provider: str = "anthropic") -> BaseModel:
    uitspraak_class = type(uitspraak)
    if provider == "anthropic":
        return label_with_anthropic(prompt, uitspraak.inhoud, uitspraak_class)
    if provider == "ollama":
        return label_with_ollama(prompt, uitspraak.inhoud, uitspraak_class)
    raise ValueError(f"Unknown provider: {provider}")

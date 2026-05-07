from pydantic import BaseModel

from functions.llms.label_with_anthropic import label_with_anthropic
from functions.llms.label_with_ollama import label_with_ollama


def label_with_llm(uitspraak: BaseModel, provider: str = "anthropic", prompt: str = "") -> BaseModel:
    uitspraak_class = type(uitspraak)
    if provider == "anthropic":
        labeled = label_with_anthropic(prompt, uitspraak.inhoud, uitspraak_class)
    elif provider == "ollama":
        labeled = label_with_ollama(prompt, uitspraak.inhoud, uitspraak_class)
    else:
        raise ValueError(f"Unknown provider: {provider}")
    labeled.inhoud = uitspraak.inhoud
    return labeled

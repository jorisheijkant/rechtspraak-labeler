from functions.llms.label_with_anthropic import label_with_anthropic
from functions.llms.label_with_ollama import label_with_ollama
from variables.prompt import prompt 

def label_with_llm(uitspraak, provider="anthropic"):
    if provider == "anthropic":
        return label_with_anthropic(prompt, uitspraak.inhoud)
    if provider == "ollama":
        return label_with_ollama(prompt, uitspraak.inhoud)
    raise ValueError(f"Unknown provider: {provider}")

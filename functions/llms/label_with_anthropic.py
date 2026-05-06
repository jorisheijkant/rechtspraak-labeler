import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

def label_with_anthropic(prompt: str, content: str, uitspraak_class: type[BaseModel]) -> BaseModel:
    client = anthropic.Anthropic()

    response = client.messages.parse(
        model="claude-opus-4-7",
        max_tokens=2048,
        system=prompt,
        messages=[{"role": "user", "content": content}],
        output_format=uitspraak_class,
    )

    return response.parsed_output

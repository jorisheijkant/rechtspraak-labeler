
import anthropic
from dotenv import load_dotenv

from functions.llms.uitspraak_schema import get_uitspraak_schema

load_dotenv()

def label_with_anthropic(prompt, pdf_content):
    client = anthropic.Anthropic()

    print(f"PDF naar Claude sturen...")

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\n{pdf_content}"
            }
        ],
        output_config={
            "format": {
                "type": "json_schema",
                "schema": get_uitspraak_schema()
            }
        }
    )

    return response.content[0].text

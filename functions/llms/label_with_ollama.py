import ollama

from functions.llms.uitspraak_schema import get_uitspraak_schema

def label_with_ollama(prompt, pdf_content, model="llama3.2"):
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\n{pdf_content}"
            }
        ],
        format=get_uitspraak_schema()
    )

    return response.message.content

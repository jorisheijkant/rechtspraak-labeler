import pandas as pd
from tqdm import tqdm

from classes.Uitspraak import Uitspraak
from functions.label_with_llm import label_with_llm
from variables.prompt import prompt

uitspraken_file = "data/uitspraken.csv"
output_file = "data/uitspraken_labeled.csv"
llm_provider = "ollama"
max_to_label = 50 # Set to None for full list labeling

scraped_uitspraken = pd.read_csv(uitspraken_file, na_filter=False)
uitspraken = [Uitspraak(**row.to_dict()) for _, row in scraped_uitspraken.iterrows()]

labeled_uitspraken = []
for uitspraak in tqdm(uitspraken[:max_to_label], desc="Labeling uitspraken", unit="uitspraak"):
    labeled_uitspraken.append(label_with_llm(uitspraak, provider=llm_provider, prompt=prompt_explosieven))
    pd.DataFrame([u.model_dump() for u in labeled_uitspraken]).to_csv(output_file, index=False)

if labeled_uitspraken:
    print(f"Saved {len(labeled_uitspraken)} labeled uitspraken to {output_file}")

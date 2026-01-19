# Run this once to create the folder locally
from datasets import load_dataset
dataset = load_dataset("imdb")
subset = dataset["train"].shuffle(seed=42).select(range(500))
subset.save_to_disk("imdb_subset")
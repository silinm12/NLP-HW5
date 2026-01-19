import sys
import os
from datasets import load_from_disk, load_dataset

def load_data(path_to_subset):
    # Requirement from Part A
    if os.path.exists(path_to_subset):
        print(f"Loading data from disk: {path_to_subset}")
        return load_from_disk(path_to_subset)
    else:
        print("Data not found on disk. Downloading and creating subset...")
        dataset = load_dataset("imdb")
        # Ensure you use the exact same seed/range as instructed in Part A
        subset = dataset["train"].shuffle(seed=42).select(range(500))
        subset.save_to_disk(path_to_subset)
        return subset

#part C


if __name__ == "__main__":
    # Example for Part B
    subset_path = sys.argv[1] # The TA will provide the path here [cite: 272]
    dataset = load_data(subset_path)
    # ... rest of your code ...
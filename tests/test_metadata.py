from src.metadata.generator import generate_metadata

metadata = generate_metadata("Processed Data")

print(f"Total Records : {len(metadata)}")

print()

print(metadata[0])
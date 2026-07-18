from src.metadata.generator import generate_metadata
from src.metadata.writer import write_metadata

metadata = generate_metadata("Processed Data")

write_metadata(metadata, "metadata.csv")

print("Metadata CSV created successfully!")

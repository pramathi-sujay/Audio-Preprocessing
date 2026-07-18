from src.metadata.generator import generate_metadata
from src.metadata.writer import write_metadata


PROCESSED_DATASET = "Renamed Data"
OUTPUT_FILE = "metadata.csv"


def main():

    metadata = generate_metadata(PROCESSED_DATASET)

    write_metadata(metadata, OUTPUT_FILE)

    print("\n===== METADATA GENERATION COMPLETE =====")
    print(f"Total Records : {len(metadata)}")
    print(f"Output File   : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
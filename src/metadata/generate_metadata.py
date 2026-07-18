from .config import DATASET_DIR, OUTPUT_FILE
from .generator import generate_metadata
from .splitter import add_dataset_split
from .writer import write_metadata


def main():

    metadata = generate_metadata(DATASET_DIR)

    metadata_df = add_dataset_split(metadata)

    write_metadata(metadata_df, OUTPUT_FILE)

    print("\nMetadata generation completed successfully!")


if __name__ == "__main__":
    main()
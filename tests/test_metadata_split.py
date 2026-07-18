import pandas as pd

from src.metadata.config import OUTPUT_FILE


def main():

    # Load metadata
    metadata = pd.read_csv(OUTPUT_FILE)

    print("\nTesting Metadata Split")
    print("-" * 40)

    # -------------------------
    # Check split column exists
    # -------------------------
    assert "split" in metadata.columns, \
        "'split' column not found."

    print("✓ Split column exists")

    # -------------------------
    # Check for missing values
    # -------------------------
    assert metadata["split"].isnull().sum() == 0, \
        "Missing values found in split column."

    print("✓ No missing values")

    # -------------------------
    # Check allowed values
    # -------------------------
    valid_splits = {"train", "validation", "test"}

    actual_splits = set(metadata["split"].unique())

    assert actual_splits.issubset(valid_splits), \
        "Invalid split values detected."

    print("✓ Split values are valid")

    # -------------------------
    # Overall distribution
    # -------------------------
    print("\nOverall Dataset Split")

    split_counts = metadata["split"].value_counts()

    total = len(metadata)

    for split in ["train", "validation", "test"]:

        count = split_counts.get(split, 0)

        percentage = (count / total) * 100

        print(f"{split:<12}: {count:>5} ({percentage:.2f}%)")

    # -------------------------
    # Class-wise distribution
    # -------------------------
    print("\nClass-wise Split")
    print("-" * 40)

    class_distribution = pd.crosstab(
        metadata["label"],
        metadata["split"]
    )

    print(class_distribution)

    print("\n✓ Metadata split test passed successfully!")


if __name__ == "__main__":
    main()
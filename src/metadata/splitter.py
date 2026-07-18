import pandas as pd
from sklearn.model_selection import train_test_split

from .config import (
    TRAIN_RATIO,
    VALIDATION_RATIO,
    TEST_RATIO,
    RANDOM_SEED,
)


def add_dataset_split(metadata):
    """
    Adds a stratified train/validation/test split
    to the metadata.

    Returns:
        pandas.DataFrame
    """

    df = pd.DataFrame(metadata)

    # First split into Train and Temp
    train_df, temp_df = train_test_split(
        df,
        test_size=(1 - TRAIN_RATIO),
        stratify=df["label"],
        random_state=RANDOM_SEED,
    )

    # Split Temp into Validation and Test
    val_ratio = VALIDATION_RATIO / (VALIDATION_RATIO + TEST_RATIO)

    validation_df, test_df = train_test_split(
        temp_df,
        test_size=(1 - val_ratio),
        stratify=temp_df["label"],
        random_state=RANDOM_SEED,
    )

    train_df["split"] = "train"
    validation_df["split"] = "validation"
    test_df["split"] = "test"

    final_df = pd.concat(
        [train_df, validation_df, test_df],
        ignore_index=True,
    )

    return final_df
"""
rename_dataset.py

Renames all audio files in the dataset using a
standardized naming convention.
"""

from pathlib import Path
import shutil

from .config import (
    INPUT_DIR,
    OUTPUT_DIR,
    SUPPORTED_AUDIO_FORMATS,
)

from .renamer import generate_filename


def rename_dataset():
    """
    Rename every audio file in the dataset.
    """

    print("=" * 50)
    print("RENAMING DATASET")
    print("=" * 50)

    total_files = 0

    for environment_dir in sorted(INPUT_DIR.iterdir()):

        if not environment_dir.is_dir():
            continue

        for class_dir in sorted(environment_dir.iterdir()):

            if not class_dir.is_dir():
                continue

            file_number = 1

            output_class_dir = (
                OUTPUT_DIR /
                environment_dir.name /
                class_dir.name
            )

            output_class_dir.mkdir(
                parents=True,
                exist_ok=True,
            )

            audio_files = sorted(
                file
                for file in class_dir.iterdir()
                if file.suffix.lower() in SUPPORTED_AUDIO_FORMATS
            )

            for audio_file in audio_files:

                new_filename = generate_filename(
                    class_dir.name,
                    file_number,
                    audio_file.suffix.lower(),
                )

                destination = output_class_dir / new_filename

                shutil.copy2(
                    audio_file,
                    destination,
                )

                file_number += 1
                total_files += 1

    print("\nRenaming Complete!")
    print(f"\nTotal Files Renamed : {total_files}")


if __name__ == "__main__":
    rename_dataset()
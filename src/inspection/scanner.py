from pathlib import Path

from src.utils.constants import SUPPORTED_AUDIO_FORMATS


def scan_dataset(dataset_path: str) -> dict:
    """
    Scan a dataset and collect information about all class folders.

    Args:
        dataset_path (str): Path to the dataset root.

    Returns:
        dict: Dataset information.
    """

    dataset = Path(dataset_path)

    if not dataset.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset}")

    classes = []
    empty_classes = []

    total_audio_files = 0
    dataset_formats = {}

    for folder in sorted(dataset.rglob("*")):

        if not folder.is_dir():
            continue

        # Check if the folder is a leaf folder
        subfolders = [item for item in folder.iterdir() if item.is_dir()]
        is_leaf_folder = len(subfolders) == 0

        # Get all supported audio files in the folder
        audio_files = sorted(
            file
            for file in folder.iterdir()
            if file.is_file()
            and file.suffix.lower() in SUPPORTED_AUDIO_FORMATS
        )

        # Empty class
        if is_leaf_folder and len(audio_files) == 0:
            empty_classes.append(folder.name)
            continue

        # Ignore intermediate folders
        if len(audio_files) == 0:
            continue

        # Count formats for this class
        class_formats = {}

        for file in audio_files:

            extension = file.suffix.lower()

            class_formats[extension] = class_formats.get(extension, 0) + 1
            dataset_formats[extension] = dataset_formats.get(extension, 0) + 1

        total_audio_files += len(audio_files)

        classes.append(
            {
                "name": folder.name,
                "path": folder,
                "num_files": len(audio_files),
                "formats": class_formats,
                "files": audio_files,
            }
        )

    return {
        "dataset_name": dataset.name,
        "dataset_path": dataset,
        "total_classes": len(classes),
        "total_audio_files": total_audio_files,
        "audio_formats": dataset_formats,
        "empty_classes": sorted(empty_classes),
        "classes": classes,
    }
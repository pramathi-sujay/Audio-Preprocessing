import csv
from pathlib import Path


def write_metadata(metadata, output_file):

    output_file = Path(output_file)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "filepath",
        "label",
        "environment",
        "duration",
    ]

    with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(metadata)
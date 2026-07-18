import csv


def write_metadata(dataframe, output_file):
    """
    Writes the metadata dataframe to CSV.
    """

    fieldnames = [
        "filename",
        "filepath",
        "label",
        "environment",
        "duration (in seconds)",
        "split",
    ]

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(
            dataframe.to_dict(orient="records")
        )

    print(f"\nMetadata saved to {output_file}")
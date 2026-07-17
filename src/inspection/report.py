def generate_report(dataset: dict) -> str:
    """
    Generate a human-readable inspection report.

    Args:
        dataset (dict): Dataset information returned by scan_dataset().

    Returns:
        str: Formatted inspection report.
    """

    lines = []

    lines.append("=" * 50)
    lines.append("        DATASET INSPECTION REPORT")
    lines.append("=" * 50)
    lines.append("")

    lines.append(f"Dataset Name      : {dataset['dataset_name']}")
    lines.append(f"Dataset Path      : {dataset['dataset_path']}")
    lines.append("")

    lines.append(f"Total Classes     : {dataset['total_classes']}")
    lines.append(f"Total Audio Files : {dataset['total_audio_files']}")
    lines.append("")

    lines.append("Audio Formats")
    lines.append("-" * 50)

    for extension, count in dataset["audio_formats"].items():
        lines.append(f"{extension:<5}: {count}")

    lines.append("")

    lines.append("Empty Classes")
    lines.append("-" * 50)

    if dataset["empty_classes"]:
        for folder in dataset["empty_classes"]:
            lines.append(f"- {folder}")
    else:
        lines.append("None")

    lines.append("")

    lines.append("Classes")
    lines.append("-" * 50)

    for cls in dataset["classes"]:

        lines.append(cls["name"])
        lines.append(f"  Files   : {cls['num_files']}")
        lines.append("  Formats :")

        for extension, count in cls["formats"].items():
            lines.append(f"    {extension:<5}: {count}")

        lines.append("")

    lines.append("=" * 50)
    lines.append("Inspection Complete")
    lines.append("=" * 50)

    return "\n".join(lines)
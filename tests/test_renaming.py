"""
Test the filename generation logic.
"""

from src.renaming.renamer import generate_filename


def main():

    print("=" * 50)
    print("RENAMING MODULE TEST")
    print("=" * 50)

    test_cases = [
        ("Baby Crying", 1),
        ("Door knocking", 12),
        ("DoorBell", 3),
        ("Fire-Smoke alarms", 7),
        ("Glass Breaking", 25),
        ("Mixer- Grinder", 15),
        ("Pressure Cooker", 2),
        ("Water Running", 101),
        ("Train_Horn", 42),
        ("Vehicle Horn", 9),
    ]

    for class_name, number in test_cases:

        filename = generate_filename(class_name, number)

        print(f"{class_name:<25} -> {filename}")


if __name__ == "__main__":
    main()
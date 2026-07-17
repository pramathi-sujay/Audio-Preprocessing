from src.inspection.report import generate_report
from src.inspection.scanner import scan_dataset


def main():

    dataset = scan_dataset("Data Collection")

    report = generate_report(dataset)

    print(report)


if __name__ == "__main__":
    main()
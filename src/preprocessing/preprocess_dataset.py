from pathlib import Path

from src.preprocessing.loader import load_audio
from src.preprocessing.mono import convert_to_mono
from src.preprocessing.resampler import resample_audio
from src.preprocessing.normalizer import normalize_audio
from src.preprocessing.silence import trim_silence
from src.preprocessing.saver import save_audio

from src.utils.constants import SUPPORTED_AUDIO_FORMATS


RAW_DATASET = Path("Data Collection")
PROCESSED_DATASET = Path("Processed Data")


def preprocess_dataset():

    total_files = 0
    processed_files = 0
    failed_files = 0

    for audio_file in sorted(RAW_DATASET.rglob("*")):

        if not audio_file.is_file():
            continue

        if audio_file.suffix.lower() not in SUPPORTED_AUDIO_FORMATS:
            continue

        total_files += 1

        print(f"[{total_files}] Processing: {audio_file}")

        try:

            # Load
            waveform, sample_rate = load_audio(audio_file)

            # Convert to mono
            waveform = convert_to_mono(waveform)

            # Resample
            waveform, sample_rate = resample_audio(
                waveform,
                sample_rate
            )

            # Normalize
            waveform = normalize_audio(waveform)

            # Trim Silence
            waveform = trim_silence(waveform)

            # Preserve folder structure
            relative_path = audio_file.relative_to(RAW_DATASET)

            output_path = (
                PROCESSED_DATASET /
                relative_path.parent /
                f"{audio_file.stem}.wav"
            )

            # Save
            save_audio(
                output_path,
                waveform,
                sample_rate
            )

            processed_files += 1

        except Exception as error:

            failed_files += 1
            print(f"Failed : {audio_file}")
            print(error)
            print()

    print("\n========================================")
    print("PREPROCESSING COMPLETE")
    print("========================================")
    print(f"Total Files     : {total_files}")
    print(f"Processed Files : {processed_files}")
    print(f"Failed Files    : {failed_files}")
    print(f"Output Folder   : {PROCESSED_DATASET}")
    print("========================================")


def main():
    preprocess_dataset()


if __name__ == "__main__":
    main()
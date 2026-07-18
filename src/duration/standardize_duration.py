"""
standardize_duration.py

Standardizes the duration of all audio files in the processed dataset.
"""

from pathlib import Path

import librosa

from .analyzer import analyze_duration, DurationAction
from .splitter import split_audio
from .saver import save_audio


INPUT_DIR = Path("Processed Data")
OUTPUT_DIR = Path("Duration Standardized Data")


def process_dataset():

    flagged_files = []

    audio_files = sorted(INPUT_DIR.rglob("*.wav"))

    print("=" * 50)
    print("STANDARDIZING AUDIO DURATIONS")
    print("=" * 50)

    for audio_path in audio_files:

        relative_path = audio_path.relative_to(INPUT_DIR)

        action, duration = analyze_duration(audio_path)

        audio, sample_rate = librosa.load(audio_path, sr=None, mono=False)

        output_folder = OUTPUT_DIR / relative_path.parent

        if action == DurationAction.KEEP:

            output_path = output_folder / audio_path.name
            save_audio(audio, sample_rate, output_path)

        elif action == DurationAction.SPLIT:

            clips = split_audio(audio, sample_rate)

            stem = audio_path.stem

            for i, clip in enumerate(clips, start=1):

                output_path = output_folder / f"{stem}_clip_{i:03d}.wav"

                save_audio(clip, sample_rate, output_path)

        elif action == DurationAction.FLAG:

            flagged_files.append((audio_path, duration))

            output_path = output_folder / audio_path.name
            save_audio(audio, sample_rate, output_path)

    print("\nDuration Standardization Complete!")

    print(f"\nTotal Files : {len(audio_files)}")
    print(f"Flagged Files : {len(flagged_files)}")

    if flagged_files:

        print("\nFlagged Audio Files")

        for path, duration in flagged_files:

            print(f"{path} ({duration:.2f} sec)")


if __name__ == "__main__":
    process_dataset()
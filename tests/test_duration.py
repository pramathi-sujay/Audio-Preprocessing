from pathlib import Path

from src.duration.analyzer import analyze_duration
from src.duration.splitter import split_audio
import librosa


TEST_FILE = Path(
    "Processed Data/Indoor/Baby Crying/bahyudinnor-heartbreaking-baby-crying-sound-effect-realistic-amp-high-quality-311648.wav"
)


def main():

    print("=" * 50)
    print("DURATION MODULE TEST")
    print("=" * 50)

    action, duration = analyze_duration(TEST_FILE)

    print(f"File      : {TEST_FILE.name}")
    print(f"Duration  : {duration:.2f} sec")
    print(f"Action    : {action.value}")

    audio, sample_rate = librosa.load(
        TEST_FILE,
        sr=None,
        mono=True,
    )

    clips = split_audio(audio, sample_rate)

    print(f"\nGenerated {len(clips)} clip(s)\n")

    for i, clip in enumerate(clips, start=1):

        clip_duration = len(clip) / sample_rate

        print(f"Clip {i:03d}: {clip_duration:.2f} sec")


if __name__ == "__main__":
    main()
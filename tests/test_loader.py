from pathlib import Path

from src.preprocessing.loader import load_audio


folder = Path("Data Collection/Indoor/Baby Crying")

audio_file = next(folder.glob("*"))

audio, sr = load_audio(audio_file)

print(audio.shape)
print(sr)
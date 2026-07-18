from pathlib import Path

import soundfile as sf

from src.utils.constants import SUPPORTED_AUDIO_FORMATS


def generate_metadata(dataset_path):

    dataset_path = Path(dataset_path)

    metadata = []

    for audio_file in sorted(dataset_path.rglob("*")):

        if not audio_file.is_file():
            continue

        if audio_file.suffix.lower() not in SUPPORTED_AUDIO_FORMATS:
            continue

        audio_info = sf.info(audio_file)

        relative_path = audio_file.relative_to(dataset_path)

        environment = relative_path.parts[0]

        label = relative_path.parts[1]

        duration = round(audio_info.duration, 2)

        metadata.append(
            {
                "filename": audio_file.name,
                "filepath": relative_path.as_posix(),
                "label": label,
                "environment": environment,
                "duration (in seconds)": duration,
            }
        )

    return metadata
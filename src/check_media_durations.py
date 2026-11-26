import subprocess
from pathlib import Path

folders = {
    "NARRATION": Path("assets/narration"),
    "VIDEO": Path("assets/video")
}

for category, folder in folders.items():
    print(f"\n========== {category} ==========")

    for file in sorted(folder.glob("*.mp3" if category == "NARRATION" else "*.mp4")):
        result = subprocess.run(
            [
                "ffprobe",
                "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                str(file)
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0 and result.stdout.strip():
            duration = float(result.stdout.strip())
            print(f"{file.name}: {duration:.2f} seconds")
        else:
            print(f"Could not read: {file.name}")
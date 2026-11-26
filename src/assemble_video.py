
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_DIR = ROOT / "assets" / "video"
LIST_FILE = VIDEO_DIR / "concat_list.txt"
TEMP_DIR = ROOT / "temp" / "normalized"
OUTPUT_DIR = ROOT / "output"

TEMP_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Read the final scene filenames
scene_files = []

for line in LIST_FILE.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if line.startswith("file '") and line.endswith("'"):
        scene_files.append(line[6:-1])

if len(scene_files) != 10:
    raise ValueError(f"Expected 10 scenes, found {len(scene_files)}")

normalized_files = []

for index, filename in enumerate(scene_files, start=1):
    source = VIDEO_DIR / filename

    if not source.exists():
        raise FileNotFoundError(f"Missing scene: {source}")

    destination = TEMP_DIR / f"scene_{index:02d}.mp4"

    print(f"Preparing scene {index}/10: {filename}")

    command = [
        "ffmpeg", "-y",
        "-i", str(source),
        "-vf",
        "scale=1920:1080:force_original_aspect_ratio=decrease,"
        "pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
        "setsar=1,fps=24",
        "-an",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        str(destination)
    ]

    subprocess.run(command, check=True)
    normalized_files.append(destination)

# Create a temporary FFmpeg concat list
concat_file = TEMP_DIR / "normalized_list.txt"

with concat_file.open("w", encoding="utf-8") as file:
    for video in normalized_files:
        safe_path = video.resolve().as_posix().replace("'", "'\\''")
        file.write(f"file '{safe_path}'\n")

# Join the normalized clips
final_video = OUTPUT_DIR / "the_waiting_mother_landscape.mp4"

subprocess.run([
    "ffmpeg", "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", str(concat_file),
    "-c", "copy",
    "-movflags", "+faststart",
    str(final_video)
], check=True)

print("\nLANDSCAPE VIDEO ASSEMBLED SUCCESSFULLY")
print(f"Output: {final_video}")

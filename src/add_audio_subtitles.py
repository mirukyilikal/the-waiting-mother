
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VIDEO = ROOT / "output" / "the_waiting_mother_landscape.mp4"
AUDIO_DIR = ROOT / "assets" / "narration"
MUSIC = ROOT / "assets" / "music" / "background_music.mp3"
SUBTITLES = ROOT / "script" / "english_subtitles.srt"
OUTPUT = ROOT / "output" / "the_waiting_mother_final.mp4"

NARRATION = [
    ("S01_narration.mp3", 0),
    ("S02_narration.mp3", 7),
    ("S03_narration.mp3", 15),
    ("S04_narration.mp3", 23),
    ("S05_narration.mp3", 31),
    ("S06_narration.mp3", 39),
    ("S08_narration.mp3", 55),
    ("S09_narration.mp3", 64),
    ("S10_narration.mp3", 74),
]

for path in [VIDEO, MUSIC, SUBTITLES]:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

for filename, _ in NARRATION:
    path = AUDIO_DIR / filename
    if not path.exists() or path.stat().st_size == 0:
        raise FileNotFoundError(f"Missing or empty narration: {path}")

# Add video, narration tracks, and background music.
command = ["ffmpeg", "-y", "-i", str(VIDEO)]

for filename, _ in NARRATION:
    command += ["-i", str(AUDIO_DIR / filename)]

command += ["-stream_loop", "-1", "-i", str(MUSIC)]

filters = []
audio_labels = []

for index, (filename, start_seconds) in enumerate(NARRATION, start=1):
    delay_ms = start_seconds * 1000
    label = f"voice{index}"

    filters.append(
        f"[{index}:a]asetpts=PTS-STARTPTS,"
        f"aresample=24000,"
        f"adelay=delays={delay_ms}:all=1,"
        f"apad=whole_dur=80,"
        f"volume=1.0[{label}]"
    )

    audio_labels.append(f"[{label}]")

# Mix all narration tracks.
filters.append(
    "".join(audio_labels)
    + f"amix=inputs={len(audio_labels)}:"
    + "duration=longest:dropout_transition=0:normalize=0,"
    + "alimiter=limit=0.95[narration]"
)

# Prepare quiet background music with fade-in and fade-out.
music_index = len(NARRATION) + 1

filters.append(
    f"[{music_index}:a]aresample=24000,"
    "atrim=0:80,"
    "asetpts=PTS-STARTPTS,"
    "volume=0.12,"
    "afade=t=in:st=0:d=3,"
    "afade=t=out:st=74:d=6[music]"
)

# Combine narration and background music.
filters.append(
    "[narration][music]"
    "amix=inputs=2:duration=longest:normalize=0,"
    "alimiter=limit=0.95,"
    "atrim=0:80[audio]"
)

subtitle_path = SUBTITLES.resolve().as_posix().replace(":", r"\:")

filters.append(
    f"[0:v]subtitles='{subtitle_path}':"
    "force_style='FontName=Arial,FontSize=22,"
    "PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
    "BorderStyle=1,Outline=2,Shadow=1,Alignment=2,"
    "MarginV=45'[video]"
)

command += [
    "-filter_complex", ";".join(filters),
    "-map", "[video]",
    "-map", "[audio]",
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "20",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    "-t", "80",
    "-movflags", "+faststart",
    str(OUTPUT),
]

print("Building final video with narration, subtitles, and background music...")
subprocess.run(command, check=True)

print("\nFINAL VIDEO CREATED SUCCESSFULLY")
print(f"Output: {OUTPUT}")

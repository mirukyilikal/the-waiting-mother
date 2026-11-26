
import json
import asyncio
from pathlib import Path
import edge_tts

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_FILE = PROJECT_ROOT / "script" / "narration.json"
OUTPUT_DIR = PROJECT_ROOT / "assets" / "narration"


async def generate_line(voice, line):
    output_file = OUTPUT_DIR / f"{line['id']}_narration.mp3"

    if output_file.exists() and output_file.stat().st_size > 0:
        print(f"Skipped (already exists): {output_file.name}")
        return

    for attempt in range(1, 4):
        try:
            communicate = edge_tts.Communicate(
                text=line["text"],
                voice=voice,
                rate="-5%",
                pitch="+0Hz"
            )

            await communicate.save(str(output_file))

            if output_file.exists() and output_file.stat().st_size > 0:
                print(f"Generated: {output_file.name}")
                return

        except Exception as error:
            print(f"Attempt {attempt} failed for {line['id']}: {error}")

        if output_file.exists():
            output_file.unlink()

        if attempt < 3:
            await asyncio.sleep(10)

    raise RuntimeError(f"Could not generate narration for {line['id']}")


async def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with SCRIPT_FILE.open("r", encoding="utf-8") as file:
        script = json.load(file)

    voice = script["voice"]

    for line in script["lines"]:
        await generate_line(voice, line)

    print("\nAll narration recordings generated successfully.")


if __name__ == "__main__":
    asyncio.run(main())

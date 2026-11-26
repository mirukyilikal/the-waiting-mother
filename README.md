# The Waiting Mother

An AI-assisted short film about a fictional Ethiopian mother who waits outside her home for her daughter to return from school.

## 1. Project Overview

**Film title:** The Waiting Mother  
**Language:** Amharic  
**Subtitles:** English  
**Story duration:** 80 seconds  
**Final duration with AI disclosure card:** 84 seconds  
**Video formats:** Landscape (16:9) and Portrait (9:16)  
**Setting:** A fictional rural Ethiopian village  

## 2. Creative Intent

The Waiting Mother explores the quiet expression of maternal love through waiting, patience, care, and welcoming a child home.

The story follows a mother who waits outside her home every afternoon for her daughter to return from school. When the daughter asks why she waits, the mother explains that she wants her child to always know that someone will welcome her home with love.

The intended audience is Ethiopian young people and families. The film aims to encourage reflection on family relationships, gratitude, and the importance of a mother's love.

## 3. Tools and Technologies

- **Python:** Pipeline scripts and automation.
- **FFmpeg:** Video processing, editing, audio mixing, and exporting.
- **Edge TTS:** Synthetic Amharic narration using the `am-ET-MekdesNeural` voice.
- **AI image generation:** Creation of fictional characters and visual scenes.
- **AI video generation:** Generation of selected scene clips.
- **Pixabay:** Background music.
- **English SRT subtitles:** English translation of the Amharic narration.

## 4. Project Structure

```text
the-waiting-mother/
│
├── assets/
│   ├── narration/
│   ├── video/
│   ├── music/
│   └── endcard/
│
├── cache/
├── output/
├── outputs/
├── script/
├── src/
│   ├── assemble_video.py
│   ├── generate_narration.py
│   ├── add_audio_subtitles.py
│   ├── validate_storyboard.py
│   └── check_media_durations.py
│
├── tests/
├── temp/
├── storyboard.json
├── runs.jsonl
├── requirements.txt
└── README.md
```

## 5. Setup and Installation

### Requirements

- Python 3.11
- FFmpeg installed and available in the system PATH
- Internet connection for online text-to-speech generation

### Create a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
pip install -r requirements.txt
```

## 6. Running the Current Pipeline

### Step 1: Validate the storyboard

```powershell
python src/validate_storyboard.py
```

This checks that the storyboard is valid JSON, contains shots, and has continuous timing without gaps or overlaps.

### Step 2: Generate narration

```powershell
python src/generate_narration.py
```

The script reads narration data from `script/narration.json` and generates Amharic audio files in `assets/narration/`.

Existing non-empty narration files are skipped, avoiding unnecessary regeneration. Failed generation attempts are retried.

### Step 3: Assemble landscape scenes

Prepare the scene list in `assets/video/concat_list.txt`, then run:

```powershell
python src/assemble_video.py
```

This normalizes and combines the scene clips into a landscape video.

### Step 4: Add narration, music, and subtitles

```powershell
python src/add_audio_subtitles.py
```

This combines the landscape video with narration, background music, and English subtitles.

### Step 5: Export final formats

The final video exports are:

- `output/the_waiting_mother_with_endcard.mp4`
- `output/the_waiting_mother_vertical.mp4`

The end card and portrait version are currently produced through separate FFmpeg processing steps.

## 7. Final Deliverables

The project includes:

- An 84-second landscape film (16:9).
- An 84-second portrait film (9:16).
- Amharic synthetic narration.
- English subtitles.
- Background music.
- An AI disclosure end card.

## 8. Current Limitations

Some parts of the production workflow are not yet fully automated.

- The complete production workflow is not yet controlled by one command.
- The current storyboard validator checks JSON structure and shot timing but does not yet implement full JSON Schema validation.
- Historical model-call metadata, including exact model versions, parameters, seeds, latency, and costs, was not fully recorded.
- Automated test coverage is not yet complete.
- A verified per-shot selective regeneration system has not yet been implemented.
- The background music was obtained from Pixabay and is not an original musical composition.
- The current music mix uses a fixed volume level rather than automated voice ducking.

These limitations are documented transparently rather than presented as completed features.

## 9. Responsible AI and Disclosure

The film uses fictional AI-generated characters and synthetic narration. It does not intentionally depict a real mother or daughter.

An AI disclosure card is included at the end of the film to communicate the use of AI-assisted production.

Before public distribution, the applicable licences and usage permissions for generated visuals, video clips, narration, and third-party music must be checked.

## 10. Future Improvements

Future development will focus on:

- Implementing complete JSON Schema validation.
- Creating a single-command production workflow.
- Adding per-shot caching and selective regeneration.
- Recording model-call metadata automatically.
- Improving automated testing.
- Creating an original musical score with automated voice ducking.
- Improving reproducibility and production documentation.

Project: The Waiting Mother
Category: AI-Content Generation — The Heritage Short

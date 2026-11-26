# Architecture — The Waiting Mother

## 1. Overview

The Waiting Mother is an AI-assisted short-film production project. It uses a storyboard-driven workflow to organize the story, generate visual and audio assets, and assemble the final film.

Python scripts manage the production steps, while FFmpeg handles video processing and final media assembly.

## 2. System Architecture

The project follows a staged production pipeline:

1. Storyboard definition
2. Storyboard validation
3. Visual asset generation
4. Narration generation
5. Scene assembly
6. Audio and subtitle integration
7. Final video export

## 3. Shared Contract: storyboard.json

The `storyboard.json` file is the central description of the film.

It defines:

- Project title and creative intent
- Target duration and languages
- Characters and setting
- Shot identifiers
- Start times and durations
- Visual descriptions
- Camera directions
- Amharic narration
- English subtitles
- Continuity requirements

Each shot has a unique identifier, such as S01, S02, and S10.

The storyboard helps maintain consistency between the visual scenes and narration.

## 4. Pipeline Components

### 4.1 Storyboard Validator

File: `src/validate_storyboard.py`

Responsibilities:

- Load the storyboard JSON.
- Check JSON readability.
- Verify that shots exist.
- Check positive shot durations.
- Verify continuous timing without gaps or overlaps.

### 4.2 Visual Asset Generation

AI-assisted image and video generation tools were used to create the fictional characters, locations, and scene visuals.

Generated visual assets are organized under `assets/`.

Some short video clips were extended using animated still images and FFmpeg processing to maintain the planned shot durations.

### 4.3 Narration Generation

File: `src/generate_narration.py`

Responsibilities:

- Read narration entries from `script/narration.json`.
- Use Edge TTS with the Amharic voice `am-ET-MekdesNeural`.
- Generate MP3 narration files.
- Store generated audio under `assets/narration/`.
- Skip existing non-empty audio files.
- Retry failed generation attempts.

### 4.4 Video Assembly

File: `src/assemble_video.py`

Responsibilities:

- Read the scene list from `assets/video/concat_list.txt`.
- Normalize video dimensions and frame rates.
- Prepare clips for consistent playback.
- Combine the clips into a landscape video.

### 4.5 Audio and Subtitle Integration

File: `src/add_audio_subtitles.py`

Responsibilities:

- Combine the assembled video with Amharic narration.
- Add background music.
- Integrate English subtitles.
- Export the final narrated film.

The current implementation uses a fixed background-music volume rather than automated sidechain ducking.

## 5. Data and Asset Flow

The main production flow is:

```text
storyboard.json
       |
       v
Storyboard Validation
       |
       v
Visual Assets + Narration Configuration
       |
       v
AI-Generated Scene Clips
       |
       v
Narration Generation
       |
       v
Landscape Video Assembly
       |
       v
Audio + Music + English Subtitles
       |
       v
Final Video
       |
       v
End Card and Portrait Export
```

## 6. Output Files

The project produces:

- `output/the_waiting_mother_final.mp4`
- `output/the_waiting_mother_with_endcard.mp4`
- `output/the_waiting_mother_vertical.mp4`

The final deliverables include landscape and portrait formats with narration, subtitles, background music, and an AI disclosure card.

## 7. Design Decisions

### Amharic narration

Amharic was selected because the story is rooted in an Ethiopian setting and is intended to connect with Ethiopian audiences.

### English subtitles

English subtitles make the film accessible to viewers who do not understand Amharic.

### Fictional characters

The mother and daughter are fictional characters created for the film. Synthetic narration is used instead of imitating a real person's voice.

### FFmpeg processing

FFmpeg provides a reproducible way to normalize video clips, combine media, mix audio, and export different aspect ratios.

## 8. Current Architectural Limitations

- The complete production pipeline is not yet orchestrated by one command.
- Storyboard validation does not yet use a complete JSON Schema.
- Per-shot selective regeneration is not yet fully implemented and verified.
- Historical model-call metadata is incomplete.
- End-card generation and portrait export remain separate processing steps.

These limitations are documented to distinguish implemented functionality from future improvements.
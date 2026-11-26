# Experiments and Production Observations — The Waiting Mother

## 1. Overview

This document records the experiments, tests, and practical observations made while producing The Waiting Mother.

The goal was to create an 80-second cinematic short film using AI-assisted visual generation, synthetic Amharic narration, subtitles, and video-processing tools.

Exact numerical measurements were not recorded for every experiment. Where measurements are unavailable, observations are described qualitatively rather than presented as measured results.

## 2. Experiments and Observations

| No. | Experiment | Observation / Outcome |
|---|---|---|
| 1 | AI-generated still images | Generated visual scenes for the mother, daughter, and rural setting. |
| 2 | AI video generation | Produced short moving clips, although some were shorter than the required shot duration. |
| 3 | Extending short clips | Combined short generated footage with animated still images to fill the required duration. |
| 4 | Pan-and-zoom animation | Used still-image movement for shots that did not have suitable video clips. |
| 5 | Amharic synthetic narration | Generated narration using the `am-ET-MekdesNeural` voice. |
| 6 | Narration speed | Used a speech rate of -5% to produce a slower delivery. |
| 7 | English subtitles | Added English subtitle cues to make the Amharic story understandable to a wider audience. |
| 8 | Audio synchronization | Adjusted audio timing, resampling, delays, and padding to resolve synchronization and missing-audio problems. |
| 9 | Background music | Added third-party Pixabay background music at a fixed reduced volume with fades. |
| 10 | Final video formats | Exported horizontal 16:9 and vertical 9:16 versions of the film. |

## 3. Technical Validation

The following checks were performed:

- Storyboard validation reported 10 shots.
- Total storyboard duration was 80 seconds.
- All shot timings were continuous.
- Narration files for S01–S06 and S08–S10 were verified to exist.
- S07 intentionally has no narration file.
- The horizontal video with the end card was exported.
- The vertical video was exported at 1080 × 1920.
- The final audio was checked with FFmpeg and listened to manually.

## 4. Important Production Decisions

### Extending Short AI Video Clips

Some generated clips were approximately three seconds long, while the storyboard required eight-second shots.

Rather than accepting gaps or shortening the film, the workflow used animated still images to extend the visual sequence.

### Using Synthetic Amharic Narration

Synthetic Amharic narration was selected to communicate the story in its chosen language without using a real person's recorded voice.

### Creating Two Aspect Ratios

Both horizontal and vertical exports were created to support different viewing platforms.

## 5. Limitations of the Experiments

The experiments were primarily practical production tests rather than controlled scientific comparisons.

The following information was not consistently recorded:

- Exact model versions for every generation.
- Random seeds.
- Full generation parameters.
- Generation latency.
- Per-generation monetary cost.
- Quantitative audience preference comparisons.

Therefore, no unsupported performance scores or numerical comparisons are claimed.

## 6. Future Experiments

Future work should investigate:

1. Comparing different image-generation prompts for character consistency.
2. Comparing video-generation tools using the same shot description.
3. Testing automated sidechain music ducking.
4. Comparing narration speeds with listener feedback.
5. Measuring the effectiveness of different subtitle styles.
6. Implementing hash-based shot caching and testing selective regeneration.
7. Conducting structured audience tests with documented feedback.

## 7. Conclusion

The production experiments helped identify practical strengths and limitations of AI-assisted filmmaking. The most important lesson was that generated assets require validation and sometimes additional processing before they can be used in a coherent final film.
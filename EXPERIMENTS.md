# Experiments and Production Observations — The Waiting Mother

## 1. Overview

This document records the experiments, tests, and practical observations made while producing *The Waiting Mother*.

The goal was to create an 80-second cinematic short film using AI-assisted visual generation, synthetic Amharic narration, English subtitles, background music, and video-processing tools.

These experiments were practical production tests rather than controlled scientific comparisons. Exact numerical measurements were not recorded for every experiment. Where measurements are unavailable, observations are described qualitatively rather than presented as measured results.

## 2. Experiments and Observations

| No. | Experiment | Observation / Outcome | Lesson Learned |
|---|---|---|---|
| 1 | AI-generated still images | Generated visual scenes featuring the mother, daughter, and rural setting. | Visual consistency should be reviewed across all scenes. |
| 2 | AI video generation | Produced short moving clips, although some were shorter than the required shot duration. | Generated clip duration should be checked before assembly. |
| 3 | Extending short clips | Combined short generated footage with animated still images to fill the required duration. | Combining different visual techniques can help maintain timeline continuity. |
| 4 | Pan-and-zoom animation | Used still-image movement for shots without suitable video clips. | Static images can contribute to a cinematic sequence when animated carefully. |
| 5 | Amharic synthetic narration | Generated narration using the `am-ET-MekdesNeural` voice. | Synthetic narration makes it possible to produce dialogue without recording a real person's voice. |
| 6 | Narration speed | Used a speech rate of -5% for a slower delivery. | Speech rate affects the pacing and emotional delivery of narration. |
| 7 | English subtitles | Added English subtitle cues to make the Amharic story understandable to a wider audience. | Subtitles help communicate the story to viewers who do not understand the narration language. |
| 8 | Audio synchronization | Adjusted audio timing, resampling, delays, and padding to resolve synchronization and missing-audio problems. | Audio should be validated throughout the entire timeline. |
| 9 | Background music | Added third-party Pixabay background music at a fixed reduced volume with fades. | Background music must be balanced against narration; automated sidechain ducking remains future work. |
| 10 | Final video formats | Exported horizontal 16:9 and vertical 9:16 versions of the film. | Multiple aspect ratios support different viewing platforms. |

## 3. Technical Validation

The following checks were performed during production:

- Storyboard validation reported 10 shots.
- Total storyboard duration was 80 seconds.
- All shot timings were continuous.
- Narration files for S01–S06 and S08–S10 were verified to exist.
- S07 intentionally has no narration file.
- The horizontal video with the end card was exported.
- The vertical video was exported at 1080 × 1920.
- The final audio was checked using FFmpeg and manual listening.

These checks confirmed important properties of the produced assets. They should not be interpreted as a complete automated test suite.

## 4. Important Production Decisions

### 4.1 Extending Short AI Video Clips

Some generated clips were approximately three seconds long, while the storyboard required eight-second shots.

Rather than accepting gaps or shortening the film, the workflow used animated still images to extend the visual sequence.

### 4.2 Using Synthetic Amharic Narration

Synthetic Amharic narration was selected to communicate the story in its chosen language without using a real person's recorded voice.

### 4.3 Creating Two Aspect Ratios

Both horizontal and vertical exports were created to support different viewing platforms.

### 4.4 Correcting Audio Problems

An earlier export contained an almost silent final section. The audio-processing workflow was updated, and the resulting export was checked with FFmpeg and listened to manually.

## 5. Limitations of the Experiments

The experiments were primarily practical production tests rather than controlled scientific comparisons.

The following information was not consistently recorded:

- Exact model versions for every generation.
- Random seeds.
- Full generation parameters.
- Generation latency.
- Per-generation monetary cost.
- Quantitative audience preference comparisons.

No unsupported performance scores or numerical comparisons are claimed.

## 6. Future Experiments

Future work should investigate:

1. Comparing different image-generation prompts for character consistency.
2. Comparing video-generation tools using the same shot description.
3. Testing automated sidechain music ducking.
4. Comparing narration speeds with feedback from actual listeners.
5. Measuring the effectiveness of different subtitle styles.
6. Implementing hash-based shot caching and testing selective regeneration.
7. Conducting structured audience tests with documented feedback.

## 7. Conclusion

The production experiments helped identify practical strengths and limitations of AI-assisted filmmaking. The most important lesson was that generated assets require validation and sometimes additional processing before they can be used in a coherent final film.

Recording observations, technical checks, and limitations provides a useful foundation for improving the pipeline and making future production runs more reproducible.
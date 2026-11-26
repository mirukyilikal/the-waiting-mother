# Failures and Lessons Learned — The Waiting Mother

## 1. Overview

During the production of *The Waiting Mother*, several technical and creative challenges affected the workflow. This document records the main problems, the solutions applied, and the lessons learned during development.

## 2. Problems Encountered

### 2.1 Short AI-Generated Video Clips

**Problem:** Some AI video-generation tools produced clips of approximately three seconds instead of the required eight seconds.

**Solution:** Short clips were extended by combining generated footage with animated still images. Other shots used slow pan-and-zoom movements to maintain visual continuity.

**Lesson:** AI-generated clips should be checked for duration and visual consistency before being added to the final timeline.

### 2.2 Missing Narration Files

**Problem:** The narration configuration initially did not include all the dialogue lines for shots S08 and S09.

**Solution:** The missing lines were added to `script/narration.json`, and the corresponding narration files were generated and verified.

**Lesson:** Every storyboard narration entry should be checked against the generated audio files.

### 2.3 Narration Generation Error

**Problem:** Narration generation encountered an error while processing an Amharic line.

**Solution:** The affected narration was tested separately, and the generated audio files were checked before continuing.

**Lesson:** Testing individual narration lines helps identify problems before full video assembly.

### 2.4 Missing Voice and Subtitles

**Problem:** An early assembled video did not display the expected subtitles or play the narration.

**Solution:** The audio and subtitle processing workflow was corrected, and the video was assembled again. The final export was checked to confirm that narration and English subtitles were present.

**Lesson:** Audio and subtitle tracks should be verified in the exported video, not only in their separate source files.

### 2.5 Audio Levels and Synchronization

**Problem:** The final section of an earlier video export had almost no audible sound.

**Solution:** The audio-processing workflow was updated to correct timing, resampling, delays, and padding. The resulting audio was checked using FFmpeg volume analysis and manual listening.

**Lesson:** Audio should be checked across the entire film, especially at transitions and near the ending.

### 2.6 Windows Terminal Character Display

**Problem:** Some Amharic text appeared incorrectly when displayed in Windows PowerShell.

**Solution:** The JSON files were checked using Python with UTF-8 encoding to distinguish terminal display problems from actual file corruption.

**Lesson:** Terminal display problems do not necessarily mean the underlying UTF-8 file is corrupted.

## 3. Remaining Limitations

The following limitations remain:

- The pipeline does not yet provide complete one-command end-to-end generation from a clean clone.
- JSON Schema validation is implemented, but further validation and testing may still be needed.
- Historical AI model-call metadata is incomplete.
- Selective regeneration of individual visual shots has not been fully implemented and verified.
- The background music is third-party Pixabay music, not an original composition.
- Music volume is controlled using a fixed level rather than automated sidechain ducking.
- Automated tests are incomplete.

These limitations are documented honestly rather than presented as completed features.

## 4. Lessons for Future Development

Future versions should:

1. Validate every input before starting generation.
2. Use consistent naming conventions for all generated assets.
3. Record errors and generation attempts automatically.
4. Implement reliable per-shot caching and selective regeneration.
5. Test audio, subtitles, and video duration after every major assembly.
6. Keep a record of generation tools, settings, and costs.
7. Test the complete workflow from a clean repository clone.

## 5. Conclusion

The production process involved practical challenges involving AI-generated video duration, narration, subtitles, and audio synchronization. Addressing these problems improved the final film and highlighted important areas for improving the pipeline. Documenting both successful solutions and remaining limitations makes the project more transparent and provides a foundation for future development.
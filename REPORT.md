# The Waiting Mother
## AI-Content Generation Challenge — Project Report

### 1. Project Overview

**The Waiting Mother** is an 84-second AI-assisted short film about a mother's love, patience, and emotional connection with her daughter.

The story takes place in a fictional Ethiopian rural village. Every afternoon, a mother waits outside her home for her daughter to return from school. When the daughter arrives, she asks why her mother waits for her every day. The mother explains that she wants her daughter to always know that someone will welcome her home with love.

The film communicates a simple message: a mother's love is often expressed through small actions, such as waiting, caring, and welcoming her child home.

### 2. Goal and Intended Audience

The goal was to create a short, emotionally meaningful film using an AI-assisted production pipeline rather than completing every production task manually.

The intended audience includes:
- Families and parents.
- Young people and students.
- People interested in Ethiopian stories and culture.
- Viewers who appreciate emotional, family-centered short films.

The film uses Amharic narration to connect with its intended cultural setting and English subtitles to make the story accessible to a wider audience.

### 3. Production Process

The film was produced through several stages:

1. **Story development:** I developed a short story about a mother waiting for her daughter to return from school.
2. **Storyboard creation:** I divided the story into 10 shots with a planned duration of 80 seconds. The storyboard was stored in `storyboard.json`.
3. **Visual generation:** I used AI image-generation tools to create scene images and AI video-generation tools to produce short clips.
4. **Shot assembly:** Because some generated clips were shorter than required, I extended selected scenes and used pan-and-zoom animation on still images.
5. **Narration:** I generated Amharic narration using Microsoft Edge Text-to-Speech with the `am-ET-MekdesNeural` voice.
6. **Subtitles:** I prepared English subtitles and added them to the video.
7. **Audio editing:** I combined the narration with background music, adjusted audio levels, and applied fades.
8. **Final editing:** I used Python and FFmpeg to assemble and export horizontal and vertical versions of the film.
9. **End card:** I added a four-second closing card identifying the film as AI-generated.

The storyboard contains 10 shots covering 80 seconds. The final horizontal and vertical exports are both 84 seconds because of the additional four-second end card.

### 4. Hardest Technical Challenge and Solution

One of the hardest problems during production was synchronizing the narration, subtitles, and background music with the video.

In an early export, some narration and subtitles did not appear correctly. I also discovered that the final section of the video had very low audio levels, making the ending difficult to hear.

I investigated the problem using FFmpeg and checked the audio levels with its `volumedetect` filter. The final section initially had an average volume of approximately -91 dB.

To solve this, I adjusted the audio-processing workflow. I corrected audio timing, resampled the audio, applied delays where necessary, padded the audio to match the required duration, and mixed the tracks again.

After rebuilding the video, I checked the audio levels again. The final section reached an average level of approximately -24.8 dB, with a maximum level of -6.4 dB. I also listened to the final export to confirm that the audio was working properly.

This experience taught me that generating good visual and audio assets is not enough. A reliable production pipeline must also validate synchronization, duration, and audio quality before exporting the final film.

### 5. Lessons Learned

**A practice that helped:**

Breaking the film into smaller shots and organizing them in a structured storyboard made production easier. It helped me manage scene order, timing, narration, and video assembly. Using FFmpeg to inspect and validate the final output also helped me identify technical problems.

**A practice that did not work as expected:**

Relying entirely on AI-generated video clips was not reliable. Some clips were shorter than expected, and some generated movements did not maintain the continuity I wanted. I had to extend clips and use animated still images to complete the film.

I also learned that AI-generated narration and music require careful review. Generating them does not automatically guarantee natural speech, good synchronization, or professional audio quality.

### 6. Audience Feedback and Evaluation

Initial design-review observations identified three areas for improvement:

- Background music consistency.
- Visual continuity, especially character movement between scenes.
- The naturalness of the Amharic narration.

These observations informed the project's design and production documentation.

However, formal audience testing with at least three viewers has not yet been completed. Therefore, these observations should not be treated as results from a completed audience study.

A future evaluation will involve showing the film to viewers, collecting structured feedback, and documenting the changes made in response.

### 7. Current Limitations

The project has several limitations:

- Some scenes use animated still images instead of fully generated video.
- The Amharic synthetic narration may not sound completely natural.
- The background music comes from Pixabay rather than being an original composition.
- The music uses a reduced fixed volume and fades; automatic sidechain ducking has not been implemented.
- Formal audience testing has not yet been completed.
- The pipeline does not yet support complete one-command execution from a clean clone or automatic regeneration of only changed shots.

These limitations are documented honestly in the project documentation.

### 8. Future Improvements

If I continue developing this project, I plan to:

1. Improve the naturalness and emotional expression of the Amharic narration.
2. Create an original musical score that better matches the emotional tone of the film.
3. Implement automatic sidechain audio ducking so the music lowers when narration is playing.
4. Improve visual consistency and character movement between generated scenes.
5. Implement caching and selective shot regeneration so that changing one scene does not require regenerating the entire film.
6. Add a reliable one-command pipeline for running the project from a clean clone.
7. Conduct structured audience testing and use real viewer feedback to improve the film.
8. Expand automated validation and testing of the production pipeline.

### 9. Conclusion

The Waiting Mother helped me explore how AI tools can support storytelling and video production. I learned to combine image generation, video generation, synthetic narration, subtitles, Python, and FFmpeg into a structured workflow.

The most important lesson was that AI-generated content still requires human judgment, technical validation, and creative decision-making. The tools can accelerate production, but the creator remains responsible for the story, quality, accuracy, and ethical use of the generated content.

This project is an important step in my learning journey toward building more reliable and responsible AI-assisted creative systems.

### 10. Project Repository

The source code, storyboard, production documentation, and technical implementation are available in the public GitHub repository:

**GitHub:** https://github.com/mirukyilikal/the-waiting-mother

The repository provides documentation of the production workflow, architecture, experiments, failures, costs, and ethical considerations.
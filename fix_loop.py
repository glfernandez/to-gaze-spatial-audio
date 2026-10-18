import re

with open("Rehearsal_Soundboard.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the loop logic inside the setInterval
old_logic = """      // Loop or Stop logic
      if (current >= currentEnd) {
        if (s.loop) {
          s.audio.currentTime = currentStart;
        } else {
          toggleAudio(id);
        }
      }"""

new_logic = """      // Loop or Stop logic
      // Buffer of 0.05s to prevent the audio from natively ending and pausing itself
      if (current >= currentEnd - 0.05 || s.audio.ended) {
        if (s.loop) {
          s.audio.currentTime = currentStart;
          s.audio.play().catch(e => console.log(e)); // Force play in case it natively paused
        } else {
          toggleAudio(id);
        }
      }"""

html = html.replace(old_logic, new_logic)

with open("Rehearsal_Soundboard.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Loop logic fixed!")

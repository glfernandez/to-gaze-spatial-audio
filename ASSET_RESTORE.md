# Private audio asset restore guide

The public GitHub repository contains the soundboard source, cue sheets, documentation, and maintenance scripts. Production audio is intentionally not public because it includes large masters, licensed/downloaded source material, and voice recordings.

## Canonical archive

- Gary OS project ID: `MEDIA-TO-GAZE-SPATIAL-AUDIO`
- Google Drive folder: `My Drive/clarw_lighting`
- Private asset directory: `SFX/`
- Asset inventory: `SFX_INVENTORY.tsv`

The Drive folder is the canonical full-fidelity archive. Keep its sharing setting private unless every recording and source asset has been cleared for redistribution.

## Restore on a new show computer

1. Clone the public repository.
2. In Google Drive for desktop, make the private `clarw_lighting/SFX` folder available on the show computer.
3. Copy or link that `SFX` directory into the repository root so `Rehearsal_Soundboard.html` can resolve `SFX/...` paths.
4. Verify that every audio file referenced by the soundboard is present:

   ```bash
   python3 verify_assets.py
   ```

5. Open `Rehearsal_Soundboard.html` in Chrome or Safari and run a cue check before rehearsal.

## What a Git pull restores

`git pull` restores code, documentation, cue sheets, and scripts. It does not restore private audio. The audio restore is a separate Drive step by design.

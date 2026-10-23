# Release testing

Reference ROM: `dist/NOTHING.gbc`, 131072 bytes.

SHA-256:
`46acb13973fa0729983251b6f484ad2c494a4e50f1035b9daad13d1b67fb5699`

## Completed checks

- Real-ROM controller replay in PyBoy 2.7.0: **18 checkpoints** passed.
- A map promise, collection, and return remain separate states.
- A wrong consent answer enters the required platformer without losing earlier
  progress or completing the unanswered ethical gate.
- Reopening the emulator with its battery save restores the unfinished detour.
- Pit retries work without repeating the introduction; all three jumps are
  completable with normal controller input.
- Winning the detour returns to its unresolved question.
- Admitting damage and repairing the sign remain separate actions.
- Victory displays the joke and moving hand actors.
- Restart restores the ending. Declining replay preserves it; accepting clears
  progress for a fresh run.
- Native resources: 36 files with unique IDs/symbols and valid scene references.
- Native dialogue analysis: 34 events, 39 pages, no fit diagnostics after fixes.
- Six scene graphics analyses returned no diagnostics.
- The final ROM was flashed successfully to a physical ModRetro Chromatic.
  Jess subsequently reported beating it and seeing the raining middle fingers.
- The separate public source copy was compiled and also passed all 18 replay
  checkpoints. Its bytes differ only in the four-byte GB Studio save signature
  at `0x200` and the two-byte cartridge checksum. The distributed ROM remains
  the exact hardware-tested build above. Rebuilt versions may invalidate older
  saves because GB Studio hashes the loaded project data for save compatibility.

The screenshots in `docs/images/` are real emulator captures. The reproducible
input sequence and matching symbols are under `tests/fixtures/`. No RAM writes
were used to manufacture progress.

## Bugs caught before release

1. Duplicate exit compiler symbols sent a room to the wrong script.
2. Adjacent triggers overlapped the player's collision area and masked an exit.
3. Pit retries unnecessarily repeated the tutorial.
4. Dialogue initially exceeded the actual font's available line width.

Those were corrected and the final walkthrough rerun. “One prompt” is a claim
about the creative starting point, not the absence of debugging.

## Limits

This is a small first playable release, not exhaustive branch coverage.
The manual pause-save branch and the third question's wrong answer have not
had separate dedicated controller walkthroughs. Hardware save retention and
audio have not been independently tested. Physical completion is Jess's report;
automated save checks ran in the emulator. Other emulators/hardware may differ.

Only one platformer detour is implemented; the broader arcade ideas are not
part of this release. See [BUILDING.md](BUILDING.md) to rerun the available tests.

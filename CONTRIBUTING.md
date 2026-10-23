# Contributing

Small, playable improvements are welcome. Describe what changes for the player,
include a screenshot when it affects the screen, and say what you tested.

Keep these rules intact unless your change explicitly proposes a new design:

- A promise is not the same as carrying it out.
- A mandatory detour must be beaten; a restart must not silently erase it.
- Beating the detour returns the player to the unresolved choice.
- Ask before clearing a saved game.
- The joke is that you win NOTHING.

Run `python3 check_resources.py`, build the ROM, and play your changed path.
Use the controller replay when your change preserves its layout and timing.
Do not commit personal saves, device logs, access tokens, or vendor executables.

For bugs, include the ROM version/hash, emulator or handheld, and the steps
needed to reproduce the problem. Please keep reports about the game itself.

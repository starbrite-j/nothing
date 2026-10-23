# Building NOTHING

## Editable project

The shipped ROM was built with GB Studio CLI **4.3.2** and GBDK **4.5.0**.
The native project descriptor uses resource format 4.2.0, release 10.

1. Clone or download this repository, including the assets.
2. Open `project.gbsproj` in a compatible GB Studio installation.
3. Edit scenes/events in `project/` or artwork in `assets/` through the editor.
4. Use the editor's ROM export to build a Game Boy Color cartridge image.

Newer editor releases may migrate the project. Work on a copy when upgrading.
The compiled reference ROM is `dist/NOTHING.gbc`; keep new builds in `build/`.

## CLI build

With GB Studio's CLI and its required build tools installed, the command is:

```sh
mkdir -p build
node /path/to/gb-studio-cli.js make:rom project.gbsproj build/NOTHING.gbc
```

Replace the CLI path with your installation. This repository does not bundle
GB Studio, GBDK, the Chromatic plugin, device utilities, or an emulator.
You do not need the Chromatic plugin to edit the project in GB Studio.

## Quick source check

```sh
python3 check_resources.py
```

This checks duplicate resource IDs, duplicate compiler symbols, and unresolved
scene transitions. It does not replace compilation or gameplay testing.

## Controller replay

Python 3.11 and PyBoy 2.7.0 were used for the recorded test:

```sh
python3 -m venv .venv
.venv/bin/pip install -r tests/requirements.txt
.venv/bin/python tests/replay.py
```

The default test checks the distributed ROM against its matching compiler
symbols. To test a fresh build with newly generated symbols:

```sh
.venv/bin/python tests/replay.py --rom build/NOTHING.gbc --symbols /path/to/symbols.noi
```

The timed replay expects the release layout and behavior. Intentional changes
may require updating the replay fixture after a new manual walkthrough. RAM is
read for assertions, never written to advance the game. Temporary battery saves
are isolated from the ROM you play.

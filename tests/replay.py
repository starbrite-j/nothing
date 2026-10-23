"""Controller-only release replay; game RAM is read only for assertions."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tempfile

from pyboy import PyBoy

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--rom', type=Path, default=ROOT / 'dist/NOTHING.gbc')
parser.add_argument('--symbols', type=Path,
                    default=ROOT / 'tests/fixtures/NOTHING.symbols.noi')
args = parser.parse_args()
symbols = {}
for line in args.symbols.read_text().splitlines():
    parts = line.split()
    if len(parts) == 3 and parts[0] == 'DEF':
        symbols[parts[1]] = int(parts[2], 16)

records = json.loads((ROOT / 'tests/fixtures/controller-replay.json').read_text())
with tempfile.TemporaryDirectory(prefix='nothing-replay-') as temporary:
    cart = Path(temporary) / 'NOTHING.gbc'
    shutil.copy2(args.rom, cart)

    def boot():
        emulator = PyBoy(str(cart), window='null', sound_emulated=False)
        emulator.set_emulation_speed(0)
        emulator.tick(120, True)
        return emulator

    game = boot()
    held = set()
    checkpoints = 0
    try:
        for record in records:
            command = record['input']
            if command.get('restart'):
                game.stop(save=True)
                game = boot()
                held = set()
            else:
                buttons = set(command.get('buttons', []))
                for button in held - buttons:
                    game.button_release(button)
                for button in buttons - held:
                    game.button_press(button)
                held = buttons
                game.tick(command.get('frames', 1), True)
            if command.get('snapshot'):
                label = command['snapshot']

                def word(address):
                    return game.memory[address] + 256 * game.memory[address + 1]

                pointer = symbols['_current_scene']
                address = game.memory[pointer] * 65536 + word(pointer + 1)
                scene = next((key for key, value in symbols.items()
                              if key.startswith('_scene_') and value == address), 'unknown')
                variables = [word(symbols['_script_memory'] + 2 * j) for j in range(11)]
                expected = record['observed']
                assert scene == expected['scene'], (label, scene, expected['scene'])
                assert variables == expected['variables'], (label, variables, expected['variables'])
                checkpoints += 1
                print(f'PASS {label}')
        print(f'PASS: {checkpoints} checkpoints; SHA256 {hashlib.sha256(cart.read_bytes()).hexdigest()}')
    finally:
        game.stop(save=True)

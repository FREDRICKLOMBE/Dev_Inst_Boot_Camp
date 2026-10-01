# Rock Paper Scissors

## Run

Keep both Python files in the same folder. Open a terminal there and run:

```sh
python rock-paper-scissors.py
```

On Windows you can use `py -E rock-paper-scissors.py`. The `-E` option ignores
Python environment variables, which avoids the existing PYTHONHOME startup
problem on this computer. No third-party packages are needed; use Python 3.8+.

## Files and sections

- `game.py`: `Game` class, with **Choice handling** and **Round logic** sections.
- `rock-paper-scissors.py`: **Menu**, **Score presentation**, and
  **Application startup** sections.

Every method and function has a docstring describing its return value.
Comments explain decisions such as keeping scores outside the menu loop.

## Playing

1. Choose `1` to play one round. Enter `rock`, `paper`, or `scissors`.
2. Choose `2` to show the current scores and return to the menu.
3. Choose `3` to show the final scores and quit.

Capital letters and surrounding spaces are accepted for game choices.
Invalid input prompts again. Scores last for the current session only.
Ctrl+C or end-of-input also ends the session and displays completed-round totals.

Rock beats scissors, scissors beats paper, and paper beats rock. Equal choices
draw. Results are always from the user's perspective. The computer uses
`random.choice()` to select its move.

As requested by the course, `print_results()` thanks the user whenever it
displays scores, including when called through Show scores.

## Manual checks

- Show scores before playing: all counters should be zero.
- Enter an invalid menu option: the menu should ask again.
- Enter ` ROCK `: it should be accepted as rock.
- Enter an invalid move: it should ask again without counting a round.
- Play several rounds: total rounds should equal wins + losses + draws.
- Show scores repeatedly: counts should stay unchanged.
- Quit: final scores should appear and the program should end.

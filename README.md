# CLI Scrabble Word Game (Simplified)

A simple command-line word game inspired by Scrabble, developed as an assignment for the university course "Learning Theories & Educational Software".  
Players form words using Greek letters from a random hand, competing against the computer.
No board is involved — just word creation and scoring.

---

## Features

- Two-player game: Human vs CPU  
- Uses a Greek dictionary with all valid words up to 7 letters  
- Scoring based on letter values  
- Saves game statistics
- Simple and clean CLI interface with colored output  
- Ability to view average scores and past game results  

---

## Requirements

- Python 3.6 or higher  
- `colorama` module for colored terminal output

To install the dependency, run:

```pip install colorama```

---

## Files

- `main.py` — Entry point and main game loop  
- `classes.py` — Game classes, logic, and data structures  
- `greek7.txt` — Greek dictionary file (required for valid words)

---

## Statistics

Game results are saved in `results_data.json` after each session.  
The statistics menu shows:

- Total games played  
- Average player and CPU scores  
- Scores per past game  

---

## Screenshot

*(Add game screenshots here )*

---

## Notes

- The project requires the `greek7.txt` dictionary file to run correctly.  

---

## Possible Improvements

- Enhance UI with clearer prompts and input validation, or GUI
- Add multiplayer support  
- Implement hints or word suggestions

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International** license.  
See the [LICENSE](LICENSE) file for details.


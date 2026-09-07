# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] The game is a Streamlit number-guessing game with Easy, Normal, and Hard settings.
- [x] The original bugs included reversed hints, inconsistent numeric/string comparison, inconsistent initial attempt counting, and difficulty changes that left the active secret outside the displayed range.
- [x] The fixes move reusable logic into `logic_utils.py`, keep comparisons numeric, synchronize difficulty state, reset New Game state, and add pytest coverage.

## Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Select a difficulty; the sidebar shows its range and attempt limit.
2. Enter a guess and submit it; the game records the guess in the Guess History table.
3. A guess above the secret returns `Too High` and the hint `Go LOWER!`.
4. A guess below the secret returns `Too Low` and the hint `Go HIGHER!`.
5. Change difficulty to start a new compatible round, or select New Game to reset attempts, score, status, and history.
6. Enter the correct number; the game displays the winning message and final score.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
> .venv\Scripts\python.exe -m pytest
============================= test session starts =============================
platform win32 -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0
collected 6 items

tests\test_game_logic.py ......                                          [100%]

============================== 8 passed in 0.07s ==============================
```

## 🚀 Stretch Features

- [x] Advanced edge-case testing: empty, non-numeric, negative, and decimal inputs are tested with pytest, along with the starter difficulty ranges.
- [x] Agent Workflow: the AI-assisted multi-file refactor and verification are documented in `ai_interactions.md`.
- [x] Professional documentation and style: all functions in `logic_utils.py` have docstrings, and pycodestyle output is recorded in `ai_interactions.md`.
- [x] Enhanced UI: `app.py` displays the active range in the main game and shows a Guess History table in the sidebar.
- [x] Prompt comparison: two prompting strategies are compared in `ai_interactions.md`.

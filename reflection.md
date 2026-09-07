# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game displayed a number-guessing interface with difficulty settings, a developer debug panel, and a score. The first run showed that the hint wording was backwards: a too-high guess could say to go higher. The game also behaved inconsistently after changing difficulty because the active secret could remain outside the newly displayed range. The starter tests could not run successfully because `logic_utils.py` contained unimplemented functions.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess higher than the secret, such as `60` when the secret is `50` | The game should report that the guess is too high and tell the player to go lower. | The outcome is "Too High," but the hint says "Go HIGHER!" | none |
| On an even-numbered attempt, guess `9` when the secret is `50` | The game should compare both values numerically and report "Too Low." | The secret is converted to text, so text comparison can report the wrong result, such as "Too High." | none |
| Submit the first guess in the initial game | The first guess should be counted as attempt 1. | The game starts with `attempts = 1`, so the first submitted guess is counted as attempt 2. | none |
| Change difficulty to Hard when the Developer Debug Info shows secret `57` | The active secret should be inside the Hard range of `1–50`, or the game should start a new compatible round. | The sidebar shows Hard and range `1–50`, but the active secret remains `57`, outside the displayed range. | none |

---

## 2. How did you use AI as a teammate?

I used GitHub Copilot in VS Code to inspect the workspace, explain the game logic, plan fixes, and generate pytest coverage. One correct suggestion was to keep the secret as an integer and compare it numerically; after implementing that change, the high/low tests passed and the string-comparison path was removed. One misleading suggestion was to replace the starter attempt limits with `10/7/5`; that changed assignment-provided values without evidence, so I rejected it and preserved Easy `6`, Normal `8`, and Hard `5`. I verified the final behavior with pytest and a code diff review.

---

## 3. Debugging and testing your fixes

I treated a bug as fixed only when the code path matched the intended behavior and a focused pytest case passed. The final command collected six tests, including winning, too-high, too-low, empty-input, non-numeric-input, and difficulty-range cases, and all six passed. Pycodestyle also reported no issues after the test formatting was corrected. AI helped identify the return-tuple contract and suggest edge cases, but I reviewed the assertions and preserved the starter difficulty values manually.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script from top to bottom after an interaction such as clicking a button or changing a select box. Ordinary local variables are recreated during each rerun, so values that must survive need to be stored in `st.session_state`. The original game mixed reruns with inconsistent initialization, which made attempts and the secret behave differently between the first game and later games. The repair resets state when the selected difficulty changes and when New Game is pressed.

---

## 5. Looking ahead: your developer habits

I want to reuse the habit of recording a reproducible input, expected result, actual result, and test result before changing code. I would also ask AI to preserve assignment-provided values explicitly and review the diff before accepting a multi-file change. This project reinforced that AI-generated code can look plausible while hiding state, type, and integration bugs, so every suggestion needs human review and executable verification.

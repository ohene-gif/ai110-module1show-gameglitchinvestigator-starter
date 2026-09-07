# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Refactor the game logic into `logic_utils.py`, fix the incorrect numeric hints and difficulty state, add pytest edge-case coverage, add a small Guess History UI, and verify the result without changing the starter attempt limits.

**What did the agent do?**

The agent implemented the four shared functions in `logic_utils.py`, updated `app.py` to import them, corrected numeric comparison and hint direction, synchronized difficulty state, reset New Game state, and added the Guess History sidebar table. It updated `tests/test_game_logic.py`, ran `python -m pytest`, and produced a passing result of 6 tests.

**What did you have to verify or fix manually?**

I reviewed the diff and rejected an earlier suggestion to change the attempt limits to `10/7/5`, because the assignment provided Easy `6`, Normal `8`, and Hard `5`. I also verified that the Hard range remained `1–50` and that changing difficulty creates a compatible active secret.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Empty input | Add pytest coverage for empty guesses. | `parse_guess("")` returns the expected validation error. | Yes | Empty input is a common form submission case. |
| Non-numeric input | Add pytest coverage for invalid text guesses. | `parse_guess("not-a-number")` returns the expected validation error. | Yes | Users may type text instead of a number. |
| Difficulty ranges | Add pytest coverage for all starter difficulty ranges. | Easy, Normal, and Hard return their defined ranges. | Yes | This protects the assignment-provided settings from accidental changes. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Review the Python files for PEP 8 issues, run a linter, and apply only formatting fixes without changing game behavior.
```

**Linting output before:**

```
tests/test_game_logic.py:3:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:9:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:15:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:27:80: E501 line too long (80 > 79 characters)
```

**Changes applied:**

Two blank lines were added between test functions, and the long non-numeric-input assertion was wrapped. A second pycodestyle run produced no warnings for `app.py`, `logic_utils.py`, or `tests/test_game_logic.py`.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

Compare two prompting strategies for fixing the reversed hints while preserving the starter difficulty and attempt settings.

| | Model A | Model B |
|-|---------|---------|
| **Model name** | Copilot: broad bug review | Copilot: constrained repair prompt |
| **Response summary** | Identified many possible issues and proposed a broader redesign. | Focused on the confirmed hint/type bug and preserved the provided settings. |
| **More Pythonic?** | Mixed; it introduced an unsupported attempt-limit change. | More appropriate because it made the smallest evidence-based change. |
| **Clearer explanation?** | Useful for finding possibilities, but it blurred bugs and design choices. | Clearer because each change was tied to a reproduction and a test. |

**Which did you prefer and why?**

I preferred the constrained repair prompt. It produced a smaller, more reviewable change and made it easier to reject the unsupported `10/7/5` attempt-limit suggestion. This is a prompt comparison rather than a claim that two different model vendors were used.

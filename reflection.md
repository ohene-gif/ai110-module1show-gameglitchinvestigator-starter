# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

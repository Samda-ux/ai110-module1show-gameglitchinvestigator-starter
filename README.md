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
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game's purpose:** The player tries to guess a secret number within a set range (1–100 on the default difficulty). After each guess the game hints "Higher" or "Lower" until the player finds the number or runs out of attempts.
- [x] **Bugs found:**
  1. **Hints are reversed:** the game says "Higher" when the guess is too high and "Lower" when it is too low.
  2. **Difficulty range doesn't update:** switching difficulty doesn't change the range of the secret number correctly.
  3. **Score doesn't match the difficulty:** after switching difficulty, the score doesn't line up with that difficulty's range.
  4. **New Game doesn't work:** after you win or lose, you can't start a new game.
- Swapped lower and higher so it outputs the proper hint.
- Changing difficulty starts fresh new game which fixes the issue with score not changing and range not changing

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Guessing game that picks a score between 1 and 100.
2. Multiple difficulties that you can choose.
3. Pick your difficulty, check your range and enter your guess in the box and submit.
4. Continue until you either run out of attempts or make it.
5. Click new game when game ends.

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests/test_game_logic.py::test_winning_guess PASSED                                                                                            [ 25%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                           [ 50%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                            [ 75%]
tests/test_game_logic.py::test_score_changes_when_swapping_difficulty PASSED                                                                   [100%]

================================================================= 4 passed in 0.88s =================================================================

```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

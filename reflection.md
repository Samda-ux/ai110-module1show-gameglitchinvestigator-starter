# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| 60 | Higher | Lower | ---------------------- |
| 20 | Lower | Higher | |
| Change| | | |
|diffi- | | | |
|culty |Remake score |Score the same | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  AI suggested fixing the code in certain areas including changing higher or lower and starting a new game difficulty swapped. I reviewed the code and tried the game out and it appeared fine
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  AI suggested filling out the reflection and i stopped it because it looked hard to read

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  Reviewed the code and tried it out
- Describe at least one test you ran (manual or using pytest)  
   and what it showed you about your code.
  I ran pytest and made a new test that checks if when I swap difficulties does my score changes with the new range as parameters
- Did AI help you design or understand any tests? How?
  Yes I used a new test that AI helped design on my suggestion which checks if the score changes when swapping difficulties

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  It outputs a web address that allows you to run the app locally

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    Probably more tests as if I used tests in the start would have helped me see problems faster
- What is one thing you would do differently next time you work with AI on a coding task?
  Probably learn how to give better prompts.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  AI is more than a tool it's almost like multiple people working with you because they are so helpful but at the same time so dumb.

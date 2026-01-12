# Blackjack (Python) 

A command-line Blackjack-style card game written in Python.  
Built during my first year at university to practice Python fundamentals, modular design, and game logic.

## Highlights
- Multiplayer (2–7 players depending on version)
- Shuffled deck generation
- Score tracking up to 21
- Replayable rounds
- Betting system (in later versions)
- Dealer logic experiments (in later versions)

> Note: This project was developed incrementally across multiple versions as part of a learning process.

---

## How to Run

### Requirements
- Python 3.x

### Run
If your main file is located in `src`:
```bash
python src/blackjack.py
```

---

## Versions

This repository contains multiple iterations of the same project, developed incrementally as part of a learning process.

- **v1 — Simple version**
  - Multiplayer
  - Closest to 21 wins
  - No betting system, no dealer

- **v2 — Betting version**
  - Adds a betting system (*mise*)
  - Input constraints (2–7 players)
  - Replayable rounds

- **v3 — Betting + dealer (random behavior)**
  - Introduces a dealer (*croupier*)
  - Dealer may draw additional cards randomly

- **v4 — Betting + dealer (rule-based behavior)**
  - Introduces dealer decision rules (stand / hit around 17)
  - Further experimentation with dealer logic

> **Recommended usage:**  
> The `main` branch contains the stable version (v2), while experimental versions are available via tags and the `versions` branch.


---

## What I Learned

- Breaking a problem into functions (deck creation, drawing cards, scoring, turns)
- Using lists and dictionaries to manage game state
- Handling user input and controlling game flow
- Iterating on a project across multiple versions (feature additions and debugging)

---

## Possible Future Improvements

- Automatic Ace handling (11 or 1) without prompting the user
- Full dealer rules (dealer draws until reaching 17)
- Explicit hand representation (store cards instead of only totals)
- Improved input validation and error handling
- Unit tests for score calculation and winner selection

---

## Project Context

This project was developed during my first year at university.  
The goal was to implement a complete, playable game loop and progressively extend it with new features.

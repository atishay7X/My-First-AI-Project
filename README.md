# My-First-AI-Project
# I have added comments in the wholw code for better understanding. Cheers!!


🎮 Rock Paper Scissors — AI Pattern Learning Game



📌 Overview
A command-line Rock Paper Scissors game built in Python where you don't just play against a random bot — you play against an AI that actively learns your move patterns and adapts its strategy to beat you.





🧠 How the AI Works

The AI uses N-Gram Frequency Analysis, a concept borrowed from Natural Language Processing (NLP) and applied to predict player behavior:

It maintains a history of your moves throughout the game.

It builds a pattern table — every sequence of your last 3 moves is recorded along with what move followed it.

When predicting your next move, it looks up your current last-3-move sequence in the table and picks the most frequent follow-up.

It then plays the move that beats your predicted move.

If no pattern exists yet, it falls back to your most frequent move overall, and if that's unavailable, it plays randomly.




📈 AI Confidence Levels
The AI signals how well it knows you:
Status                  Meaning
🤔 Learning             Not enough data, mostly guessing
🧠 Getting smarter      Patterns starting to emerge
🔥 Pattern locked       AI has figured out your tendencies





🛠️ Tech & Concepts Used

Python — core language----

1.collections.defaultdict — efficient pattern/frequency storage

2.N-Gram modeling — sequence-based prediction (same idea used in text prediction)

3.Greedy prediction — always counters the most likely predicted move





🚀 How to Run ---

bashpython rock_paper_scissors.py

No external libraries needed — runs on pure Python! ✅






💡 Key Learning Outcomes

1.Understanding pattern recognition in games

2.Applying frequency-based prediction models

3.Building a simple adaptive AI without machine learning libraries


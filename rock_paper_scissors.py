import random
from collections import defaultdict

# ─── Constants ───────────────────────────────────────────────────────────────
MOVES = ["rock", "paper", "scissors"]
BEAT = {
    "rock": "paper",       # paper beats rock
    "paper": "scissors",   # scissors beats paper
    "scissors": "rock",    # rock beats scissors
}
SHORT = {"r": "rock", "p": "paper", "s": "scissors"}

# ─── AI Brain ────────────────────────────────────────────────────────────────
class PatternAI:
    """
    Learns the player's move patterns using n-gram frequency analysis.
    Looks at the last N moves to predict the next one.
    Falls back to frequency-based or random if no pattern found.
    """
    def __init__(self, pattern_len=3):
        self.pattern_len = pattern_len
        self.history = []                        # player's move history
        self.patterns = defaultdict(lambda: defaultdict(int))
        self.freq = defaultdict(int)             # overall move frequency

    def record(self, move):
        """Record a player's move and update pattern tables."""
        # Update n-gram pattern
        if len(self.history) >= self.pattern_len:
            key = tuple(self.history[-self.pattern_len:])
            self.patterns[key][move] += 1

        self.freq[move] += 1
        self.history.append(move)

    def predict(self):
        """Predict player's next move; return counter-move."""
        predicted = None

        # Try pattern-based prediction (n-gram)
        if len(self.history) >= self.pattern_len:
            key = tuple(self.history[-self.pattern_len:])
            if self.patterns[key]:
                predicted = max(self.patterns[key], key=self.patterns[key].get)

        # Fallback: most frequent move overall
        if predicted is None and self.freq:
            predicted = max(self.freq, key=self.freq.get)

        # Fallback: pure random
        if predicted is None:
            return random.choice(MOVES)

        # Return the move that BEATS the predicted move
        return BEAT[predicted]

    def confidence(self):
        """Return a rough confidence level based on data collected."""
        total = sum(self.freq.values())
        if total < 5:
            return "Learning... 🤔"
        elif total < 15:
            return "Getting smarter... 🧠"
        else:
            return "Pattern locked! 🔥"


# ─── Game Logic ───────────────────────────────────────────────────────────────
def get_winner(player, ai):
    if player == ai:
        return "tie"
    elif BEAT[player] == ai:
        return "ai"
    else:
        return "player"


def print_banner():
    print("\n" + "═" * 45)
    print("   🎮  ROCK  PAPER  SCISSORS  —  AI  MODE")
    print("═" * 45)
    print("  The AI learns YOUR move patterns to beat you!")
    print("  Commands: r=rock  p=paper  s=scissors  q=quit")
    print("═" * 45 + "\n")


def print_scoreboard(scores, total):
    print(f"\n  📊  Score after {total} round(s):")
    print(f"     You: {scores['player']}  |  AI: {scores['ai']}  |  Ties: {scores['tie']}")


def play():
    ai = PatternAI(pattern_len=3)
    scores = {"player": 0, "ai": 0, "tie": 0}
    round_num = 0

    print_banner()

    while True:
        raw = input("  Your move (r/p/s  or  q to quit): ").strip().lower()

        if raw == "q":
            break

        if raw not in SHORT:
            print("  ⚠️  Invalid input. Use r, p, s, or q.\n")
            continue

        player_move = SHORT[raw]
        ai_move = ai.predict()       # AI decides BEFORE recording player move
        ai.record(player_move)       # Now record what player actually did

        round_num += 1
        result = get_winner(player_move, ai_move)
        scores[result] += 1

        # Display round result
        print(f"\n  Round {round_num}")
        print(f"  You played : {player_move.upper()}")
        print(f"  AI  played : {ai_move.upper()}")

        if result == "player":
            print("  ✅  You win this round!")
        elif result == "ai":
            print("  ❌  AI wins this round!")
        else:
            print("  🤝  It's a tie!")

        print(f"  AI status  : {ai.confidence()}")
        print_scoreboard(scores, round_num)
        print()

    # ── Final summary ──
    print("\n" + "═" * 45)
    print("         GAME OVER — FINAL RESULTS")
    print("═" * 45)
    total = round_num or 1
    print(f"  Rounds played : {round_num}")
    print(f"  Your wins     : {scores['player']}  ({scores['player']/total*100:.1f}%)")
    print(f"  AI wins       : {scores['ai']}  ({scores['ai']/total*100:.1f}%)")
    print(f"  Ties          : {scores['tie']}")

    if scores["player"] > scores["ai"]:
        print("\n  🏆  You beat the AI! Well played!")
    elif scores["ai"] > scores["player"]:
        print("\n  🤖  AI wins! It figured out your pattern!")
    else:
        print("\n  🤝  It's a draw overall!")

    print("═" * 45 + "\n")


# ─── Entry Point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    play()

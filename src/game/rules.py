# Explanation of the Game "10,000" Rules

# Scoring Methods

# 1. Single Dice Values:
#    - A single five is worth 50 points.
#    - A single one is worth 100 points.

# 2. Three of a Kind:
#    - Rolling three of the same number scores 100 points multiplied by the number rolled.
#    - Exception: If the number rolled is one, it scores 1,000 points instead.

# 3. Multiple of a Kind:
#    - For four, five, or six of the same number, the score is doubled for each additional die.
#      For example:
#      - Four threes score 600 points (3 x 100 = 300, doubled to 600).
#      - Five threes score 1,200 points (4 x 100 = 400, doubled again).
#    - Maximum score for rolling six ones is 8,000 points.

# 4. Straight:
#    - A straight (rolling the numbers 1 through 6) scores 1,500 points.
#    - If a player does not roll a straight, they get one chance to complete it by rerolling the missed numbers.
#    - If the reroll fails, the round is a "crap out" and no points are scored.

# 5. Three Pairs:
#    - Rolling three pairs (e.g., 2+2, 4+4, 5+5) scores 1,000 points.
#    - This rule does not apply if the roll consists of a quadruple and a pair (e.g., 2+2, 2+2, 6+6).

# General Scoring Rules

# - Dice must be rolled simultaneously to score as three of a kind.
# - In progressive scoring, players can combine dice from previous rolls to score higher.
# - A full house cannot be formed if four of a kind is already present. The player needs to reroll one of the four to form a proper full house.

# Example:
# - Player rolls six dice and gets three fours, scoring 400 points.
# - Player rerolls three dice and gets a 2, 4, and 5.
# - The additional four does not multiply the previous score unless playing progressive scoring, 
#   so the player only scores 50 points for the single 5.
# - If the player later rolls two more 5s, they each score 50 points (no three-of-a-kind bonus with the earlier 5).


class Rules:
    def __init__(self):
        self.score_rules = {
            1: 100,  # 1s are worth 100 points
            5: 50,   # 5s are worth 50 points
        }

    def calculate_score(self, dice_rolls):
        score = 0
        counts = {i: dice_rolls.count(i) for i in range(1, 7)}

        # Scoring for three or more of a kind
        for num, count in counts.items():
            if count >= 3:
                if num == 1:
                    score += 1000  # Three 1s are worth 1000 points
                else:
                    score += num * 100  # Three of any other number is worth 100 times the number

                counts[num] -= 3  # Remove the counted dice

        # Scoring for remaining 1s and 5s
        score += counts[1] * self.score_rules[1]
        score += counts[5] * self.score_rules[5]

        # Scoring for a straight (1 through 6)
        if all(counts[i] == 1 for i in range(1, 7)):
            score += 1500

        # Scoring for three pairs
        pairs = [num for num, count in counts.items() if count == 2]
        if len(pairs) == 3:
            score += 1000

        return score

    def check_special_rolls(self, roll_results):
        counts = {i: roll_results.count(i) for i in range(1, 7)}

        # Check if the roll results in three pairs
        if len([num for num, count in counts.items() if count == 2]) == 3:
            return "three_pairs"

        # Check if the roll results in a straight (1 through 6)
        if all(counts[i] == 1 for i in range(1, 7)):
            return "straight"

        return None

    def is_valid_move(self, dice_rolls):
        # Implement logic to check if the move is valid based on the game rules
        return True  # Placeholder for actual validation logic

    def handle_no_scoring_dice(self, roll_results):
        if not any(d in [1, 5] or roll_results.count(d) >= 3 for d in roll_results):
            return True
        return False

    def handle_pair_roll(self, roll_results):
        if len(roll_results) == 2 and roll_results[0] == roll_results[1]:
            return True
        return False
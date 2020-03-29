from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Info from structure of problem
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    # Info from given statements
    Biconditional(AKnight, And(AKnight, AKnave))
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Info from structure of problem
    Or(AKnight, AKnave),                # A is either a knight or a knave
    Implication(AKnight, Not(AKnave)),  # A cannot be a knave if it is a knight
    Or(BKnight, BKnave),                # Similarly for B
    Implication(BKnight, Not(BKnave)),

    # Info from give statements
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(    
    # Info from structure of problem
    Or(AKnight, AKnave),                # A is either a knight or a knave
    Implication(AKnight, Not(AKnave)),  # A cannot be a knave if it is a knight
    Or(BKnight, BKnave),                # Similarly for B
    Implication(BKnight, Not(BKnave)),

    # Info from give statements
    Biconditional(AKnight, Or(And(AKnight, BKnight),
                              And(AKnave, BKnave))),
    Biconditional(BKnight, Or(And(AKnight, BKnave),
                              And(AKnave, BKnight)))
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Info from structure of problem
    Or(AKnight, AKnave),                # A is either a knight or a knave
    Implication(AKnight, Not(AKnave)),  # A cannot be a knave if it is a knight
    Or(BKnight, BKnave),                # Similarly for B
    Implication(BKnight, Not(BKnave)),
    Or(CKnight, CKnave),                # Similarly for C
    Implication(CKnight, Not(CKnave)),

    # Info from give statements
    
    Biconditional(Or(AKnight, AKnight),
                  Or(AKnight, AKnave)),
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

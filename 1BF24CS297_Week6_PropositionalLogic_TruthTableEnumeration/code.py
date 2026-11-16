
from itertools import product

# Check whether an implication is true
def implies(a, b):
    return (not a) or b


# Check whether the Knowledge Base is true
def PL_TRUE_KB(model):
    P = model["P"]
    Q = model["Q"]
    R = model["R"]

    return (
        implies(Q, P) and
        implies(P, not Q) and
        (Q or R)
    )


# Check whether the query is true
def PL_TRUE(query, model):
    P = model["P"]
    Q = model["Q"]
    R = model["R"]

    if query == "R":
        return R

    elif query == "R -> P":
        return implies(R, P)

    elif query == "Q -> R":
        return implies(Q, R)


# Truth Table Enumeration Algorithm
def TT_ENTAILS(query):

    symbols = ["P", "Q", "R"]

    print("\nP Q R | Q->P P->~Q Q|R | KB |", query)
    print("-" * 48)

    entails = True

    for values in product([False, True], repeat=3):

        model = dict(zip(symbols, values))

        P = model["P"]
        Q = model["Q"]
        R = model["R"]

        # Evaluate individual KB sentences
        sentence1 = implies(Q, P)
        sentence2 = implies(P, not Q)
        sentence3 = Q or R

        # Evaluate complete KB
        KB = sentence1 and sentence2 and sentence3

        # Evaluate query
        result = PL_TRUE(query, model)

        # Print truth table
        print(
            P, Q, R, "|",
            sentence1, sentence2, sentence3,
            "|", KB, "|", result
        )

        # Check entailment only when KB is true
        if KB and not result:
            entails = False

    return entails


# Main program
queries = ["R", "R -> P", "Q -> R"]

for query in queries:
    print("\nChecking KB entails", query)

    if TT_ENTAILS(query):
        print("Result: YES, KB entails", query)
    else:
        print("Result: NO, KB does not entail", query)

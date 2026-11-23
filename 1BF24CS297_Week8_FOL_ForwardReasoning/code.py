# Forward Chaining in First Order Logic

facts = [
    ("American", "Robert"),
    ("Missile", "T1"),
    ("Owns", "A", "T1"),
    ("Enemy", "A", "America")
]

rules = [
    ([("Missile", "?x"), ("Owns", "A", "?x")],
     ("Sells", "Robert", "?x", "A")),

    ([("Missile", "?x")],
     ("Weapon", "?x")),

    ([("Enemy", "?x", "America")],
     ("Hostile", "?x")),

    ([("American", "?p"), ("Weapon", "?q"),
      ("Sells", "?p", "?q", "?r"), ("Hostile", "?r")],
     ("Criminal", "?p"))
]


def match(pattern, fact, substitution):
    if pattern[0] != fact[0]:
        return None

    for p, f in zip(pattern, fact):
        if p.startswith("?"):
            if p in substitution:
                if substitution[p] != f:
                    return None
            else:
                substitution[p] = f
        elif p != f:
            return None

    return substitution


def forward_chaining(facts, rules):
    new_facts = True

    while new_facts:
        new_facts = False

        for conditions, conclusion in rules:
            substitutions = [{}]

            for condition in conditions:
                new_substitutions = []

                for sub in substitutions:
                    for fact in facts:
                        result = match(condition, fact, sub.copy())

                        if result is not None:
                            new_substitutions.append(result)

                substitutions = new_substitutions

            for sub in substitutions:
                new_fact = tuple(
                    sub.get(item, item) for item in conclusion
                )

                if new_fact not in facts:
                    facts.append(new_fact)
                    new_facts = True
                    print("Inferred:", new_fact)

    return facts


# Run Forward Chaining
result = forward_chaining(facts, rules)

# Check the goal
if ("Criminal", "Robert") in result:
    print("\nGoal proved: Robert is Criminal")
else:
    print("\nGoal not proved")

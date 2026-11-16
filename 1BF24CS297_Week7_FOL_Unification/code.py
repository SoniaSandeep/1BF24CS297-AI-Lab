
def is_variable(x):
    return isinstance(x, str) and x.islower() and x.isalpha()


def occurs_check(var, expr):
    if var == expr:
        return True
    if isinstance(expr, tuple):
        return any(occurs_check(var, item) for item in expr)
    return False


def substitute(expr, substitutions):
    if isinstance(expr, str):
        while expr in substitutions:
            expr = substitutions[expr]
        return expr

    if isinstance(expr, tuple):
        return tuple(substitute(x, substitutions) for x in expr)

    return expr


def unify(x, y, substitutions):
    x = substitute(x, substitutions)
    y = substitute(y, substitutions)

    if x == y:
        return substitutions

    if is_variable(x):
        if occurs_check(x, y):
            return None
        substitutions[x] = y
        return substitutions

    if is_variable(y):
        if occurs_check(y, x):
            return None
        substitutions[y] = x
        return substitutions

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y):
            return None

        if x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            substitutions = unify(a, b, substitutions)

            if substitutions is None:
                return None

        return substitutions

    return None


# Main program
print("UNIFICATION ALGORITHM")
print("---------------------")

# Example expressions:
# Eats(x, Apple)
# Eats(Riya, y)

expr1 = ("Eats", "x", "Apple")
expr2 = ("Eats", "Riya", "y")

print("\nExpression 1:", expr1)
print("Expression 2:", expr2)

result = unify(expr1, expr2, {})

if result is None:
    print("\nUnification FAILED")
else:
    print("\nUnification SUCCESSFUL")
    print("Substitutions:")

    for var, value in result.items():
        print(var, "=", value)

    print("\nUnified Expression:")
    print(substitute(expr1, result))

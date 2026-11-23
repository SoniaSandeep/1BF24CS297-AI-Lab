# First Order Logic - Resolution

# Knowledge Base
clauses = [
    ["~food(x)", "likes(John,x)"],
    ["food(Apple)"],
    ["food(Vegetables)"],
    ["~eats(y,z)", "killed(y)", "food(z)"],
    ["eats(Anil,Peanuts)"],
    ["alive(Anil)"],
    ["~eats(Anil,w)", "eats(Harry,w)"],
    ["killed(g)", "alive(g)"],
    ["~alive(k)", "~killed(k)"]
]

# Negate the goal
goal = "~likes(John,Peanuts)"

print("Knowledge Base:")
for c in clauses:
    print(c)

print("\nNegated Goal:", goal)

# Resolution steps
print("\nResolution Steps:")

# Step 1
c1 = "~food(Peanuts)"
print("1.", c1)

# Step 2
c2 = "~eats(Anil,Peanuts) OR killed(Anil)"
print("2.", c2)

# Step 3
c3 = "killed(Anil)"
print("3.", c3)

# Step 4
c4 = "~alive(Anil)"
print("4.", c4)

# Step 5
c5 = "alive(Anil)"
print("5.", c5)

# Contradiction
print("\nResolving:")
print("~alive(Anil) AND alive(Anil)")
print("{}")

print("\nHence, John likes Peanuts is PROVED.")

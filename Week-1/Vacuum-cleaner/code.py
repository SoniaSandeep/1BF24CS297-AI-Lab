# Vacuum Cleaner Agent

rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

position = input("Enter vacuum position (A/B): ").upper()

while True:

    print("\nCurrent State:")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("Vacuum Position:", position)

    # Simple Reflex Agent
    if rooms[position] == "Dirty":

        print("Action: SUCK")
        rooms[position] = "Clean"

    else:

        # Move to the other room
        if position == "A":
            position = "B"
            print("Action: MOVE RIGHT")
        else:
            position = "A"
            print("Action: MOVE LEFT")

    # Goal-based condition
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nGoal achieved!")
        print("Both rooms are clean.")
        break

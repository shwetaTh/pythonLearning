# initial state
left_bank = {"M", "G", "g", "f"}  # M = man, G = goat, g = grass, f = fox
right_bank = set()
boat = [None, None]  # boat can hold two items or be empty

def going_across(direction, boat_space1, boat_space2):
    global left_bank, right_bank, boat

    if direction == "l-r":
        left_bank.discard(boat_space1)
        left_bank.discard(boat_space2)
        right_bank.update({boat_space1, boat_space2})

    elif direction == "r-l":
        right_bank.discard(boat_space1)
        right_bank.discard(boat_space2)
        left_bank.update({boat_space1, boat_space2})

    boat = [None, None]

print("initial state:")
print(f"left bank: {left_bank}")
print(f"right bank: {right_bank}")
print()

boat = ["M", "G"]
going_across("l-r", boat[0], boat[1])
print("after move 1 (l-r):")
print(f"left bank: {left_bank}")
print(f"right bank: {right_bank}")
print()

boat = ["M", None]
going_across("r-l", boat[0], boat[1])
print("after move 2 (r-l):")
print(f"left bank: {left_bank}")
print(f"right bank: {right_bank}")
print()

boat = ["M", "g"]
going_across("l-r", boat[0], boat[1])
print("after move 3 (l-r):")
print(f"left bank: {left_bank}")
print(f"right bank: {right_bank}")
print()

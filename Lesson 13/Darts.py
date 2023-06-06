# Read user input
player_name = input()
retire = False
points = 301
good_shot = 0
bad_shot = 0
# Logic
while not retire:
    multiplier = input()
    score = input()

    if multiplier == "Retire" or score == "Retire":
        retire = True
        break

    if multiplier == 'Single':
        score = int(score)
    elif multiplier == 'Double':
        score = 2 * int(score)
    elif multiplier == 'Triple':
        score = 3 * int(score)

    if points > 0 and int(score) <= points:
        points -= score
        good_shot += 1
        if points == 0:
            print(f"{player_name} won the leg with {good_shot} shots.")
            break
    else:
        bad_shot += 1
        continue
# Output
if retire:
    print(f"{player_name} retired after {bad_shot} unsuccessful shots.")


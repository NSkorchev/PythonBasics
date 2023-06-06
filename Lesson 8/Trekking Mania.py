# Read user input
group = int(input())
total_people = 0
mussala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

# Logic
for i in range(0, group):
    people_in_group = int(input())
    total_people += people_in_group

    if people_in_group <= 5:
        mussala += people_in_group
    elif 6 <= people_in_group <= 12:
        montblanc += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

# Output
print(f"{mussala / total_people * 100:.2f}%")
print(f"{montblanc / total_people * 100:.2f}%")
print(f"{kilimanjaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")

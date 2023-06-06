# Read user input
time_period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
# Logic
for i in range(1, time_period + 1):
    patients = int(input())
    if i % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1

    if patients > doctors:
        untreated_patients += (patients - doctors)
        treated_patients += doctors
    else:
        treated_patients += patients
# Output
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")





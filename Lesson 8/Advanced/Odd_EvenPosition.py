from sys import maxsize
# Read user input
sum_odd, sum_even = 0, 0
odd_min, even_min = maxsize, maxsize
odd_max, even_max = -maxsize, -maxsize

# Logic
for i in range(1, int(input()) + 1):
    number = float(input())

    if i % 2 == 0:
        sum_even += number

        if number < even_min:
            even_min = number
        if number > even_max:
            even_max = number

    else:
        sum_odd += number

        if number < odd_min:
            odd_min = number
        if number > odd_max:
            odd_max = number

# Output
print(f"OddSum={sum_odd:.2f},")
print(f"OddMin=" + f"{odd_min:.2f}," if odd_min != maxsize else "OddMin=No,")
print(f"OddMax=" + f"{odd_max:.2f}," if odd_max != -maxsize else "OddMax=No,")
print(f"EvenSum={sum_even:.2f},")
print(f"EvenMin=" + f"{even_min:.2f}," if even_min != maxsize else "EvenMin=No,")
print(f"EvenMax=" + f"{even_max:.2f}" if even_max != -maxsize else "EvenMax=No")
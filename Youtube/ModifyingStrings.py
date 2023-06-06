# Read user input
text = "X-DSPAM-Confidence:    0.8475"

# Logic
y = text.find('0.')
z = text[y:]
num = float(z)

# Output
print(num)

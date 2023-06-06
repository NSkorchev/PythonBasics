# Read user input
yearly_tax = int(input())
# Logic
shoes = yearly_tax - 0.4 * yearly_tax
outfit = shoes - 0.2 * shoes
ball = 0.25 * outfit
accessories = 0.2 * ball

total = yearly_tax + shoes + outfit + ball + accessories

# Output
# print(shoes)
# print(outfit)
# print(ball)
# print(accessories)

print(total)

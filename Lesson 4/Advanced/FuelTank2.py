# Read user input
fuel_type = input()
fuel = float(input())
club_card = input()
gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
total_price = 0

if club_card == 'Yes':
    diesel_price = diesel_price - 0.12
    gasoline_price = gasoline_price - 0.18
    gas_price = gas_price - 0.08

# Logic
# Output
while True:

    if fuel_type == 'Diesel' and fuel > 25:
        total_price = diesel_price * fuel * 0.9
        print(f"{total_price:.2f} lv.")
        break
    elif fuel_type == 'Diesel' and 20 < fuel <= 25:
        total_price = diesel_price * fuel * 0.92
        print(f"{total_price:.2f} lv.")
        break
    elif fuel_type == 'Diesel' and 20 > fuel:
        total_price = diesel_price * fuel
        print(f"{total_price:.2f} lv.")
        break
    elif fuel_type == 'Gasoline' and fuel > 25:
        total_price = gasoline_price * fuel * 0.9
        print(f"{total_price:.2f} lv.")
        break
    elif fuel_type == 'Gasoline' and 20 < fuel <= 25:
        total_price = gasoline_price * fuel * 0.92
        print(f"{total_price:.2f} lv.")
        break
    elif fuel_type == 'Gasoline' and 20 > fuel:
        total_price = gasoline_price * fuel
        print(f"{total_price:.2f} lv.")
        break
    elif fuel_type == 'Gas' and fuel > 25:
        total_price = gas_price * fuel * 0.9
        print(f"{total_price:.2f} lv.")
        break
    elif fuel_type == 'Gas' and 20 < fuel <= 25:
        total_price = gas_price * fuel * 0.92
        print(f"{total_price:.2f} lv.")
        break
    elif fuel_type == 'Gas' and 20 > fuel:
        total_price = gas_price * fuel
        print(f"{total_price:.2f} lv.")
        break

    else:
        print('Invalid fuel!')
        break

# tip_gorivo = input()
# volume = float(input())
# club_card = input()
#
# gorivo_prices = [2.22, 2.33, 0.93]  # ceni na gorivata Gasoline Diesel Gas
# discount_with_club_card = [0.18, 0.12, 0.08]  # namalenie na gorivata Gasoline Diesel Gas
#
# # namalenie w procenti
# if volume > 25:
#     volume_discount = 10 / 100
# elif 20 <= volume <= 25:
#     volume_discount = 8 / 100
# else:
#     volume_discount = 0 / 100
#
# if tip_gorivo == "Gasoline":
#     if club_card == "No":
#         gorivo_price = gorivo_prices[0]
#     else:
#         gorivo_price = gorivo_prices[0] - discount_with_club_card[0]
# elif tip_gorivo == "Diesel":
#     if club_card == "No":
#         gorivo_price = gorivo_prices[1]
#     else:
#         gorivo_price = gorivo_prices[1] - discount_with_club_card[1]
# else:
#     if club_card == "No":
#         gorivo_price = gorivo_prices[2]
#     else:
#         gorivo_price = gorivo_prices[2] - discount_with_club_card[2]
#
# final_amount_before_discount = volume * gorivo_price
# final_amount = final_amount_before_discount - (final_amount_before_discount * volume_discount)
# print(f"{final_amount:0.2f} lv.")

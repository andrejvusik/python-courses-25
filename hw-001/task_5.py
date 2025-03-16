# Task 5. Exchanging money
# Enter the amount in rubles (an integer). Determine how many 100, 50, 10, 5, and 1 ruble bills
# will be needed to exchange it.

amount_of_money = int(input("Enter the amount in rubles (whole number): "))

number_banknotes_100 = amount_of_money // 100
number_banknotes_50 = amount_of_money % 100 // 50
number_banknotes_10 = amount_of_money % 50 // 10
number_banknotes_5 = amount_of_money % 10 // 5
number_banknotes_1 = amount_of_money % 5 // 1

print(f"To exchange an amount equal to {amount_of_money} rub you will need: ")
if number_banknotes_100: print(f"- banknotes of 100 rubles: {number_banknotes_100}")
if number_banknotes_50: print(f"- banknotes of 50 rubles: {number_banknotes_50}")
if number_banknotes_10: print(f"- banknotes of 10 rubles: {number_banknotes_10}")
if number_banknotes_5: print(f"- banknotes of 5 rubles: {number_banknotes_5}")
if number_banknotes_1: print(f"- banknotes of 1 ruble: {number_banknotes_1}")

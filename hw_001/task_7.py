# Task 7. Time format
# Enter the number of seconds and convert them to minutes and seconds,
# for example, 75 → 1 minute 15 seconds.

number_of_second = int(input("Enter number of seconds: "))

minutes = number_of_second // 60
seconds = number_of_second % 60

print(f"{number_of_second} seconds like is {minutes} minute and {seconds} seconds")

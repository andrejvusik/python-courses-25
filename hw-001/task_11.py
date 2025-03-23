# Task 11. Checking the IP address
# Enter a string. Check if it is a valid IP address (the format
# should be XXX.XXX.XXX.XXX, where XXX is a number from 0 to 255).

testing_ip = input("Please enter the IP address to check if it is correct: ")
valid_ip = 1

if testing_ip.count(".") != 3:
    print(f"The entered IP address \"{testing_ip}\" is NOT correct.")
    valid_ip = 0
else:
    testing_ip_parts = testing_ip.split(".")
    for part in testing_ip_parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            print(f"The entered IP address \"{testing_ip}\" is NOT correct.")
            valid_ip = 0
            break

if valid_ip:
    print(f"The entered IP address \"{testing_ip}\" is correct.")

# Task 11. Checking the IP address
# Enter a string. Check if it is a valid IP address (the format
# should be XXX.XXX.XXX.XXX, where XXX is a number from 0 to 255).

test_string = input("Please enter the IP address to check if it is correct: ")

if test_string.count(".") == 3:
    test_list = test_string.split(".")
    if test_list[0].isdigit() and test_list[1].isdigit() and test_list[2].isdigit() and test_list[3].isdigit():
        if 0 <= int(test_list[0]) <= 255 and 0 <= int(test_list[1]) <= 255 and 0 <= int(
                test_list[2]) <= 255 and 0 <= int(test_list[3]) <= 255:
            print(f"The entered IP address \"{test_string}\" is correct.")
        else:
            print(f"The entered IP address \"{test_string}\" is NOT correct.")
    else:
        print(f"The entered IP address \"{test_string}\" is NOT correct.")
else:
    print(f"The entered IP address \"{test_string}\" is NOT correct.")

temp_choice = input("Enter what you would like to convert from? (Enter the number)\n"
                    "1)Celsius \n"
                    "2)Fahrenheit \n")
if temp_choice == "1":
    temp1 = input("Enter the temperature: ")
    temp1 = float(temp1[:-1])
    temp2 = (temp1 * 1.8) + 32
    print("This is the temperature in Fahrenheit " + str(temp2) +"F")
elif temp_choice == "2":
    temp1 = input("Enter the temperature: ")
    temp1 = float(temp1[:-1])
    temp2 = (temp1 -32) / 1.8
    print("This is the temperature in Celsius " + str(temp2) + "C")

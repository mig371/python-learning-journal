kilometers = float(input("Enter distance in kilometers: "))
miles = float(input("Enter distance in miles: "))

kilometers_to_miles = kilometers * 0.621371
miles_to_kilometers = miles / 0.621371

print(f"{kilometers} kilometers is equal to {kilometers_to_miles:.2f} miles.")
print(f"{miles} miles is equal to {miles_to_kilometers:.2f} kilometers.")

# i made this code for both ways in conversion, so you can convert kilometers to miles and miles to kilometers. i know the instructions were "Kilometer to Mile Conversion" but i thought it would be more useful to have both conversions in one program. also i know you wanted us to learn in colab on google but i made this code in Visual Studio Code. just because i am more familiar with it. i hope this is okay.
# also i surched up things outside this class and learned of how to use f strings https://youtu.be/d1m_ej68Uiw?si=x3N_Yn4SuNle7_EL
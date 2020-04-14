first_number = float(input("In this program you will insert three *different* float numbers to view decreasing order"
                           "\ninsert the first float number: "))
second_number = float(input("insert the second float number: "))
third_number = float(input("insert the third float number: "))

print(first_number, "-", second_number, "-", third_number)

if first_number > second_number > third_number:
    print("Decreasing order: ", first_number, "-", second_number, "-", third_number)
elif first_number > third_number > second_number:
    print("Decreasing order: ", first_number, "-", third_number, "-", second_number)
elif second_number > first_number > third_number:
    print("Decreasing order: ", second_number, "-", first_number, "-", third_number)
elif second_number > third_number > first_number:
    print("Decreasing order: ", second_number, "-", third_number, "-", first_number)
elif third_number > second_number > first_number:
    print("Decreasing order: ", third_number, "-", second_number, "-", first_number)
elif third_number > first_number > second_number:
    print("Decreasing order: ", third_number, "-", first_number, "-", second_number)

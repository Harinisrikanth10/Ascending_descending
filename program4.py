arr = [95, 82, 78, 51, 99]
choice = int(input("Enter 1 for Ascending or 2 for Descending: "))
if choice == 1:
    arr.sort()
    print("Ascending Order:", arr)
elif choice == 2:
    arr.sort(reverse=True)
    print("Descending Order:", arr)
else:
    print("Invalid Choice")
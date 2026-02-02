n = int(input())
month = n % 100
if 3 <= month <= 5:
    print("spring")
elif 6 <= month <= 8:
    print("summer")
elif 9 <= month <= 11:
    print("autumn")
else:
    print("winter")
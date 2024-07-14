food = input("Enter food type (V for Veg, N for Non-Veg): ")
n = int(input("Enter quantity: "))
dis = int(input("Enter distance in kms: "))

if dis > 0 and n > 0 and (food == 'V' or food == 'N'):
    if dis <= 3:
        bill = 0
    elif 4 <= dis <= 6:
        bill = 3 * (dis - 3)
    else:
        bill = 3 * 3 + 6 * (dis - 6)

    if food == 'V':
        bill += n * 120
    elif food == 'N':
        bill += n * 150
else:
    bill = -1

print("Total bill:", bill)

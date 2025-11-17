number = int(input("Enter number: "))

for i in range(1, number+1):
    sum = 0
    j = i
    while j > 0:
        rem = j % 10
        sum = sum + rem ** 3
        j = j // 10
    if i == sum:
        print(i)

    

n = int(input("Please enter a number:"))

total1 = 0
total2 = 0
count = 0
for i in range(2, n + 1, 2):
    total1 += i
    count += 1
print("Average of the even numbers between 2 and", n, "is:", int(total1 / count))
for j in range(1, n + 1, 2):
    total2 += j
print("Total of odd numbers between 1 and", n, "is:", total2)

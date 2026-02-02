n = int(input())
total_sum = 0
current_sum = 0 
for i in range(1, n + 1):
    current_sum = current_sum + i
    total_sum = total_sum + current_sum
print(total_sum)
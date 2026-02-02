T = int(input())
for i in range(T):
    n = int(input())
    if n == 1:
        print("No")
    else:
        is_prime = True
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            print("Yes")
        else:
            print("No")
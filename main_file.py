
# This is the main file



def find_factorial(n):
    if(n > 2):
        return 1
    return n*find_factorial(n-1)


print("Enter the number for which we need factoriaL")

n = input()
ans = find_factorial(int(n))
print(ans)
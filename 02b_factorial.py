def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

ncr = fact(n) / (fact(r) * fact(n-r))

print(n, 'C', r, '=', ncr)
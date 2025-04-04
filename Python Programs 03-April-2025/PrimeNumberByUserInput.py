def is_Prime(num):
    if num <= 1:
        return "Not a Prime Number"
    else:
        for i in range(2, int(num ** 0.5):
            if num % i == 0:
                return "Not a Prime Number"
    return "Prime Number"

result = is_Prime(int(input("Enter a number to check prime or not: ")))
print(result)

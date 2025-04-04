
def is_Prime(num):
    if num <=1: # other use the condition like (num < 2)
        return False
    else:
        for i in range(2, int(num ** 0.5):
            if num % i == 0:
                return False
    return True

print(is_Prime(10))# False because 10 is not prime number
print(is_Prime(7))# True because 7 is prime number

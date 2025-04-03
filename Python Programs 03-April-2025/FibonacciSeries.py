def is_Fibo(num):
     a, b = 0, 1
     for _ in range(num):
        print(a, end=" ")  
        a, b = b, a + b  
is_Fibo(10)
# method ---- 1
import time

def decimal_to_binary_conversion(num):
    if num == 0:
        return
    decimal_to_binary_conversion(num//2)
    print(num%2,end="")
def decimal_to_binary_conversion2(num):
    if num == 0:
        return ""
    decimal_to_binary_conversion2(num//2)
    result = decimal_to_binary_conversion2(num//2) + str(num%2)
    return result

def fun(n):
    if n == 0:
        return
    print(n)
    fun(n - 1)

def fun1(n):
    if n == 0:
        return
    fun1(n - 1)
    print(n)


start = time.perf_counter()
fun(1000)
end = time.perf_counter()

print(f"fun time: {end - start:.6f} seconds")


start = time.perf_counter()
fun1(1000)
end = time.perf_counter()

print(f"fun1 time: {end - start:.6f} seconds")
print(decimal_to_binary_conversion2(8))


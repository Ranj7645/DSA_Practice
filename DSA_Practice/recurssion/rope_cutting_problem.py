def maximimumPiecesOfRopes(n,a,b,c):

    if n == 0:
        return 0
    if n < 0:
        return -1
    res = max((maximimumPiecesOfRopes(n-a,a,b,c)), (maximimumPiecesOfRopes(n-b,a,b,c)), (maximimumPiecesOfRopes(n-c,a,b,c)))
    if res == -1:
        return -1
    else :
        return res+1

n = 3
a = 3
b = 2
c = 1

result = maximimumPiecesOfRopes(n,a,b,c)
print(f"maximum number of rope pieces could be {result}")
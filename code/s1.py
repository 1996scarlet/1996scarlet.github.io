def spiralOrder(matrix):
    res, count = [], 0
    while matrix:
        for item in matrix.pop(0):
            count += 1
            if count%10 ==7 and (count//10) & 1:
                res.append(item)

        matrix = list(zip(*matrix))
        matrix.reverse()
    
    return res

M, N = map(int, input().split())

matrix = []
for i in range(M):
    matrix.append([[i, j] for j in range(N)])

print(spiralOrder(matrix))

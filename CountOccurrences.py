from collections import defaultdict
def threeByN(matrix):
    
    d = defaultdict(set)
    n = len(matrix[0])
    for i in range(3):
        for j in range(3):
            pos = 0
            k = j
            while k < (n) and pos < (n - 2):
                d[pos].add(matrix[i][k])
                pos += 1
                k += 1
    table = [True] * (n - 2)
    for key, value in d.items():
        if len(value) != 9:
            table[key] = False
    return table
    
matrix = [[1, 2, 3, 2, 5, 7],
          [4, 5, 6, 1, 7, 6],
          [7, 8, 9, 4, 8, 3]]
          
matrix2 = [[1, 2, 3, 2],
          [4, 5, 6, 1],
          [7, 8, 9, 4]]

matrix1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(threeByN(matrix))               

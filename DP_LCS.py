def LCSubStr(X, Y, m, n):
 
    # Inicializacion de la tabla con cero en cada celda
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]
 

    # Guarda el resultado final de la longitud de la subcadena
    result = 0
 
    # LCSuff[m+1][n+1] se construye de forma bottom up
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result
 
 
# X = 'Computer Science'
# Y = 'Comp-Sci'
 
# m = len(X)
# n = len(Y)
 
# print('La longitud de la subcadena mas larga es:',
#       LCSubStr(X, Y, m, n))
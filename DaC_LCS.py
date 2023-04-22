def lcs_divide_and_conquer(X, Y):
    # Base case: if one of the strings is empty, return an empty string as LCS
    if len(X) == 0 or len(Y) == 0:
        return ""
    
    # Divide: Encontrar el centro de cada string
    midX = len(X) // 2
    midY = len(Y) // 2
    
    # Conquer: Encontrar recursivamente los LCS de cada par de subcadenas
    if X[midX] == Y[midY]:
        # Si los caracteres de las mitades coinciden se incluyen en el LCS resultante
        return lcs_divide_and_conquer(X[:midX], Y[:midY]) + X[midX] + lcs_divide_and_conquer(X[midX+1:], Y[midY+1:])
    else:
        # Sino, el LCS muestra dos posible sub solucion y presenta la mas larga
        return max(lcs_divide_and_conquer(X[:midX], Y), lcs_divide_and_conquer(X, Y[:midY]), key=len)

result = lcs_divide_and_conquer('Computer Science', 'Comp-Sci')
print(result)
print('de longitud:', len(result))
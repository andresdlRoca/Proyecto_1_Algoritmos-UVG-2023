def lcs_divide_and_conquer(X, Y):
    """
    This function takes two strings X and Y as input and returns the longest common substring between them using the divide and conquer approach.
    """
    def lcs_helper(X, Y, l1, r1, l2, r2):
        if l1 > r1 or l2 > r2:
            return ""
        if r1 - l1 == 0:
            if X[l1] in Y[l2:r2+1]:
                return X[l1]
            else:
                return ""
        mid1 = (l1 + r1) // 2
        mid2 = (l2 + r2) // 2
        left_lcs = lcs_helper(X, Y, l1, mid1, l2, mid2)
        right_lcs = lcs_helper(X, Y, mid1+1, r1, mid2+1, r2)
        cross_lcs = find_cross_lcs(X, Y, l1, r1, l2, r2)
        if len(left_lcs) >= len(right_lcs) and len(left_lcs) >= len(cross_lcs):
            return left_lcs
        elif len(right_lcs) >= len(left_lcs) and len(right_lcs) >= len(cross_lcs):
            return right_lcs
        else:
            return cross_lcs

    def find_cross_lcs(X, Y, l1, r1, l2, r2):
        mid1 = (l1 + r1) // 2
        mid2 = (l2 + r2) // 2
        max_len = 0
        lcs = ""
        i = mid1
        while i >= l1:
            j = mid2
            while j <= r2:
                if X[i] == Y[j]:
                    k = 0
                    while i-k >= l1 and j-k >= l2 and X[i-k] == Y[j-k]:
                        k += 1
                    if k > max_len:
                        max_len = k
                        lcs = X[i-k+1:i+1]
                j += 1
            i -= 1
        return lcs

    n1 = len(X)
    n2 = len(Y)
    return lcs_helper(X, Y, 0, n1-1, 0, n2-1)
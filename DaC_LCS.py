import sys

def lcs_divide_and_conquer(s1, s2):
    """
    This function takes two strings s1 and s2 as input and returns the longest common substring between them using the divide and conquer approach.
    """
    def lcs_helper(s1, s2, l1, r1, l2, r2):
        if l1 > r1 or l2 > r2:
            return ""
        if r1 - l1 == 0:
            if s1[l1] in s2[l2:r2+1]:
                return s1[l1]
            else:
                return ""
        mid1 = (l1 + r1) // 2
        mid2 = (l2 + r2) // 2
        left_lcs = lcs_helper(s1, s2, l1, mid1, l2, mid2)
        right_lcs = lcs_helper(s1, s2, mid1+1, r1, mid2+1, r2)
        cross_lcs = find_cross_lcs(s1, s2, l1, r1, l2, r2)
        if len(left_lcs) >= len(right_lcs) and len(left_lcs) >= len(cross_lcs):
            return left_lcs
        elif len(right_lcs) >= len(left_lcs) and len(right_lcs) >= len(cross_lcs):
            return right_lcs
        else:
            return cross_lcs

    def find_cross_lcs(s1, s2, l1, r1, l2, r2):
        mid1 = (l1 + r1) // 2
        mid2 = (l2 + r2) // 2
        max_len = 0
        lcs = ""
        i = mid1
        while i >= l1:
            j = mid2
            while j <= r2:
                if s1[i] == s2[j]:
                    k = 0
                    while i-k >= l1 and j-k >= l2 and s1[i-k] == s2[j-k]:
                        k += 1
                    if k > max_len:
                        max_len = k
                        lcs = s1[i-k+1:i+1]
                j += 1
            i -= 1
        return lcs

    n1 = len(s1)
    n2 = len(s2)
    return lcs_helper(s1, s2, 0, n1-1, 0, n2-1)
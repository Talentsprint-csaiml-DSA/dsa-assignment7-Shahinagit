#Given two strings X and Y, find the length of their longest common subsequence (LCS) 
#and optionally return the subsequence itself.

def longest_common_subsequence(X, Y):
    A, B = len(X), len(Y)
    
    # Create a pt table with initialization to store lengths of LCS
   #pt = [[0] * (B + 1) for _ in range(A + 1)]
    pt = [[0 for _ in range(B + 1)] for _ in range(A+1)]
       
    # Build the dp table
    for i in range(1, A + 1):
        for j in range(1, B + 1):
            if X[i - 1] == Y[j - 1]:
                pt[i][j] = pt[i - 1][j - 1] + 1
            else:
                pt[i][j] = max(pt[i - 1][j], pt[i][j - 1])
    
    # Length of LCS is in pt[A][B]
    lcs_length = pt[A][B]
    
    # Reconstruct the LCS from the pt table
    lcs = []
    i, j = A, B
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif pt[i - 1][j] >= pt[i][j - 1]:
            i = i-1
        else:
            j = j-1
    
    # The LCS is built backwards, so we need to reverse it
    lcs.reverse()
    
    return lcs_length, ''.join(lcs)

# ExaAple usage:
X = "asbe"
Y = "bes"
lcs_length, lcs = longest_common_subsequence(X, Y)
print(f"Length of LCS: {lcs_length}")
print(f"LCS: {lcs}")

    




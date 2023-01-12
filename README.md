# Longest-Common-subsequence
# Application to the comparison of the DNA of two or more organisms

a-) Problem
  
  The longest common subsequence (LCS) problem is to find the longest subsequence present in two sequences given in the same order, so to find the longest sequence that can be obtained at from the first original sequence by deleting some elements and from the second original sequence by deleting other elements.
For example, consider the following two sequences, X and Y:
X: ABCBDAB
Y: BDCABA

The LCS of X and Y are: BDAB, BCAB, and BCBA

b-) Analysis and Pseudo-code

  As a naive solution we can check if each subsequence of X is a subsequence of Y. Since there are 2^m possible subsequences of X, the time complexity of this solution would be O(n.2^m), where m is the length of the first string and n is the length of the second string.
The LCS problem can be broken down into smaller, simpler "subproblems", which can be further broken down into even simpler subproblems, and so on, until, eventually, the solution becomes trivial.

Consider two sequences, X and Y, of length m and n;

i) Suppose both end with the same element:
       
   To find their LCS, we can shorten each sequence by deleting the last element, and as soon as we find the LCS of the shortened sequences, we add the deleted element.
   In other words, LCS(X[1…m], Y[1…n]) = LCS(X[1…m-1], Y[1…n-1]) + X[m] if X [m] = Y[n]
                      
ii) Now suppose that the two sequences do not end with the same element:

  The LCS of X and Y is the longer of the two sequences LCS(X[1…m-1], Y[1…n]) and LCS(X[1…m], Y[1…n-1]) . To better understand this, consider the following two sequences:
X: ABCBDAB (n items)
Y: BDCABA (m elements)
The LCS of these two sequences either ends with B (the last element of sequence X) or not.

Case 1: If LCS ends in B, then it cannot end in A, and we can remove A from the sequence Y, and the problem reduces to LCS(X[1…m], Y[1…n- 1]).

Case 2: If LCS does not end in B, then we can remove B from the sequence X and the problem reduces to LCS(X[1…m-1], Y[1…n]). For example,
LCS(ABCBDAB, BDCABA) = max(LCS(ABCBDA, BDCABA), LCS(ABCBDAB, BDCAB))

My contact: jospanifozing@yahoo.com

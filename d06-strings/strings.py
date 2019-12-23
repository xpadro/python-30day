def printChars(S):
    '''
    Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed
    and odd-indexed characters as 2 space-separated strings on a single line (see 
    the Sample below for more detail).

    The first line contains an integer, T (the number of test cases).
    Each line i of the T subsequent lines contain a String, S.
    '''

    odd = ""
    even = ""

    for i in range(len(S)):
        if (i % 2 == 0):
            even = even + S[i]
        else:
            odd = odd + S[i]
    
    print(f"{even} {odd}")


T = input()
for i in range(int(T)):
    printChars(input())
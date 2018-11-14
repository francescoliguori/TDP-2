import filecmp
def find_kmp(T, P):
    '''Return the lowest index of T at which substring P begins (or else -1).'''

    n, m = len(T), len(P) # introduce convenient notations
    tmp=T+T[0:m-1]  #add
    n=len(tmp) #add
    print(tmp) #check
    if m == 0:
        return 0 # trivial search for empty string
    fail = compute_kmp_fail(P) # rely on utility to precompute
    j = 0 # index into text
    k = 0 # index into pattern
    while j<n  :

        if tmp[j] == P[k]: # P[0:1+k] matched thus far  modified
            if k == m - 1: # match is complete
                return True
            j += 1 # try to extend match
            k += 1
        elif k > 0:
            k = fail[k-1] # reuse suffix of P[0:k]
        else:
            j += 1
    return False # reached end without match




def compute_kmp_fail(P):
    '''Utility that computes and returns KMP fail list.'''
    m = len(P)
    fail = [0]*m # by default, presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m: # compute f(j) during this pass, if nonzero
        if P[j] == P[k]: # k + 1 characters match thus far
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0: # k follows a matching prefix
            k = fail[k-1]
        else: # no match found starting at j
            j += 1
    return fail

if __name__=="__main__":
    print("test testi")
    print(find_kmp("ciaomondo","oci"))

    print("prova testi")
    f1=open("prova1.txt","r")
    f2=open("prova2.txt","r")
    print(f1.read())
    print(f2.read())
    print(f1.read()==f2.read())
    print(filecmp.cmp("prova1.txt","prova2.txt"))

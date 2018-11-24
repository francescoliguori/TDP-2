from TdP_collections.text.find_kmp import *


def circular_substring(p, t):
    if len(t) ==0:
        raise ValueError("Stringa vuota.")
    result = find_kmp(t+t[:len(p)-1], p)
    if result == -1:
        return False
    else:
        return True

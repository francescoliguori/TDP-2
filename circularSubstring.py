from TdP_collections.text.find_kmp import *


def circular_substring(p, t):
    result = find_kmp(t+t[:len(p)-1], p)
    # print(t+t[:len(p)])

    if result == -1:
        return False
    else:
        return True


if __name__ == "__main__":
    print("circular", circular_substring("ciaomondo", "ocia"))

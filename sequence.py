from collections import defaultdict
from random import choice, shuffle
import re

# def overlap(a, b):
#     """ get the maximum overlap of a & b plus where the overlap starts """

#     overlaps = []

#     for i in range(len(b)):
#         for j in range(len(a)):
#             if a.endswith(b[:i + 1], j):
#                 overlaps.append((i, j))

#     return max(overlaps) if overlaps else (0, -1)


def overlap(a, b):
    # return max(i for i in range(len(b)+1) if a.endswith(b[:i]))
    matches = []
    for i in range(1, len(b) + 1):
        regex = b[:i]
        m = re.search(fr'{regex}$', a)
        if m: matches.append((i - 1, m.start()))
    return max(matches) if matches else (0, -1)

def readData(): # stores reads from file into readSquences List
    sequences = []
    with open('rand.500.1.fq', 'r') as f: 
        for line in f:
            line = line.strip()
            f_letter = line[0:1]
            if(f_letter == 'A' or f_letter == 'G' or f_letter == 'T' or f_letter =='C'):
                sequences.append(line)
    # print(sequences)
    return sequences
    
def main(lst):

    # lst = ['SGALWDV', 'GALWDVP', 'ALWDVPS', 'LWDVPSP', 'WDVPSPV', 'NONSEQUITUR']


    shuffle(lst)  # to verify order doesn't matter

    overlaps = defaultdict(list)

    while len(lst) > 1:
        overlaps.clear()

        for a in lst:
            for b in lst:
                if a == b:
                    continue

                amount, start = overlap(a, b)
                overlaps[amount].append((start, a, b))

        maximum = max(overlaps)

        if maximum == 0:
            break

        start, a, b = choice(overlaps[maximum])  # pick one among equals

        lst.remove(a)
        lst.remove(b)
        lst.append(a[:start] + b)

    print(*lst)

if __name__ == "__main__":
    sequences = readData()
    main(sequences)

    # a = 'SGALWDV'
    # b = 'GALWDVP'
    # print(overlap(a, b))
    # print(overlap2(a, b))

# lolsort, et@iki.fi and java@iki.fi
# inspired by https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.116.9158&rep=rep1&type=pdf

import itertools

def orderliness(sequence):
    """calculate the orderliness of the sequence

    orderliness is a count of all ordered pairs in the sequence
    """
    orderliness = 0
    for a, b in zip(sequence, sequence[1:]):
        orderliness += 1 if a <= b else 0
    return orderliness
        
def maximum(sequence):
    """ find the element with maximally ordered element from 
    the sequence using recursion """
    def findmax(a, n):  
        if (n == 1):
            return a[0]
        return a[n - 1] if orderliness(a[n - 1]) > orderliness(findmax(a, n - 1)) else findmax(a, n - 1)

    return findmax(sequence, len(sequence))

def lolsort(sequence):
    """ Lolsort, an incredibly inefficient sorting algorithm

    Sort the sequence by first multiplying the problem by 
    creating all possible permutations of the sequence
    and then finding the most ordered one.
    """
    permutations = list(itertools.permutations(sequence))
    # return the most orderly permutation
    return maximum(permutations)
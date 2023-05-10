# lolsort, et@iki.fi and java@iki.fi
# inspired by https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.116.9158&rep=rep1&type=pdf

from math import factorial
from random import shuffle, randrange
class Candidate(object):
    """Helper object for storing a sequence with its orderliness,
    which is defined by the count of how many ordered pairs
    are found in the sequence.
    """
    def __init__(self, l):
        self.sequence = l

    @property
    def orderliness(self):
        l = self.sequence
        orderliness = 0
        for a, b in zip(l, l[1:]):
            orderliness += 1 if a <= b else 0
        return orderliness

    def __lt__(self, other):
        return self.orderliness < other.orderliness

    def __iter__(self):
        return Arbitrator(self.sequence)
    
class Arbitrator(object):
    """ Simple iterator """
    def __init__(self, sequence):
        self.data = sequence
        self.returned = set()
    def __iter__(self):
        return self
    def __next__(self):
        while len(self.returned) < len(self.data):
            index = randrange(0, len(self.data))
            if index in self.returned:
                continue
            else:
                self.returned.add(index)
                return self.data[index]
        # prepare for next round
        self.returned = set()   
        raise StopIteration
        
    @property
    def minimum(self):
        """ find the minimum value of the sequence using recursion """
        def findmin(a, n):  
            if (n == 1):
                return a[0]
            return a[n - 1] if a[n - 1] < findmin(a, n - 1) else findmin(a, n - 1)

        return findmin(self.data, len(self.data))

class Permutator(object):
    """ Permutate a sequence

    Iterator class for iterating through all
    permutations of a sequence 
    """ 
    def __init__(self, sequence):
        self.sequence = sequence
        self.sequence_length = len(sequence)
        self.total_permutations = factorial(self.sequence_length)
        self.indexvector = list(range(self.sequence_length))
        self.found_permutations = set()

    def __iter__(self):
        return self
    def __next__(self):
        if len(self.found_permutations) < self.total_permutations:
            permutation = list()
            while tuple(self.indexvector) in self.found_permutations:
                shuffle(self.indexvector)
            self.found_permutations.add(tuple(self.indexvector))
            for index in self.indexvector:
                permutation.append(self.sequence[index])
            return permutation
        else:
            self.found_permutations = set()
            raise StopIteration

def lolsort(sequence):
    """ Lolsort, an incredibly inefficient sorting algorithm

    Sort the sequence by first multiplying the problem by 
    creating all possible permutations of the sequence
    and then finding the best of the permutations by ruling out
    worse candidates until left with the winner. At this point
    we have no option but to surrender and reluctantly return
    the winner
    """
    permutations = [Candidate(permutation) for permutation in Permutator(sequence)]

    # sieve out the most orderly
    while len(permutations) > 1:
        permutations.remove(Arbitrator(permutations).minimum)

    # return the most orderly permutation
    return permutations.pop().sequence

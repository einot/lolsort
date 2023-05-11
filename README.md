# lolsort
Lolsort, an incredibly inefficient sorting algorithm

Authors:
Eino Tuominen <et@iki.fi>
Jani Väisänen <java@iki.fi>

Inspired by https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.116.9158&rep=rep1&type=pdf

A new take on bogosort in which the sorting happens by chance but also it maximizes
the size requirements.

There are two versions. Original lolsort.py which is overly complicated, and then the ordersort.py which
is an optimized and simple implementation of the algorithm.

## lolsort.py

High level pseudo code:

1. (inefficiently) create all permutations of the sequence
2. calculate orderliness of each permutation
3. discard least orderly permutations until only one is left
4. reluctantly return the winner

## ordersort.py

An optimized version of the lolsort, it doesn't utilize chance or do unnecessary elimination. It's time complexity is still O(e^(n!)).

# lolsort
Lolsort, an incredibly inefficient sorting algorithm

Authors:
Eino Tuominen <et@iki.fi>
Jani Väisänen <java@iki.fi>

Inspired by https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.116.9158&rep=rep1&type=pdf

Time complexity is O((N!)^2)

A new take on bogosort in which the sorting happens by chance but also it maximizes
the size requirements.

High level pseudo code:

1. create all permutations of the sequence
2. calculate orderliness of each permutation
3. discard least orderly permutations until only one is left
4. reluctantly return the winner

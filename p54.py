"""
Project Euler Problem 54
========================

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive values.
  * Flush: All cards of the same suit.
  * Full House: Three of a kind and a pair.
  * Four of a Kind: Four cards of the same value.
  * Straight Flush: All cards are consecutive values of same suit.
  * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

        Hand   Player 1            Player 2              Winner
        1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
               Pair of Fives       Pair of Eights
        2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
               Highest card Ace    Highest card Queen
        3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
               Three Aces          Flush with Diamonds
               4D 6S 9H QH QC      3D 6D 7H QD QS
        4      Pair of Queens      Pair of Queens        Player 1
               Highest card Nine   Highest card Seven
               2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        5      Full House          Full House            Player 1
               With Three Fours    with Three Threes

The file poker.txt contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?
"""
# XXX: use enumerate('2..A', start=2) to relace get_values()
# XXX: use Collections.Couter to relace itertools.groupby() for simple usage
from itertools import groupby


def get_values(strs):
    table = {'T': 10,
             'J': 11,
             'Q': 12,
             'K': 13,
             'A': 14}
    for s in strs:
        if '2' <= s <= '9':
            yield int(s)
        else:
            yield table[s]


def get_ranks(group):
    glen = len(group)
    maxval, maxlen = max(group.items(), key=lambda a: (a[1], a[0]))
    if glen == 2:
        rank = 7
        if maxlen == 4:
            rank = 8
    elif glen == 3:
        rank = 3
        if maxlen == 3:
            rank = 4
    elif glen == 4:
        rank = 2
    else:
        rank = 1
    remain = group.keys()
    remain.remove(maxval)
    if rank == 7:
        maxval = [val for val in group if group[val] == 2]
        remain = [val for val in group if group[val] != 2]
    return rank, maxval, remain


def rank(player):
    "Return comparable rank for list `player`, containing five cards"
    rank = None
    flush = len(set(card[1] for card in player)) == 1
    player = (card[0] for card in player)
    values = sorted(get_values(player))
    straight = all(values[i+1]-values[i] == 1 for i in range(len(values)-1))
    if flush:
        rank = 6
        if straight:
            rank = 9
    if straight:
        rank = 5
    if rank:
        return rank, max(values), values.remove(max(values))
    group = {}
    for value, it in groupby(values):
        group[value] = len(list(it))
    return get_ranks(group)


def main():
    n = 0
    for each in open('resources/poker.txt'):
        each = each.split()
        p1, p2 = each[:5], each[5:]
        if rank(p1) > rank(p2):
            n += 1
    return n


if __name__ == '__main__':
    print main()

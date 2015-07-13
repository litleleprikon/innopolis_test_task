#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'litleleprikon'

from player import FIGURES, FIG_LEN, Player


def comparator(figure_1: str, figure_2: str) -> int:
    """
    Function, that make a comparison of teo figures and returns 0 if figures equals to each other,
    1 if first figure beats second
    2 if second figure beats first
    :param figure_1: name of first figure
    :param figure_2: name of third figure
    :return:
    -- Doctests --
    >>> comparator('камень', 'бумага')
    2
    >>> comparator('камень', 'камень')
    0
    >>> comparator('камень', 'ножницы')
    1
    """
    if figure_1 not in FIGURES or figure_2 not in FIGURES:
        raise Exception('Доступные фигуры: {}'.format(', or '.join(FIGURES)))
    if figure_1 == figure_2:
        return 0
    elif figure_2 == FIGURES[(FIGURES.index(figure_1) + 1) % FIG_LEN]:
        return 2
    return 1

class Tournament:
    """
    Tournament class is responsible for tournament.
    This class creates players list and run rounds of tournament
    """
    def __init__(self, rounds_count: int):
        self.__counter = rounds_count
        self.__players = [Player(i) for i in range(2**rounds_count)]
        print('\n'.join(map(str, self.__players)))

    def __make_round(self):
        winners = []
        players_len = len(self.__players)
        i = 0
        winner = None
        while i < players_len:
            while True:
                result = comparator(self.__players[i].figure, self.__players[i+1].figure)
                if result != 0:
                    winner = self.__players[i-1+result]
                    print('{} vs {} - победил {}!'.format(self.__players[i].name, self.__players[i+1].name, winner.name))
                    break
            winners.append(winner)
            i += 2
        if len(winners) == 1:
            return True
        self.__players = winners

    def run(self):
        i = 1
        while True:
            if len(self.__players) == 2:
                print('\nФинал')
            else:
                print('\nРаунд {}'.format(i))

            if self.__make_round():
                break
            i += 1

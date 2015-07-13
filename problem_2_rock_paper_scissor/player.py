#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'litleleprikon'


from random import randint


FIGURES = ['камень', 'бумага', 'ножницы']
FIG_LEN = len(FIGURES)

class Player:
    """
    Player class is needed to store tactics and to generate figures by this tactic

    -- Doctests --
    >>> player = Player()
    >>> player.figure in FIGURES
    True
    """
    def __init__(self, number: int):
        self.name = 'игрок{}'.format(number)
        tactic = randint(0, FIG_LEN-1)
        self.main_figure = FIGURES[tactic]
        self.__figures = [FIGURES[(tactic+i) % FIG_LEN] for i in range(FIG_LEN)]

    def __str__(self):
        return '{}: {}'.format(self.name, self.main_figure)

    @property
    def figure(self):
        rand = randint(0, FIG_LEN)
        return self.__figures[rand % FIG_LEN]

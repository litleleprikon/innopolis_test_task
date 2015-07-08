#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'litleleprikon'

from decimal import Decimal, getcontext
import argparse

# Set Decimal precision to 10
getcontext().prec = 10


def create_parser():
    parser = argparse.ArgumentParser(description='Quadratic equation solver')
    parser.add_argument('-a', required=True, action='store',
                        type=lambda x: Decimal(x) if str(x).replace('.', '').isdigit() else Decimal(1),
                        dest='a', help='First coefficient of equation, cant be a zero')
    parser.add_argument('-b', action='store',
                        type=lambda x: Decimal(x) if str(x).replace('.', '').isdigit() else Decimal(0),
                        dest='b', help='Second coefficient of equation', default=Decimal(0))
    parser.add_argument('-c', action='store',
                        type=lambda x: Decimal(x) if str(x).replace('.', '').isdigit() else Decimal(0),
                        dest='c', help='Third coefficient of equation', default=Decimal(0))
    return parser.parse_args()


def discriminant(a: Decimal, b: Decimal, c: Decimal) -> Decimal:
    """
    Function, that returns descriminant of quadratic equation
    :param a: First coefficient of equation, cant be a zero
    :param b: First coefficient of equation
    :param c: First coefficient of equation
    :return: Discriminant

    -- Doctests --
    >>> discriminant(1, 0, 0)
    0
    >>> discriminant(1, 2, 0)
    4
    >>> discriminant(1, 2, 3)
    -8
    """
    d = b**2 - 4*a*c
    return d


def solver(a: Decimal, b: Decimal, c: Decimal) -> tuple:
    """
    Function, that returns
    :param a: First coefficient of equation, cant be a zero
    :param b: First coefficient of equation
    :param c: First coefficient of equation
    :return: Root of the equation

    -- Doctests --
    >>> solver(Decimal(1), Decimal(2), Decimal(3))

    >>> '{:.2f}, {:.2f}'.format(*solver(Decimal(1), Decimal(0), Decimal(0)))
    '0.00, 0.00'
    >>> '{:.2f}, {:.2f}'.format(*solver(Decimal(1), Decimal(2), Decimal(0)))
    '0.00, -2.00'
    """
    d = discriminant(a, b, c)
    if d > 0:
        x1 = (-b + d**Decimal(0.5))/2*a
        x2 = (-b - d**Decimal(0.5))/2*a
        return x1, x2
    if d == 0:
        x = -(b/2*a)
        return x, x


def main():
    args = create_parser()
    solution = solver(args.a, args.b, args.c)
    if solution is None:
        print('No real roots')
    else:
        print('Root 1 is {}, root 2 is '.format(*solution))


if __name__ == "__main__":
    main()

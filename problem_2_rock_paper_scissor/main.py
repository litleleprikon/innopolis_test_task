#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'litleleprikon'

from tournament import Tournament
import argparse


def create_parser():
    def check_value(value: str) -> int:
        if not value.isdigit():
            print('Количество раундов должно задаваться целым положительным числом, значение узтановлено по умолчанию')
            return 1
        return int(value)

    parser = argparse.ArgumentParser(description='Программа проведения турнира "Камень, ножницы, бумага"')
    parser.add_argument('num', action='store', type=lambda x: check_value(x),
                        help='Количество раундов, не может быть 0, значение по умолчанию: 1')
    return parser.parse_args()


def main():
    args = create_parser()
    Tournament(args.num).run()


if __name__ == '__main__':
    main()

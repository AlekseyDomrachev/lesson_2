#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
Moscow_point = sites['Moscow']
London_point = sites['London']
Paris_point = sites['Paris']


def distance_calculate(point_1, point_2):
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5


distance = {'Moscow_London': (distance_calculate(Moscow_point, London_point)),
            'Moscow_Paris': (distance_calculate(Moscow_point, Paris_point)),
            'Paris_London': (distance_calculate(Paris_point, London_point))}

pprint(distance)

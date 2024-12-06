from typing import List
import math
from linear_algebra import sum_of_squares
from collections import Counter
import matplotlib.pyplot as plt

num_friends = [
    100.0,
    49,
    41,
    40,
    25,
    21,
    21,
    19,
    19,
    18,
    18,
    16,
    15,
    15,
    15,
    15,
    14,
    14,
    13,
    13,
    13,
    13,
    12,
    12,
    11,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]

contagem_amigos = Counter(num_friends)
valor_maximo = max(num_friends)
xs = range(int(valor_maximo + 1))
ys = [contagem_amigos[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("histograma da contagem de amigos")
plt.xlabel("# de amigos")
plt.ylabel("# de pessoas")
# plt.show()

numero_pontos = len(num_friends)
valor_minimo = min(num_friends)

valores_ordenados = sorted(num_friends)
valor_minimo = valores_ordenados[0]
segundo_valor_minimo = valores_ordenados[1]
segundo_valor_maximo = valores_ordenados[-2]


def media(xs: List[float]) -> float:
    return sum(xs) / len(xs)


media(num_friends)


def _mediana_par(xs: List[float]) -> float:
    return sorted(xs)[len(xs) // 2]


def _mediana_impar(xs: List[float]) -> float:
    ordenado_xs = sorted(xs)
    hi_pontomediano = len(xs) // 2
    return (ordenado_xs[hi_pontomediano - 1] + ordenado_xs[hi_pontomediano]) / 2


def mediana(v: List[float]) -> float:
    return _mediana_impar(v) if len(v) % 2 == 0 else _mediana_par((v))


assert mediana([1, 10, 2, 9, 5]) == 5
assert mediana([1, 9, 2, 10]) == (2 + 9) / 2

assert mediana(num_friends) == 6


def quantile(xs: List[float], p: float) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


def moda(x: List[float]) -> float:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


assert set(moda(num_friends)) == {1, 6}


def de_media(xs: List[float]) -> List[float]:
    x_bar = media(xs)
    return [x - x_bar for x in xs]


def variancia(xs: List[float]) -> float:
    assert len(xs) >= 2

    n = len(xs)
    deviations = de_media(xs)
    return sum_of_squares(deviations) / (n - 1)


assert 81.54 < variancia(num_friends) < 81.55


def desvio_padrao(xs: List[float]) -> float:
    return math.sqrt(variancia(xs))


assert 9.02 < desvio_padrao(num_friends) < 9.04


def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)

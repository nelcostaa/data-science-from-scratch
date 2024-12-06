from typing import Callable
import math
from typing import List

Vector = List[float]

height_weight_age = [
    70,  # inches,
    170,  # pounds,
    40,
]  # years

grades = [
    95,  # exam1
    80,  # exam2
    75,  # exam3
    62,
]  # exam4


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)

    return [v_i + w_i for v_i, w_i in zip(v, w)]


print(add([1, 2, 3], [4, 5, 6]) == [5, 7, 9])


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided!"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))


def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v, w))


Matrix = List[List[float]]

A = [
    [1, 2, 3],  # A has 2 rows and 3 columns
    [4, 5, 6],
]

B = [
    [1, 2],  # B has 3 rows and 2 columns
    [3, 4],
    [5, 6],
]

from typing import Tuple


def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns


def get_row(A: Matrix, i: int) -> Vector:
    return A[i]


def get_columns(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]


def make_matrix(
    num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]
) -> Matrix:
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

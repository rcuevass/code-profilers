import numpy as np
from viztracer import VizTracer

tracer = VizTracer()

tracer.start()


def generate_matrices(matrix_dim: int = 10000) -> tuple:
    a = np.random.random((matrix_dim, matrix_dim))
    b = np.random.random((matrix_dim, matrix_dim))
    return a, b


def product_loop(a: np.array, b: np.array) -> np.array:
    c = np.empty(a.shape)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i, j] = a[i, j] * b[i, j]
    return c


def product_numpy(a: np.array, b: np.array) -> np.array:
    return a * b


tracer.stop()
tracer.save()
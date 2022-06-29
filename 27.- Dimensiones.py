# Dimensiones

import numpy as np

def main():
    # Escalar
    escalar = np.array(42)
    print(escalar)
    print(escalar.ndim)

    # Vector
    vector = np.array([1, 2, 3])
    print(vector)
    print(vector.ndim)

    # Matriz
    matriz = np.array([[1, 2, 3], [4, 5, 6]])
    print(matriz)
    print(matriz.ndim)

    # Tensor
    tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(tensor)
    print(tensor.ndim)

if __name__ == '__main__':
    main()
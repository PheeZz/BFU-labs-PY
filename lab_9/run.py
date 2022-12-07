import numpy as np
from pprint import pformat
from copy import deepcopy
from scipy import stats
from timeit import timeit


def save_matrix(string: str):
    """save matrix to file"""
    if not string.strip():
        string = "3,4,17,-3\n5,11,-1, 6\n0,2,-5,8"

    with open("lab_9/matrix.txt", "w") as file:
        file.write(string)


def read_matrix(matrix_path: str = "lab_9/matrix.txt") -> np.ndarray:
    """read matrix from file"""
    with open(matrix_path, "r") as file:
        matrix = file.read()
        matrix = np.array([list(map(int, row.split(",")))
                           for row in matrix.splitlines()])
    return matrix


def sum_max_min() -> tuple[int, int, int]:
    """TASK 1\n
    read matrix from file and sum all elements, find max and min"""
    matrix = read_matrix()
    return matrix.sum(), matrix.max(), matrix.min()


def run_lenght_encoding(vector: np.ndarray = read_matrix()) -> tuple[np.ndarray, np.ndarray]:
    """TASK 2\n
    run lenght encoding
    return tuple of two vectors: unique elements and their counts"""
    unique, counts = np.unique(vector, return_counts=True)
    return unique, counts


def generate_matrix(rows: int = 10, columns: int = 4) -> np.ndarray:
    """generate matrix with random elements with normal distribution"""
    return np.random.normal(size=(rows, columns))


def min_max_avg_std_deviation(matrix: np.ndarray = generate_matrix()) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """TASK 3\n
    return tuple of four vectors: matrix,\n
    min, max, average, standart deviation for all matrix"""
    return matrix, matrix.min(axis=0).min(), matrix.max(axis=0).max(), matrix.mean(axis=0).mean(), matrix.std(axis=0).std()


def max_after_zero(vector: np.ndarray = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])) -> int:
    """TASK 4\n
    return max element value in vector after zero"""
    if 0 in vector:
        after_zeros = vector[1:][vector[:-1] == 0]
        return after_zeros.max()
    return None


def density_log_of_multivariate_normal_distribution(dots_X: np.ndarray = np.array([1, 0]), size: tuple = None,
                                                    EX: np.ndarray = np.array([0, 0]), lenght_vector: int = 1,
                                                    cov_matrix: np.ndarray = np.array([[1, 0], [0, 1]])):
    """TASK 5\n
    return density log of multivariate normal distribution"""
    return np.log(np.linalg.det(cov_matrix)) - lenght_vector * np.log(2 * np.pi) \
        - 0.5 * (dots_X - EX).T @ np.linalg.inv(cov_matrix) @ (dots_X - EX)


def switch_rows(matrix: np.ndarray = np.arange(16).reshape(4, 4), index_row_first: int = 0, index_row_second: int = 2) -> np.ndarray:
    """TASK 6 \n
    switch two rows in matrix"""
    old_matrix = deepcopy(matrix)
    matrix[index_row_first], matrix[index_row_second] = old_matrix[index_row_second], old_matrix[index_row_first]
    return old_matrix, matrix


def find_unique(url):
    """TASK 7\n
    find unique elements and their count in 'species' column in file from iris url"""
    iris = np.genfromtxt(url, delimiter=",", dtype='object')
    species = np.array([row[4] for row in iris])
    unique, counts = np.unique(species, return_counts=True)
    return unique, counts


def not_null_indexes(vector: np.ndarray = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])) -> np.ndarray:
    """TASK 8\n
    return indexes of not null elements"""
    return np.where(vector != 0)[0]


if __name__ == "__main__":
    task_1_answers = sum_max_min()
    print(f'TASK 1:\n\tSumm of all elements: {task_1_answers[0]}\n\
        Maximum value in matrix: {task_1_answers[1]}\n\
        Minimum value in matrix: {task_1_answers[2]}', end="\n\n\n")

    task_2_answers = run_lenght_encoding(np.array([2, 2, 2, 3, 3, 3, 5]))
    print(f'TASK 2:\n\tUnique elements: {task_2_answers[0]}\n\
        Counts of unique elements: {task_2_answers[1]}', end="\n\n\n")

    task_3_answers = min_max_avg_std_deviation()
    first_five_rows = f'{task_3_answers[0][:5]}'
    print(f'TASK 3:\n\tMatrix: {task_3_answers[0]}\n\n\
        Minimum value in matrix: {task_3_answers[1]}\n\n\
        Maximum value in matrix: {task_3_answers[2]}\n\n\
        Average value in matrix: {task_3_answers[3]}\n\n\
        Standart deviation in matrix: {task_3_answers[4]}', end="\n\n\n")

    random_vector = np.random.randint(0, 10, 10)
    print(f'TASK 4:\n\tRandom vector: {random_vector}\n\
        Maximum value after zero: {max_after_zero(random_vector)}', end="\n\n\n")

    dots_X, size, EX, lenght_vector, cov_matrix = np.array(
        [1, 0]), (2, 2), np.array([0, 0]), 2, np.array([[1, 0], [0, 1]])

    print(f'TASK 5:\n\tDots X: {dots_X}\n\
        Size: {size}\n\
        EX: {EX}\n\
        Lenght vector: {lenght_vector}\n\
        Covariance matrix: {cov_matrix}\n\
        Density log of multivariate normal distribution\n\
        numpy variation:\n\
        {density_log_of_multivariate_normal_distribution(dots_X, size, EX, lenght_vector, cov_matrix)}\n\
        Time of numpy variation: {timeit("density_log_of_multivariate_normal_distribution(dots_X, size, EX, lenght_vector, cov_matrix)", setup="from __main__ import density_log_of_multivariate_normal_distribution, dots_X, size, EX, lenght_vector, cov_matrix"):.4f}\n\n\
        scipy variation:\n\
        {stats.multivariate_normal.logpdf(dots_X, mean=EX, cov=cov_matrix)}\n\
        Time of scipy variation: {timeit("stats.multivariate_normal.logpdf(dots_X, mean=EX, cov=cov_matrix)", setup="from scipy import stats; from __main__ import dots_X, EX, cov_matrix")}', end="\n\n\n")

    task_6_answers = switch_rows()
    print(f'TASK 6:\n\tOld matrix:\n{task_6_answers[0]}\n\
        New matrix:\n{task_6_answers[1]}', end="\n\n\n")

    task_7_answers = find_unique(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
    print(f'TASK 7:\n\tUnique elements: {task_7_answers[0]}\n\
        Counts of unique elements: {task_7_answers[1]}', end="\n\n\n")

    array_with_nulls = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
    print(
        f'TASK 8:\n\tIndexes of not null elements:\n\t{not_null_indexes(array_with_nulls)}\
        \n\n\tin array:\n\
        {array_with_nulls}', end="\n\n\n")

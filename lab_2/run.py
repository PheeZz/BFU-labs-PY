from pprint import pprint


class Triangle():
    def __init__(self, pascal_value: int = 10, serpinsky_value: int = 3) -> None:
        self._pascal_value = pascal_value
        self._serpinsky_value = serpinsky_value

    def pascal(self):
        # Pascal triangle
        triangle = [[1], [1, 1]]
        for row in range(2, self._pascal_value):
            triangle.append([1])
            for value in range(1, row):
                triangle[row].append(
                    triangle[row - 1][value - 1] + triangle[row - 1][value])
            triangle[row].append(1)

        triangle = [list(map(str, row)) for row in triangle]
        triangle = [list(map(lambda x: x.rjust(len(triangle[-1][-1])), row))
                    for row in triangle]
        triangle = [' '.join(i) for i in triangle]

        print('\n\nPascal triangle:')
        for value in triangle:
            print(value.center(len(triangle[-1]), ' '))

    def serpinsky(self):
        # Sierpinski triangle
        # create matrix 20x20
        triangle = [[' ' for _ in range(20)] for _ in range(20)]
        # set start points
        triangle[0][9], triangle[-1][0], triangle[-1][-1] = '*', '*', '*'
        print()
        # TODO: make it work


if __name__ == '__main__':
    # _ = Triangle(int(input('Enter number for Pascal triangle: ')))
    _ = Triangle()
    _.pascal()
    _.serpinsky()



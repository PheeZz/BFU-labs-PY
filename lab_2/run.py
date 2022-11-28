import functools

class Triangle():
    def __init__(self, pascal_value: int = 10, sierpinski_value: int = 3) -> None:
        self._pascal_value = pascal_value
        self._sierpinski_value = sierpinski_value

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

    def sierpinski(self):
        """Sierpinski triangle"""
        def aggregate(TRIANGLE, I):
            SPACE = " " * (2 ** I)
            return ([SPACE+X+SPACE for X in TRIANGLE] + [f"{X} {X}" for X in TRIANGLE])
        print('\n\nSierpinski triangle:')
        print('\n'.join(functools.reduce(
            aggregate, range(self._sierpinski_value), ["*"])))


if __name__ == '__main__':
    # _ = Triangle(int(input('Enter number for Pascal triangle: ')))
    _ = Triangle()
    _.pascal()
    _.sierpinski()

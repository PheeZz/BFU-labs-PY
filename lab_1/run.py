class PrettyPrinter():
    def __init__(self, number: int):
        self._number = number

    # 2.1
    def int_output(self):
        print('#2.1:')
        for maximum in range(1, self._number+1):
            print(*range(1, maximum+1), sep='')
        print('\n')

    def str_output(self):
        for maximum in range(1, self._number+1):
            print(*[str(i) for i in range(1, maximum+1)], sep='')
        print('\n\n')

        # 2.2
    def triangle(self):
        print('#2.2:')
        triangle_list = list()
        for maximum in range(1, self._number+1):
            output_str = str()
            output_str += ''.join([str(i) for i in range(1, maximum+1)])
            output_str += ''.join([str(i) for i in range(maximum-1, 0, -1)])
            triangle_list.append(output_str)

        for item in triangle_list:
            item = item.center(len(triangle_list[-1]), ' ')
            print(item)

    def triangle_round(self):
        print('\n\n#2.3:')
        triangle_list = list()
        whitespaces = len(str(self._number))
        for maximum in range(1, self._number+1):
            output_str = str()
            temp_list = [str(i) for i in range(1, maximum+1)]
            temp_list_reversed = [str(i) for i in range(maximum-1, 0, -1)]

            temp_list = [i.rjust(whitespaces, ' ') for i in temp_list]
            temp_list_reversed = [i.rjust(whitespaces, ' ')
                                  for i in temp_list_reversed]

            output_str += ''.join(temp_list+temp_list_reversed)
            triangle_list.append(output_str)

        for item in triangle_list:
            item = item.center(len(triangle_list[-1]), ' ')
            print(item)


def union(*args) -> int:
    return 3 - len(set().union(*args))


if __name__ == '__main__':
    print(f'#1: {union((1, 2, 3))}\n\n')

    _ = PrettyPrinter(int(input('Enter number for triangle and pyramid: ')))
    _.int_output()
    _.str_output()
    _.triangle()
    _.triangle_round()
    print('\nby Daniil Y. 2022')

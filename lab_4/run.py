class listPlus():
    def __init__(self, input_list: list = [3, 4, 7, 1, 2, 5, 6, 9, 8],
                 second_list: list = [1, 2, 3, 4, 5]) -> None:
        self._input_list = input_list
        self._second_list = second_list

    def current_more_previous(self) -> list:
        return [self._input_list[index] for index in range(1, len(self._input_list)) if self._input_list[index] > self._input_list[index - 1]]

    def swith_min_max(self) -> list:
        min_index = self._input_list.index(min(self._input_list))
        max_index = self._input_list.index(max(self._input_list))
        self._input_list[min_index], self._input_list[max_index] = self._input_list[max_index], self._input_list[min_index]
        return self._input_list, f'Min index: {min_index} with value: {min(self._input_list)}', f'Max index: {max_index} with value: {max(self._input_list)}'

    def crossing(self):
        return len([self._input_list[index] for index in range(len(self._input_list)) if self._input_list[index] in self._second_list])

    def repetitions(self):
        repeats = dict([(self._input_list[index], self._input_list.count(
            self._input_list[index])) for index in range(len(self._input_list))])
        ouput_list = [str(value) for value in repeats.values() if value]
        return ' '.join(ouput_list)


if __name__ == '__main__':
    _ = listPlus()
    # 0
    print(_.current_more_previous(), end='\n\n')
    # 1
    print(*_.swith_min_max(), sep='\n', end='\n\n')
    # 2
    print(
        f'crossing numbers count in lists:\n{_._input_list}\n{_._second_list}\n{_.crossing()}', end='\n\n')
    # 3
    for rotation in (['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc'],
                     ['aaa', 'bbb', 'ccc'],
                     ['abc', 'abc', 'abc']):
        _._input_list = rotation
        print(
            f'Repetitions for input list:\n{_._input_list}\n{_.repetitions()}', end='\n\n')

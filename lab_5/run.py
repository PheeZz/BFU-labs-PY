class ListsAndSets():
    def __init__(self, input_list: list = [1, 2, 3, 2, 1],
                 second_list: list = [1, 2, 3, 4, 5, 6, 7],
                 input_set: set = {1, 2, 3},
                 second_set: set = {1, 4, 5}) -> None:
        self._input_list = input_list
        self._second_list = second_list
        self._input_set = input_set
        self._second_set = second_set

    def unique_count(self) -> int:
        return len(set(self._input_list))

    def is_subset(self) -> bool:
        return self._input_set.issubset(self._second_set)

    def cities_game(self, already_used: int) -> list:
        cities = [input(f'City #{index + 1}: ').lower()
                  for index in range(already_used)]
        return '\nREPEAT' if input('Enter a new city: ').lower() in cities else '\nOK'


if __name__ == '__main__':
    _ = ListsAndSets()
    print(
        f'Task #1: Unique count in list: {_._input_list}\n{_.unique_count()}', end='\n\n')
    print(
        f'Task #2: Is set: {_._input_set} subset of set: {_._second_set}\n{_.is_subset()}', end='\n\n')
    print(f'Task #3: Cities game {_.cities_game(3)}', end='\n\n')

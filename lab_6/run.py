import functools


class txt_work():
    def __init__(self, file_name):
        self.file_name = file_name

    def product_to_txt(self):
        # task 1
        with open(self.file_name, 'r') as f:
            numbers = f.read()
        with open('lab_6\\output.txt', 'w') as f:
            f.write(str(functools.reduce(
                lambda x, y: x * y, map(int, numbers.split()))))

    def sort_file(self):
        # task 2
        with open(self.file_name, 'r') as f:
            numbers = f.read()
        with open('lab_6\\output_2.txt', 'w') as f:
            f.write(' '.join(list(map(str, sorted(map(int, numbers.split()))))))

    def kids_task(self):
        # task 3
        with open('lab_6\\kids\\kids.txt', 'r', encoding='UTF-8') as f:
            kids = f.read()
            # filter integers
            kids_old = list(filter(lambda x: x.isdigit(), kids.split()))
            _max_index = max(list(map(int, kids_old)))
            _min_index = min(list(map(int, kids_old)))

        with open('lab_6\\kids\\max_age.txt', 'w', encoding='UTF-8') as f:
            # write max age and name
            f.write(
                f'{kids.splitlines()[kids_old.index(str(_max_index))]}')

        with open('lab_6\\kids\\min_age.txt', 'w', encoding='UTF-8') as f:
            # write min age and name
            f.write(
                f'{kids.splitlines()[kids_old.index(str(_min_index))]}')


if __name__ == '__main__':
    test_txt = txt_work('lab_6\\input.txt')
    test_txt.product_to_txt()
    test_txt.sort_file()
    test_txt.kids_task()

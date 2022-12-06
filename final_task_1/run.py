import csv
import tabulate
from random import shuffle
from copy import deepcopy
from os import mkdir, listdir, getcwd


class csv_work():
    def __init__(self, file_name):
        self.file_name = file_name

    def Show(self, view_start_from: str = 'top', view_count: int = 5):
        with open(self.file_name, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            if len(data) < view_count:
                view_count = len(data)
                print('-'*20, 'В файле меньше строк, чем вы хотите вывести', '-'*20)

            # get headers names from first row
            headers = data[0]
            del data[0]

            if view_start_from == 'top':
                print(tabulate.tabulate(
                    data[:view_count],
                    headers=headers,
                    tablefmt='simple_grid'))

            elif view_start_from == 'bottom':
                print(tabulate.tabulate(reversed(data)[:view_count],
                      headers=headers,
                      tablefmt='simple_grid'))

            elif view_start_from == 'random':
                # create copy of data to don't change original data list
                shuffled_list = deepcopy(data)
                # shuffle it
                shuffle(shuffled_list)
                print(tabulate.tabulate(shuffled_list[:view_count],
                      headers=headers,
                      tablefmt='simple_grid'))

    def Info(self):
        """return file info such as unenmpty rows and columns as dict"""
        with open(self.file_name, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            # get number of columns
            columns = len(data[0])
            # get number of rows
            rows = len(data)
            # get number of empty rows
            empty_rows = data.count([''] * columns)
            # get number of empty columns
            empty_columns = sum(column == (
                '',) * rows for column in zip(*data))
            return {'columns': columns,
                    'rows': rows,
                    'empty_rows': empty_rows,
                    'empty_columns': empty_columns}

    def DelNaN(self):
        # delete all strings with at least one empty cell
        deletions_count = 0
        with open(self.file_name, 'r') as f:  # load file
            reader = csv.reader(f)
            data = list(reader)  # put file data to list variable
            for row in data:  # start checking each row for empty cells
                if '' in row:  # if found empty cell
                    data.remove(row)  # delete row from data variable
                    deletions_count += 1  # update deletions counter
        print('-'*20, 'Удалено строк:', deletions_count, '-'*20)

        with open(self.file_name, 'w', newline='') as f:  # open file for writing
            writer = csv.writer(f)
            # rewrite file with new data
            writer.writerows(data)

    def MakeDS(self):
        # shuffle data
        with open(self.file_name, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            shuffle(data)
        # slice data to 70% for training and 30% for testing
        train_data = data[:int(len(data) * 0.7)]
        test_data = data[int(len(data) * 0.7):]

        # create directory for train and test data
        if 'Learning' not in listdir(f'{getcwd()}\\lab_6') or 'Testing' not in listdir(f'{getcwd()}\\lab_6'):
            mkdir(f'{getcwd()}\\lab_6\\Learning')
            mkdir(f'{getcwd()}\\lab_6\\Testing')
        # make training dataset
        with open('lab_6/Learning/LearningSet.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(train_data)
        # make testing dataset
        with open('lab_6/Testing/TestingSet.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(test_data)


if __name__ == '__main__':
    test_csv = csv_work('final_task_1/myFile0.csv')
    test_csv.Show()
    print(test_csv.Info())
    test_csv.DelNaN()
    test_csv.MakeDS()

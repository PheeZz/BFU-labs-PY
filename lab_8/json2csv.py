import csv
import json
import sys


def json2csv(json_file: str):
    with open(json_file, 'r') as f:
        data = json.load(f)
    # get key from list inside dict
    table = tuple(data.keys())[0]
    # get keys from dict
    keys = data[table][0].keys()
    # create csv file with same name as json file
    with open(f'{json_file[:-5]}.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(data[table])


if __name__ == '__main__':
    json2csv(sys.argv[1])

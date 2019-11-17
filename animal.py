from __future__ import print_function
import csv
import json
import pandas as pd

try:
    import argparse

    parser = argparse.ArgumentParser(description='Inputs client details', add_help=True, epilog='Example of use')
    parser.add_argument('--name', type=str, help='client name', action='store', default=False, dest="name")
    parser.add_argument('--address', type=str, help='client address', action='store', default=False, dest="address")
    parser.add_argument('--phone', type=str, help='phone', action='store', default=False, dest="phone")
    flags = parser.parse_args()

except ImportError:
    flags = None


class UnsupportedFileFormat(Exception):
    pass


class SaveCSV:

    def save_data(self, data):
        csv_file = "client.csv"
        csv_columns = ['name', 'address', 'phone']
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                writer.writerow(data)
        except IOError:
            print("I/O error")
        return csv_file


class SaveJSON:

    def save_data(self, data):
        json_file = "client.json"
        try:
            with open(json_file, 'w') as jsonfile:
                json.dump(data, jsonfile)
        except IOError:
            print("I/O error")
        return json_file


SAVE_FORMATS = {
    'csv': SaveCSV(),
    'json': SaveJSON(),
}


def save_data(key, value):
    if key in ['csv', 'json']:
        SAVE_FORMATS[key].save_data(value)
        SAVE_FORMATS[key].save_data(value)
    else:
        raise UnsupportedFileFormat('{0} format not yet supported.'.format(key))


def supported_formats():
    return list(SAVE_FORMATS.keys())


def read_json_with_panda(url):
    df = pd.read_json(url, orient='columns')
    return df.head(10)


if __name__ == '__main__':
    print('Format(s) supported: ', supported_formats())
    save_data('csv', flags.__dict__)
    save_data('json', flags.__dict__)
    print(read_json_with_panda(url='https://api.github.com/users/mumehta/repos'))


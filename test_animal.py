# test_animal.py

import pytest
import os
from animal import save_data, SaveCSV, SaveJSON, UnsupportedFileFormat


@pytest.fixture
def test_data():
    data = {
        'name': 'test_name',
        'address': 'test_address',
        'phone': '000',
    }
    return data


def test_save_csv_data(test_data):
    file_extension = os.path.splitext(SaveCSV().save_data(data=test_data))[1][1:]
    assert file_extension == 'csv'


def test_save_json_data(test_data):
    file_extension = os.path.splitext(SaveJSON().save_data(data=test_data))[1][1:]
    assert file_extension == 'json'


def test_save_unknown_data_format(test_data):
    with pytest.raises(UnsupportedFileFormat):
        file_extension = os.path.splitext('unknown.extn')[1][1:]
        save_data(file_extension, test_data)

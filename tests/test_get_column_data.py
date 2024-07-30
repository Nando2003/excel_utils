import pytest

from openpyxl import Workbook
from openpyxl.utils.exceptions import InvalidFileException

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.column_utils.get_column_data import get_column_data_from_excel

@pytest.fixture
def sample_excel_file(tmp_path):
    workbook = Workbook()
    worksheet = workbook.active

    data = [
        ['Header'],
        ['Row 1'],
        ['Row 2'],
        ['Row 3'],
        [ None ],
        ['Row 5']
    ]

    for row in data:
        worksheet.append(row)

    file_path = tmp_path / 'sample.xlsx'
    workbook.save(file_path)
    return file_path

def test_get_column_data_from_excel_valid(sample_excel_file):
    result = get_column_data_from_excel(
        str(sample_excel_file),
        row=1,
        column='A',
        index=False
    )

    expected = ['Header', 'Row 1', 'Row 2', 'Row 3', 'Row 5']
    assert result == expected

def test_get_column_data_from_excel_with_index(sample_excel_file):
    result = get_column_data_from_excel(
        str(sample_excel_file),
        row=1,
        column='A',
        index=True
    )

    expected = [(1, 'Header'), (2, 'Row 1'), (3, 'Row 2'), (4, 'Row 3'), (6, 'Row 5')]
    assert result == expected

def test_get_column_data_from_excel_invalid_file(tmp_path):
    invalid_file = tmp_path / 'invalid_file.txt'
    invalid_file.write_text('This is not an Excel file.')

    with pytest.raises(InvalidFileException):
        get_column_data_from_excel(str(invalid_file))
    
def test_get_column_data_from_excel_invalid_column(sample_excel_file):
    with pytest.raises(ValueError):
        get_column_data_from_excel(
            str(sample_excel_file),
            row=1,
            column='ABZZ'
        )
    
def test_get_column_data_from_excel_invalid_row(sample_excel_file):
    with pytest.raises(ValueError):
        get_column_data_from_excel(
            str(sample_excel_file),
            row=100000000,
            column='A'
        )
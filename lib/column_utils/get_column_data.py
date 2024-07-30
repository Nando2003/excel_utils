from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException

def get_column_data_from_excel(xlsx_path:str, row:int =1, column:str ='A', index:bool =False) -> list:
    """
    Extracts data from a specific column in an Excel file and stores it in a list.

    :param xlsx_path: Path to the Excel file.
    :param row: Starting row for extraction (1-indexed).
    :param column: Column to extract data from.
    :param index: If True, returns a list of tuples with (index, data). If False, returns a list of data only.
    :return: A list containing the data from the specified column. 
             If index=True -> [(index, data), (index, data), ...] 
             If index=False -> [data, data, ...]
    :raises ValueError: If the specified row or column does not exist.
    :raises InvalidFileException: If the provided path does not lead to a valid .xlsx file.
    """
    try:
        load_wb = load_workbook(xlsx_path)
        sheet = load_wb.active
        
        column = column.upper()
        row = row - 1
        
        cell_ID = [cell for cell in sheet[column][row:]]
        
        if index is True:
            indexed_cell_value = [(cell.row, cell.value) for cell in cell_ID if cell.value is not None]
            return indexed_cell_value # [(index, value)...]
        
        cell_value = [cell.value for cell in cell_ID if cell.value is not None]
        return cell_value # [value...]
    
    except ValueError:
        raise ValueError("The specified row or column does not exist.")

    except InvalidFileException:
        raise InvalidFileException("The path does not lead to a valid .xlsx file.")

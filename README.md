# Excel Utils

`excel_utils` is a Python package designed to extract data from a specific column in an Excel file and store it in a list. 

## Installation

To install the package, clone the repository and install it using `pip`:

```bash
pip install git+https://github.com/nando2003/excel_utils.git
```

## Usage

```python
from excel_utils import get_column_data_from_excel

# Extract data from column 'A' starting from row 1 without row indices
data = get_column_data_from_excel('path/to/your/file.xlsx', row=1, column='A', index=False)
print(data)

# Extract data from column 'A' starting from row 1 with row indices
data_with_index = get_column_data_from_excel('path/to/your/file.xlsx', row=1, column='A', index=True)
print(data_with_index)
```

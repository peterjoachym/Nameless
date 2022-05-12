#data and file handling functions


# file handling functions
from io import TextIOWrapper

def get_data_to_change(filename: str) -> str:
    """open  txt file and extract file data"""
    opened_to_read = open(filename, "r")
    file_data = opened_to_read.read()
    return file_data


def open_to_write(filename: str) -> TextIOWrapper:
    """open file to write"""
    file_opened_to_write = open(filename, "w")
    return file_opened_to_write

# data handling functions

def x_filler(str_len: int) -> str:
    x_filled = ""
    for i in range(str_len):
        x_filled = x_filled + "X"
    return x_filled

def replace_str_by_x(file_data: str, str_list_to_replace: list) -> str:
    for str in str_list_to_replace:
        file_data = file_data.replace(str, x_filler(len(str)))
    return file_data
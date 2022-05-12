# function that replace personnal informations such as name, location, dates, tel. numbers by letter X
from Data import local_data as data
from blinder import file_data_func as file
from blinder import get_str_to_replace as get_str


# main function

def get_blinded_file(filename: str) -> None:
    """blind successively personnal data in .txt file """
    file_data = file.get_data_to_change(filename)
    file_data = file.replace_str_by_x(file_data, data.digits)
    file_data = file.replace_str_by_x(file_data, get_str.get_email(file_data))
    file_data = file.replace_str_by_x(file_data, get_str.get_links(file_data))
    file_data = file.replace_str_by_x(file_data, get_str.get_names_from_filedata(file_data))
    file_data = file.replace_str_by_x(file_data, get_str.get_names_from_filename(filename))
    # file_data = file.replace_str_by_x(file_data, data.data_to_blind)

    file.open_to_write(filename).write(file_data)


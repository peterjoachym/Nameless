from Data import local_data as data
from blinder import str_func


def get_names_from_filename(filename: str) -> list:
    """take filename of resume and transform it in names string array which contains all cap cases"""
    filename = str_func.del_from_str(filename, data.files_extensions)
    filename = str_func.del_from_str(filename, data.cv_strings)
    filename = str_func.replace_by_space(filename, data.separators)
    name_list = str_func.split_on_space(filename)
    name_list = str_func.remove_empty_strings(name_list)
    name_list = str_func.create_all_cases(name_list)
    return name_list

def get_names_from_filedata(file_data:str)->list:
    """get first two words from file data"""
    file_data_str_list = str_func.split_on_space(file_data)
    file_data_str_list = str_func.remove_empty_strings(file_data_str_list) 
    names_list = []
    names_list.append(file_data_str_list[0])
    names_list.append(file_data_str_list[1])
    names_list = str_func.remove_line_break(names_list)
    names_list=str_func.create_all_cases(names_list)
    return(names_list)

def get_links(file_data: str) -> list:
    """get internet links, github, linked in resume file"""
    file_data_str_list = str_func.split_on_space(file_data)
    links_str_list = []
    for element in file_data_str_list:
        if "/" in element:
            links_str_list.append(element)
    return links_str_list

def get_email(file_data: str) -> list:
    """get all string that contains @ in resumen file"""
    file_data_str_list = str_func.split_on_space(file_data)
    email_str_list = []
    for element in file_data_str_list:
        if "@" in element:
            email_str_list.append(element)
    return email_str_list

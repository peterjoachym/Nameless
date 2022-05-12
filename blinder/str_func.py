# filename handling functions

def del_from_str(filename: str, elements_to_del: list) -> str:
    """delete elements in argument from str"""
    for element in elements_to_del:
        filename = filename.replace(element, "")
    return filename    

def replace_by_space(filename: str, elements_to_del: list) -> str:
    """replace separators from elements_to_del from filename"""
    for element in elements_to_del:
        filename = filename.replace(element, " ")
    return filename    


def split_on_space(only_names: str) -> list:
    """split string on space"""
    name_list = only_names.split(" ")
    return name_list


def remove_empty_strings(element_list: list) -> list:
    """remove empty string from list"""
    for element in element_list:
        if element == "":
            element_list.remove(element)
    return element_list

def remove_line_break(element_list: list) -> list:
    """remove break line at the and of an string"""
    removed=[]
    for element in element_list:
        element = element.strip("\n")
        removed.append(element)
    return removed    

def create_all_cases(element_list: list) -> list:
    """create all upper or lower cases of strings in array"""
    all_cases_list = []
    for element in element_list:
        all_cases_list.append(element.capitalize())
        all_cases_list.append(element.upper())
    return all_cases_list


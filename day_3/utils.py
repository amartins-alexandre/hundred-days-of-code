def map_to_int_list(str_list: list) -> list:
    str_list = str_list.replace(',', '').split()
    return list(map(int, str_list))
def convert_dict_to_row(dict_data: dict, target_table: tuple):
    result = []
    for col in target_table:
        result.append(dict_data[col[1]])
    return result

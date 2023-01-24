import json

def tokenize_request(requete : str):
    tokens = requete.split()
    tokens_lower = [token.lower() for token in tokens]
    return tokens_lower

def import_json_to_dict(json_file_path):
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data

def filter_dict(my_dict : dict, list_keys):
    filtered_dict = {key: my_dict[key] for key in list_keys}
    return filtered_dict

def filter_dict_enhanced(my_dict : dict):
    list_values = list(my_dict.values())
    common_ids = []
    for value in list_values:   
        common_ids.append(list(value.keys()))
    common_ids = list(set.intersection(*map(set,common_ids)))
    for k,v in my_dict.items():
        new_v = filter_dict(v, common_ids)
        my_dict[k] = new_v
    return my_dict


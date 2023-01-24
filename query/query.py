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
    return my_dict, common_ids

def reinverse_dict(my_dict : dict, commond_ids : list):
    new_dict = dict.fromkeys(commond_ids, '')
    for k,v in new_dict.items():
        temp_dict = dict.fromkeys(list(my_dict.keys()), '')
        for k2,v2 in my_dict.items():
            temp_dict[k2] = v2[k]
        new_dict[k] = temp_dict
    return new_dict

def score(tokens : list, my_dict : dict):
    dict_copy = my_dict.copy()
    for k,v in dict_copy.items():
        keys = list(v.keys())
        i = 0
        while tokens[i] not in keys:
            tokens.pop[i]
        list_posi = []
        for key, value in v.items():
            list_posi.append(value['positions'])
        flatlist=[element for sublist in list_posi for element in sublist]
        dummy_tokens = ['blank' for i in range(max(flatlist) + 1)]
        for key, value in v.items():
            for i in value['positions']:
                dummy_tokens[i] = key
        j = 0
        while dummy_tokens[j] == 'blank':
            dummy_tokens.pop(j)
        intersection = len(list(set(tokens).intersection(dummy_tokens)))
        union = (len(tokens) + len(dummy_tokens)) - intersection
        score = float(intersection) / union
        v['score'] = score
    return dict_copy

def filtered_docs_by_ranking(ranked_dict : dict, doc_dict : dict):
    sorted_dict = dict(sorted(ranked_dict.items(), key=lambda x:x[1]['score']))
    keys_ranked = list(sorted_dict.keys())
    keys_ranked = [int(value) for value in keys_ranked]
    dummy_list = []
    for id in keys_ranked:
        doc = doc_dict[id]
        doc.pop('id')
        doc['Title'] = doc.pop('title')
        doc['URL'] = doc.pop('url')
        dummy_list.append(doc)
    return dummy_list

def export_dict_to_json(file_path, my_dict : list):
    with open(file_path, "w") as final:
        json.dump(my_dict, final)
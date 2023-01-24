import unittest
from query.query import *

class TestQuery(unittest.TestCase):
    
    def test_tokenize_request(self):
        requete = "Site OfficieL"
        actual = tokenize_request(requete=requete)
        expected = ['site', 'officiel']
        self.assertEqual(actual, expected)
    
    def test_filter_dict(self):
        my_dict = import_json_to_dict('index.json')
        list_keys = ['site', 'officiel']
        actual = filter_dict(my_dict, list_keys)
        expected = {'site': {'2': {'positions': [0], 'count': 1},
                    '20': {'positions': [4], 'count': 1},
                    '21': {'positions': [3], 'count': 1},
                    '23': {'positions': [3], 'count': 1},
                    '41': {'positions': [4], 'count': 1},
                    '101': {'positions': [0], 'count': 1},
                    '183': {'positions': [2], 'count': 1},
                    '274': {'positions': [0], 'count': 1},
                    '428': {'positions': [5], 'count': 1},
                    '497': {'positions': [4], 'count': 1}},
                    'officiel': {'2': {'positions': [1], 'count': 1},
                    '41': {'positions': [5], 'count': 1},
                    '101': {'positions': [1], 'count': 1},
                    '183': {'positions': [3], 'count': 1},
                    '428': {'positions': [6], 'count': 1}}}
        self.assertEqual(actual, expected)
    
    def test_filter_dict_enhanced(self):
        my_dict = {'site': {'2': {'positions': [0], 'count': 1},
                    '20': {'positions': [4], 'count': 1},
                    '21': {'positions': [3], 'count': 1},
                    '23': {'positions': [3], 'count': 1},
                    '41': {'positions': [4], 'count': 1},
                    '101': {'positions': [0], 'count': 1},
                    '183': {'positions': [2], 'count': 1},
                    '274': {'positions': [0], 'count': 1},
                    '428': {'positions': [5], 'count': 1},
                    '497': {'positions': [4], 'count': 1}},
                    'officiel': {'2': {'positions': [1], 'count': 1},
                    '41': {'positions': [5], 'count': 1},
                    '101': {'positions': [1], 'count': 1},
                    '183': {'positions': [3], 'count': 1},
                    '428': {'positions': [6], 'count': 1}}}
        actual_dict, actual_id = filter_dict_enhanced(my_dict)
        expected_dict = {'site': {'2': {'positions': [0], 'count': 1},
                        '41': {'positions': [4], 'count': 1},
                        '183': {'positions': [2], 'count': 1},
                        '101': {'positions': [0], 'count': 1},
                        '428': {'positions': [5], 'count': 1}},
                        'officiel': {'2': {'positions': [1], 'count': 1},
                        '41': {'positions': [5], 'count': 1},
                        '183': {'positions': [3], 'count': 1},
                        '101': {'positions': [1], 'count': 1},
                        '428': {'positions': [6], 'count': 1}}}
        expected_id = sorted(['101', '183', '2', '41', '428'])
        self.assertEqual(actual_dict, expected_dict)
        self.assertEqual(sorted(actual_id), expected_id)

    def test_reinverse_dict(self):
        my_dict = {'site': {'2': {'positions': [0], 'count': 1},
                    '41': {'positions': [4], 'count': 1},
                    '183': {'positions': [2], 'count': 1},
                    '101': {'positions': [0], 'count': 1},
                    '428': {'positions': [5], 'count': 1}},
                    'officiel': {'2': {'positions': [1], 'count': 1},
                    '41': {'positions': [5], 'count': 1},
                    '183': {'positions': [3], 'count': 1},
                    '101': {'positions': [1], 'count': 1},
                    '428': {'positions': [6], 'count': 1}}}
        common_ids = ['101', '183', '2', '41', '428']
        actual = reinverse_dict(my_dict, common_ids)
        expected = {'2': {'site': {'positions': [0], 'count': 1},
                    'officiel': {'positions': [1], 'count': 1}},
                    '41': {'site': {'positions': [4], 'count': 1},
                    'officiel': {'positions': [5], 'count': 1}},
                    '183': {'site': {'positions': [2], 'count': 1},
                    'officiel': {'positions': [3], 'count': 1}},
                    '101': {'site': {'positions': [0], 'count': 1},
                    'officiel': {'positions': [1], 'count': 1}},
                    '428': {'site': {'positions': [5], 'count': 1},
                    'officiel': {'positions': [6], 'count': 1}}}
        self.assertEqual(actual, expected)
    
    def test_score(self):
        tokens = ['site', 'officiel']
        my_dict = {'2': {'site': {'positions': [0], 'count': 1},
                    'officiel': {'positions': [1], 'count': 1}},
                    '41': {'site': {'positions': [4], 'count': 1},
                    'officiel': {'positions': [5], 'count': 1}},
                    '183': {'site': {'positions': [2], 'count': 1},
                    'officiel': {'positions': [3], 'count': 1}},
                    '101': {'site': {'positions': [0], 'count': 1},
                    'officiel': {'positions': [1], 'count': 1}},
                    '428': {'site': {'positions': [5], 'count': 1},
                    'officiel': {'positions': [6], 'count': 1}}}
        actual = score(tokens, my_dict)
        expected = {'2': {'site': {'positions': [0], 'count': 1},
                    'officiel': {'positions': [1], 'count': 1},
                    'score': 1.0},
                    '41': {'site': {'positions': [4], 'count': 1},
                    'officiel': {'positions': [5], 'count': 1},
                    'score': 1.0},
                    '183': {'site': {'positions': [2], 'count': 1},
                    'officiel': {'positions': [3], 'count': 1},
                    'score': 1.0},
                    '101': {'site': {'positions': [0], 'count': 1},
                    'officiel': {'positions': [1], 'count': 1},
                    'score': 1.0},
                    '428': {'site': {'positions': [5], 'count': 1},
                    'officiel': {'positions': [6], 'count': 1},
                    'score': 1.0}}
        self.assertEqual(actual, expected)
    
    def test_filtered_docs_by_ranking(self):
        ranked_dict = {'2': {'site': {'positions': [0], 'count': 1},
                    'officiel': {'positions': [1], 'count': 1},
                    'score': 1.0},
                    '41': {'site': {'positions': [4], 'count': 1},
                    'officiel': {'positions': [5], 'count': 1},
                    'score': 1.0},
                    '183': {'site': {'positions': [2], 'count': 1},
                    'officiel': {'positions': [3], 'count': 1},
                    'score': 1.0},
                    '101': {'site': {'positions': [0], 'count': 1},
                    'officiel': {'positions': [1], 'count': 1},
                    'score': 1.0},
                    '428': {'site': {'positions': [5], 'count': 1},
                    'officiel': {'positions': [6], 'count': 1},
                    'score': 1.0}}
        doc_dict = import_json_to_dict('documents.json')
        actual = filtered_docs_by_ranking(ranked_dict, doc_dict)
        expected = [{'Title': 'Site officiel des Amis du Cadre noir de Saumur',
                    'URL': 'http://www.amisducadrenoir.fr/'},
                    {'Title': 'Guitares Lâg : Le Site Officiel de la grande marque Française',
                    'URL': 'https://www.lagguitars.com/fr_FR/'},
                    {'Title': 'Paul Eluard site officiel - Paul Eluard',
                    'URL': 'https://eluard.org/'},
                    {'Title': 'Site Officiel de QRM - Quevilly Rouen Métropole',
                    'URL': 'https://qrm.fr/'},
                    {'Title': 'La Maison De Dietrich - Site Officiel France - Electroménager',
                    'URL': 'https://www.dedietrich-electromenager.fr/'}]
        self.assertEqual(actual, expected)
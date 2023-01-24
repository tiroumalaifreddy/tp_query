from query.query import *
import click

@click.command()
@click.option('--json_file_doc')
@click.option('--json_file_index')
@click.option('--query')
def run(json_file_doc, json_file_index, query):
    document = import_json_to_dict(json_file_doc)
    index = import_json_to_dict(json_file_index)
    tokens = tokenize_request(query)
    filtered_index = filter_dict(index, tokens)
    filtered_index_enhanced, common_ids = filter_dict_enhanced(filtered_index)
    inverted_index = reinverse_dict(filtered_index_enhanced, common_ids)
    index_with_score = score(tokens, inverted_index)
    docs_id_answer = filtered_docs_by_ranking(index_with_score, document)
    export_dict_to_json('results.json', docs_id_answer)


if __name__ == '__main__':
    run()
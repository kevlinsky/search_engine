from task_4.tf_idf import get_paragraphs_dict, get_lemmas_and_tokens


def create_inverted_index(page_tokens):
    all_tokens = list()

    for item in page_tokens.values():
        all_tokens += item

    unique_tokens = list(set(all_tokens))
    unique_tokens_dict_str = dict()
    unique_tokens_dict_int = dict()

    for token in unique_tokens:
        unique_tokens_dict_int[token] = list()
        unique_tokens_dict_str[token] = list()
        for page_num, tokens in page_tokens.items():
            if token in tokens:
                unique_tokens_dict_int[token].append(page_num)
                unique_tokens_dict_str[token].append(str(page_num))
                continue

    return unique_tokens_dict_int, unique_tokens_dict_str


def save_result_file(inverted_index_dict):
    with open('inverted_index.txt', 'w', encoding='utf-8') as file:
        for token, pages in inverted_index_dict.items():
            file.write(token + ': ' + ', '.join(pages) + '\n')


if __name__ == '__main__':
    paragraphs_dict = get_paragraphs_dict()
    print('Page parsed')

    lemmas, tokens = get_lemmas_and_tokens(paragraphs_dict)
    print('Lemmas and tokens were formed')

    inverted_index_dict_int, inverted_index_dict_str = create_inverted_index(tokens)
    print('Inverted index formed')

    save_result_file(inverted_index_dict_str)
    print('Result file saved')
